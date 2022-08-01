from django.contrib import admin
from blog.models import CatagoryModel, ArticleModel

# Register your models here.
admin.site.register(CatagoryModel)


class ArticlesAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = ("title", "creationDate", "editDate")


admin.site.register(ArticleModel, ArticlesAdmin)
