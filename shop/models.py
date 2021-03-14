from django.db import models
from django.contrib.auth.models import User
#Utilites for shop 
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.


# Categories model
class Categories(models.Model):
	name = models.CharField('Nomi', max_length=50)
	slug = models.SlugField('*',max_length=50, unique=True, db_index=True)
	hot = models.BooleanField("Mashxur", default=False)

	def get_absolute_url(self):
		return reverse('shop:category_detail', kwargs={'c_slug':self.slug})

	class Meta:
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'

	def __str__(self):
		return f"Kategoriya - {self.name}"

class SubCategory(models.Model):
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Kategoriya')
	name = models.CharField(max_length=25, unique=True, verbose_name='Nomi')
	slug = models.SlugField('*',max_length=50, unique=True, db_index=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:category_detail', kwargs={'c_slug':self.slug})

	class Meta:
		verbose_name_plural = 'Kategoriya osti Kategoriyalar'
		verbose_name = 'Kategoriya osti Kategoriya'
		ordering = ['name']
# Tag model

class Tag(models.Model):
	name = models.CharField('Nomi', max_length=50)
	slug = models.SlugField('*',max_length=50, unique=True, db_index=True)

	def get_absolute_url(self):
		return reverse('shop:tag_detail', kwargs={'tag_slug':self.slug})

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Taglar'

	def __str__(self):
		return f"Tag - {self.name}"


# Product  model
class Product(models.Model):
	CHOICES = (
		('white','WHITE'),
		('black','BLACK'),
		('blue','BLUE'),
		('green','GREEN'),
		('yellow','YELLOW'),
		('red','RED'),
		('tomato','TOMATO'),
		('pink','PINK'),
		('teal','TEAL'),
		('brown','BROWN'),
		)

	name = models.CharField('Tovar nomi', max_length=50)
	slug = models.SlugField('*', max_length=50)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category', null=True)
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
	tag = models.ForeignKey(Tag, on_delete=models.PROTECT, blank=True, null=True)
	image = models.ImageField('Rasmi',upload_to="product_images/")
	description = models.TextField('Tovar haqida', blank=True)
	price = models.PositiveIntegerField('Narxi', default=0, null=True)
	old_price = models.PositiveIntegerField('Avvalgi Narxi', default=0, blank=True)
	colors = models.CharField('Ranglari', max_length=50, choices=CHOICES )
	instock = models.BooleanField("Omborda bor yoki yo'q", default=True)
	count = models.PositiveIntegerField('Soni', default=1)

	new = models.BooleanField('Yangi', default=True)
	hot = models.BooleanField('Hot', default=False)
	special = models.BooleanField('Maxsus taklif', default=False)

	def get_absolute_url(self):
		return reverse('shop:product_detail', kwargs={'p_slug':self.slug})

	class Meta:
		verbose_name = 'Tovar'
		verbose_name_plural = 'Tovarlar'

	def __str__(self):
		return f"Tovar - {self.name}"

# Product Images model
class ProductImages(models.Model):
	product = models.ForeignKey(Product,default=None, null=True, blank=True, on_delete=models.CASCADE)
	image = models.ImageField('Tovar alohida rasmlari', upload_to='product_images/', blank=True, null=True)

	def __str__(self):
		return self.product.name

	class Meta:
		verbose_name = 'Tovar rasmlari'
		verbose_name_plural = 'Tovar rasmlari'


class CartProduct(models.Model):
	product = models.ForeignKey(Product, verbose_name='Tovar', on_delete=models.CASCADE)
	quanty = models.PositiveIntegerField(default=1)
	price = models.PositiveIntegerField(default=0, verbose_name='Tovar narxi')

	def __str__(self):
		return "Tovar {}, (Savatcha uchun)".format(self.product.name)

	# @staticmethod	
	# def cart_products_list(cart):
	# 	cart_products = CartProducts.objects.filter(savatcha_tovar=cart)
	# 	return cart_products
			

class Cart(models.Model):
	#owner = models.ForeignKey(Customer, verbose_name='Xaridor', on_delete=models.CASCADE)
	products = models.ManyToManyField(CartProduct, null=True, related_name='savatcha_tovar')
	total_products = models.PositiveIntegerField(default=0)
	total_price = models.PositiveIntegerField(default=0, verbose_name='Umumiy narxi')

	def __str__(self):
		return str(self.id)

	def add(self, product_id):
		product = Product.objects.get(id=product_id)
		cart_products = self.products.all()
		for i in cart_products:
			if product == i.product:
				return False		
		else:
			#create product to CartProducts
			self.products.create(product=product, price=product.price)
			self.total_products = self.products.all().count()
			self.total_price += product.price 
			self.save()
			return True

	def remove(self,product_id):
		product = Product.objects.get(id=product_id)
		item = self.products.get(product=product)
		self.products.remove(item)
		self.total_price -= item.price
		self.total_products -= item.quanty
		self.save()
		item.delete()
		return True

	def change(self, product_id, quanty):
		product = Product.objects.get(id=product_id)
		item = self.products.get(product=product)
		item.quanty = quanty
		item.price = quanty * product.price
		item.save()


# Blog Page Mode

class Post(models.Model):
	title = models.CharField('Sarlavha', max_length=550)
	slug = models.SlugField('*',max_length=150, unique=True, db_index=True)
	body = RichTextField()
	image = models.ImageField('Poster', upload_to='blog_images/')
	author = models.CharField('Muallif', max_length=50, blank=True, default='Admin')
	published = models.DateTimeField('Vaqti', auto_now_add=True)

	def get_absolute_url(self):
		return reverse('shop:blogDetailPage', kwargs={'post_slug':self.slug})
		
	class Meta:
		verbose_name = 'Maqola'
		verbose_name_plural = 'Maqolalar'

	def __str__(self):
		return f"Maqola - {self.title}"


# Comment Page Model

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	name = models.CharField('Ismi', max_length=50)
	email = models.EmailField('Email', max_length=224)
	title = models.CharField('Mavzu', max_length=150)
	comment = models.TextField('Xabar')

	class Meta:
		verbose_name = 'Muhokama'
		verbose_name_plural = 'Muhokamalar'

	def __str__(self):
		return f"Muhokama - {self.name}"

# Contact Page Model

class Contact(models.Model):
	name = models.CharField('Ismi', max_length=50)
	email = models.EmailField('Email', max_length=224)
	title = models.CharField('Mavzu', max_length=150)
	comment = models.TextField('Xabar')

	class Meta:
		verbose_name = 'Aloqa'
		verbose_name_plural = 'Aloqalar'

	def __str__(self):
		return f"Xabar - {self.name}"


class SliderContent(models.Model):
	brand_tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
	brand_title = models.CharField('Brand nomi', max_length=50)
	brand_desc = models.CharField('Brand haqida', max_length=200)
	brand_poster = models.ImageField('Brand poster', upload_to='posters/')

	def get_absolute_url(self):
		return reverse('shop:tag_detail', kwargs={'tag_slug':self.brand_tag.slug})

	class Meta:
		verbose_name = 'Slayder'
		verbose_name_plural = 'Slaydlar'

	def __str__(self):
		return f"Kategoriya - {self.brand_title}"


class Order(models.Model):
	Pay=(('cash','CASH'),
		 ('click','CLICK'),
		 ('PayMe','PAYME'),
		 ('oson','OSON'),)

	customer = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
	phone = models.CharField('Phone',max_length=50)
	email = models.EmailField('E-mail',max_length=50)
	tm_id = models.CharField('tm_id',max_length=50, blank=True)
	state = models.CharField('State',max_length=50)
	province = models.CharField('Province',max_length=50)
	district = models.CharField('District',max_length=50)
	street = models.CharField('Street',max_length=50)
	residence_address = models.CharField('Home_adress',max_length=50)
	postal_code = models.PositiveIntegerField('Postal_code')
	payment_type = models.CharField('Payment_type', max_length=50, choices=Pay )
	message = models.TextField('Additional_message', blank=True)
	payed = models.BooleanField('Payed', default=False)

	class Meta:
		verbose_name = 'order'
		verbose_name_plural = 'orders'

	def __str__(self):
		return f"{self.payed}"

