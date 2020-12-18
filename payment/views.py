from django.shortcuts import render, reverse, HttpResponse
from django.conf import settings
from django.views.generic import TemplateView
import stripe

from orders.models import Order
from bought.models import BoughtProduct


def checkout_session(request, pk):
    order = Order.objects.get(pk=pk)
    total_price = order.product.price * order.quantity

    product = order.product
    if order.quantity > product.quantity:
        return HttpResponse('Order quantity exceeds product quantity, please pick a lesser amount.')
    product.quantity -= order.quantity
    product.save()
    if product.quantity <= 0:
        product.is_available = False
        product.quantity = 0
        product.save()
    order.delete()

    image = product.product_images.first()
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': order.product.price * 100,
                    'product_data': {
                        'name': order.product.title,
                        'images': None, #fix this
                    },
                },
                'quantity': order.quantity,
            },
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('categories')),
    )

    # send email to the user whose product was bought / shop

    bought = BoughtProduct.objects.create(user=request.user, quantity=order.quantity, product=product)

    return render(request, 'payment/checkout.html', {'session_id': session.id,
                                                     'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
                                                     'order': order,
                                                     'image': image,
                                                     'total_price': total_price})


def stripe_webhook(request):
    endpoint_secret = 'whsec_T8NO5xOwc6F5Lwjiy8t4DW0GpFaYQGxr'
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object  # contains a stripe.PaymentIntent
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object  # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event.type))

    if event.type == 'checkout.session.completed':
        session = event['data']['object']
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)

    return HttpResponse(status=200)


class ThanksView(TemplateView):
    template_name = 'payment/thanks.html'