from django.shortcuts import get_object_or_404, render
from blog.models import ArticleModel
from blog.forms import CommentCreateModelForm


def articlePage(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    comments = article.comments.all()

    if request.method == 'POST':
        createCommentForm = CommentCreateModelForm(data=request.POST)
        if createCommentForm.is_valid():
            comment = createCommentForm.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
    
    createCommentForm = CommentCreateModelForm()

    return render(request, 'pages/article-page.html', context={
        'article': article,
        'comments': comments,
        'createCommentForm': createCommentForm
    })
