from django.urls import path
from .import views


app_name = 'shop'

urlpatterns = [
	path('', views.homeView, name='homePage'),
	path('results/', views.FilterProductView.as_view(), name='search_result'),
	path('<str:c_slug>', views.category_detail, name='category_detail'),
	path('tag/<str:tag_slug>', views.tag_detail, name='tag_detail'),
	path('products/<str:p_slug>', views.detail, name='product_detail'),
	#Blog and Contact Views
	path('blog/', views.blog, name='blogPage'),
	path('blog/<str:post_slug>', views.blog_detail, name='blogDetailPage'),
	path('checkout/', views.order,name="checkout"),
	path('cart/', views.CartView.as_view(), name='cart'),
	path('cart-products/', views.CartProducts.as_view(), name='cart_products'),
	path('delete_item/', views.cart_delete_item, name='cart_delete_item'),
	path('change_cart/', views.change_cart, name='change_cart'),

]