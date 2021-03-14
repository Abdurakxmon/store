from .models import *
from .views import cart_init
""" Context Proccessor """


def view(request):
	cart = cart_init(request)
	context = {
		'cart':cart,
		'cart_products':CartProduct.objects.all(),
		'tags':Tag.objects.all(),
		'slider_contents':SliderContent.objects.all()[:3],
		'new_products':Product.objects.filter(new=True),
		'hot_products':Product.objects.filter(hot=True),
		'special_products':Product.objects.filter(special=True),
	}
	return context