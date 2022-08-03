from django.urls import path, include
from blog.views import contact, index, category, myArticles

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('my-articles', myArticles, name='my-articles')
]
