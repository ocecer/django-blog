from django.urls import path, include
from blog.views import contact, index

urlpatterns = [
    path('', index),
    path('contact', contact),
]
