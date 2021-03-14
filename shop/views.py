from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.db.models import Q
#Shop 
from django.views.generic import ListView
from django.views.generic.base import View
from django.http import JsonResponse
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.

class FilterProductView(ListView):
	model = Product
	template_name = 'list.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = Product.objects.filter(
			Q(name__icontains = query) | Q(description__icontains = query)
			)
		return object_list




def login(request):
	return render(request, 'sign-in.html')

# @login_required
def homeView(request):
	category = Categories.objects.all()

	products = Product.objects.all()

	context = {
		'categories':category,
		'products':products,
	}
	return render(request, 'home.html', context)

def order(request):
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('shop:homePage'))
        
        else:
            return HttpResponseRedirect(reverse('shop:checkout'))  
    else:
        form=OrderForm()
    return render(request,'checkout.html', {'form':form})


def category_detail(request, c_slug):
	category = get_object_or_404(SubCategory,slug=c_slug)
	products = Product.objects.filter(subcategory=category)

	context = {'products':products}
	
	return render(request, 'category.html',context )

def tag_detail(request, tag_slug):
	tag = get_object_or_404(Tag,slug=tag_slug)
	products = Product.objects.filter(tag=tag)

	context = {'products':products}
	
	return render(request, 'tags.html',context )




def detail(request, p_slug):
	product = get_object_or_404(Product, slug=p_slug)
	context =  {'product':product}
	return render(request, 'detail.html',context)


def blog(request):
	posts = Post.objects.all().order_by('-id')[:10]
	return render(request, 'blog.html', {'posts':posts})

def blog_detail(request, post_slug):
	post = get_object_or_404(Post, slug=post_slug)
	return render(request, 'blog-details.html', {'post':post})



def cart_init(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
	except:
		cart = Cart.objects.create()
		request.session['cart_id'] = cart.id
	return cart


def cart_delete_item(request):
	cart = cart_init(request)
	product_id = request.GET.get('data')
	cart_remove = cart.remove(product_id)
	#item = CartProduct.objects.get()
	data = {
		'cart_total_price':cart.total_price,
		'ok':200
		}
	if cart:
		return JsonResponse(data)

class CartView(View):

	def get(self,request):
		status = {}
		product_id = request.GET.get('data')
		cart = cart_init(request)
		check_product = cart.add(product_id)
		if check_product:			
			status["status"] = "OK"
		else:
			status["status"] = "Product was added to cart"
		return JsonResponse(status)


class CartProducts(ListView):
	template_name = 'shopping-cart.html'

	def get_queryset(self):
		return "qale"

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    cart = cart_init(self.request)
	    context['cart_products'] = cart.products.all()
	    context['cart'] = cart

	    return context

def change_cart(request, product_id, last_qty):
	d = request.GET.get('data')
	data = json.loads(d)
	p_id = data['product_id']
	cart = cart_init(request)
	product = cart.products.get(id=p_id)
	item.total_price = product.price * quanty
	cart_change = cart.change(product_id, last_qty)
	data = {
		'item_total':item.total_price,
		'total_price':cart.total_price,
		'ok':200
		}

	if cart:
		return JsonResponse(data)

