from django.shortcuts import render, get_object_or_404
from blog.models import ArticleModel, CatagoryModel
from django.core.paginator import Paginator


def category(request, categorySlug):
    category = get_object_or_404(CatagoryModel, slug=categorySlug)
    articles = category.article.order_by("-id")
    page = request.GET.get('page')
    paginator = Paginator(articles, 1)

    return render(request, "pages/category.html", context={
        "articles": paginator.get_page(page),
        "categoryName": category.categoryName
    })
