from django.db import models
from autoslug import AutoSlugField
from blog.models import CatagoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class ArticleModel(models.Model):
    articleImage = models.ImageField(upload_to="article_images")
    title = models.CharField(max_length=50)
    content = RichTextField()
    creationDate = models.DateTimeField(auto_now_add=True)
    editDate = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    categories = models.ManyToManyField(CatagoryModel, related_name="article")
    author = models.ForeignKey(
        "account.CustomUserModel", on_delete=models.CASCADE, related_name="aricles")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "Article"

    def __str__(self):
        return self.title
