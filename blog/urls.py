from django.urls import path, include
from blog.views import ContactFormView, index, CategoryListView, myArticles, ArticleView, CreatePostView, UpdatePostView, DeletePostView, deleteComment
# from blog.views.createPost import CreatePostView
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', index, name='home'),
    path('contact', ContactFormView.as_view(), name='contact'),
    path('about-us', TemplateView.as_view(template_name='pages/about-us.html'),
         name='about-us'),
    path('redirect', RedirectView.as_view(url='/'), name='redirect'),
    path('category/<slug:categorySlug>',
         CategoryListView.as_view(), name='category'),
    path('my-articles', myArticles, name='my-articles'),
    path('article-page/<slug:slug>', ArticleView.as_view(), name='article-page'),
    path('create-post', CreatePostView.as_view(), name='create-post'),
    path('update-post/<slug:slug>', UpdatePostView.as_view(), name='update-post'),
    path('delete-post/<slug:slug>', DeletePostView.as_view(), name='delete-post'),
    path('delete-comment/<int:id>', deleteComment, name='delete-comment'),
]
