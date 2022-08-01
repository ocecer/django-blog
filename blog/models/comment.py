from django.db import models
from django.contrib.auth.models import User
from blog.models import ArticleModel


class CommentModel(models.Model):
    author = models.ForeignKey(
        "account.CustomUserModel", on_delete=models.CASCADE, related_name="comment")
    article = models.ForeignKey(
        ArticleModel, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    creationDate = models.DateTimeField(auto_now_add=True)
    editDate = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "comment"

    def __str__(self):
        return self.author.username
