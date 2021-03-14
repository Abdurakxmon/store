from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id','name',]
	list_display_links = ['name', ]
	prepopulated_fields = {'slug':('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ['id','name',]
	list_display_links = ['name', ]
	list_filter = ['name']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['id','name',]
	list_display_links = ['name', ]
	prepopulated_fields = {'slug':('name',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['email','payed','payment_type',]
	list_display_links = ['payed', ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id','title',]
	list_display_links = ['title', ]
	prepopulated_fields = {'slug':('title',)}

	
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(SliderContent)
admin.site.register(Cart)
admin.site.register(CartProduct)

class ProductImageAdmin(admin.StackedInline):
	model =  ProductImages



# Product
@admin.register(Product)
class ProAdmin(admin.ModelAdmin):
	inlines = [ProductImageAdmin]
	list_display = ['name', 'category', 'instock']
	list_display_links = ['name', ]
	prepopulated_fields = {'slug':('name',)}

	class Meta:
		model = Product


@admin.register(ProductImages)
class PrImAdmin(admin.ModelAdmin):
	pass