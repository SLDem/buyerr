from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.CategoriesView.as_view(), name='categories'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category'),
    path('sub-category/<int:pk>/', views.SubCategoryDetailView.as_view(), name='sub_category'),
    path('other/<int:pk>/', views.SubCategoryOtherDetailView.as_view(), name='other'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('selling/<int:pk>/', views.UserProductsView.as_view(), name='selling'),
    path('add-images/<int:pk>/', views.AddProductImageView.as_view(), name='add_images'),
    path('delete-product/<int:pk>/', views.DeleteProduct.as_view(), name='delete_product'),
    path('update-product/<int:pk>/', views.UpdateProduct.as_view(), name='update_product'),
    path('ajax/load-sub-categories/', views.load_sub_categories, name='load_sub_categories'),
]
