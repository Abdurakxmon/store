from django.urls import path, include

app_name = 'customer'

urlpatterns = [
	path('social-auth/', include('social_django.urls', namespace="social")),
	path('login/', views,LoginView.as_view(), name='login'),
]