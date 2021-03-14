from django.forms import ModelForm,Textarea
from .models import Order

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ('customer','payed')
		widgets = {
			'message':Textarea(attrs={'rows':10,'cols':70}),
		}