from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic import TemplateView, FormView, DetailView, ListView, CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy

from .models import Category, Product, Image, SubCategory
from .forms import CategoryForm, ProductForm, ImagesForm

from orders.models import Order
from orders.forms import OrderForm
from viewed.models import ViewedItem
from accounts.models import User


class CategoriesView(FormView, ListView):
    form_class = CategoryForm
    template_name = 'products/categories.html'
    model = Category
    context_object_name = 'categories'

    def form_valid(self, form):
        form.save()
        return redirect('categories')


class CategoryDetailView(DetailView):
    template_name = 'products/category.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        category = Category.objects.get(pk=pk)
        sub_categories = SubCategory.objects.filter(category=category)
        context['sub_categories'] = sub_categories
        return context


class SubCategoryDetailView(DetailView):
    template_name = 'products/sub_category.html'
    model = SubCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        sub_category = SubCategory.objects.get(pk=pk)
        category = sub_category.category
        products = Product.objects.filter(sub_category=sub_category)
        context['products'] = products
        context['category'] = category
        context['sub_category'] = sub_category
        return context


class SubCategoryOtherDetailView(DetailView):
    model = Category
    template_name = 'products/other.html'

    def get_context_data(self, **kwargs):
        context = super(SubCategoryOtherDetailView, self).get_context_data(**kwargs)
        category = Category.objects.get(pk=self.kwargs['pk'])
        sub_categories = SubCategory.objects.filter(category=category)
        products = Product.objects.filter(category=category)
        products_to_show = []
        for product in products:
            if not product.sub_category:
                products_to_show.append(product)
        context['category'] = category
        context['products'] = products_to_show
        return context


class ProductDetailView(DetailView, FormView, View):
    template_name = 'products/product.html'
    model = Product
    context_object_name = 'product'
    form_class = OrderForm

    def form_valid(self, form):
        new_order = form.save(commit=False)
        new_order.user = self.request.user
        product = Product.objects.get(pk=self.kwargs['pk'])
        new_order.product = product
        new_order.save()
        return redirect('profile', pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        user = product.user
        viewed = ViewedItem.objects.filter(user=self.request.user, product=product)
        if viewed:
            pass
        else:
            ViewedItem.objects.create(user=self.request.user, product=product)

        if product.quantity > 0:
            product.is_available = True
            product.save()
        images = product.product_images.all()

        context['images'] = images
        context['user'] = user
        return context


class UserProductsView(ListView, FormView):
    model = User
    form_class = ProductForm
    template_name = 'products/selling.html'

    def get_context_data(self, **kwargs):
        context = super(UserProductsView, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['pk'])
        products = Product.objects.filter(user=user)
        context['user'] = user
        context['products'] = products
        return context

    def get_queryset(self):
        products = Product.objects.filter(user=self.request.user)
        return products

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = self.request.user
            new_product.save()
            return redirect('add_images', pk=new_product.pk)
        else:
            return HttpResponse('Make sure you enter a valid title, price, quantity and chose a category for your product')


def load_sub_categories(request):
    category = request.GET.get('category')
    if category:
        sub_categories = SubCategory.objects.filter(category=category).order_by('title')
    else:
        sub_categories = SubCategory.objects.none()
    return render(request, 'products/selling_sub_categories_list_options.html', {'sub_categories': sub_categories})


class AddProductImageView(DetailView, FormView):
    model = Product
    form_class = ImagesForm
    template_name = 'products/images_form.html'

    def get_context_data(self, **kwargs):
        context = super(AddProductImageView, self).get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        context['product'] = product
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('images')
        product = self.get_object()
        if form.is_valid():
            form.save(commit=False)
            for image in files:
                i = Image.objects.create(product=product, image=image)
                i.save()
            form.save()
            return redirect('product', pk=product.pk)
        else:
            return self.form_invalid(form)


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('selling', kwargs={'pk': self.request.user.pk})


class DeleteProduct(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse_lazy('selling', kwargs={'pk': self.request.user.pk})