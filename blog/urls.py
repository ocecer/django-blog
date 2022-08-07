from venv import create
from django.urls import path, include
from blog.views import contact, index, category, myArticles, articlePage, createPost, updatePost, deletePost
from blog.views.createPost import createPost

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('my-articles', myArticles, name='my-articles'),
    path('article-page/<slug:slug>', articlePage, name='article-page'),
    path('create-post', createPost, name='create-post'),
    path('update-post/<slug:slug>', updatePost, name='update-post'),
    path('delete-post/<slug:slug>', deletePost, name='delete-post'),
]
