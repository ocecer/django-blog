from django.shortcuts import get_object_or_404, render
from blog.models import ArticleModel


def articlePage(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    comments = article.comments.all()
    return render(request, 'pages/article-page.html', context={
        'article': article,
        'comments': comments
    })
