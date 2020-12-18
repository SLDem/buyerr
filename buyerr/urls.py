"""buyerr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products.views import CategoriesView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', CategoriesView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('questions/', include('questions.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('viewed/', include('viewed.urls')),
    path('reviews/', include('reviews.urls')),
    path('messages/', include('user-messages.urls')),
    path('search/', include('search.urls')),
    path('ratings/', include('ratings.urls')),
    path('payment/', include('payment.urls')),
    path('bought/', include('bought.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
