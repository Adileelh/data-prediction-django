
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('predict/', views.predict, name='predict'),
    path('contact', views.contact, name='contact')


]
