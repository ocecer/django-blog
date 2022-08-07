from django.shortcuts import render, redirect
from blog.forms import AricleWriteModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def createPost(request):
    form = AricleWriteModelForm(
        request.POST or None, files=request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        form.save_m2m()
        return redirect('article-page', slug=article.slug)

    return render(request, 'pages/create-post.html', context={'form': form})
