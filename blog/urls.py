from django.urls import path, include
from blog.views import contact, index, category, myArticles, articlePage

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('my-articles', myArticles, name='my-articles'),
    path('article-page/<slug:slug>', articlePage, name='article-page')
]
