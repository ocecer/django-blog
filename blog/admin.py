from django.contrib import admin
from blog.models import CatagoryModel, ArticleModel, CommentModel, ContactModel

# Register your models here.
admin.site.register(CatagoryModel)


class ArticlesAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = ("title", "creationDate", "editDate")


admin.site.register(ArticleModel, ArticlesAdmin)


class CommentAdmin(admin.ModelAdmin):
    search_fields = ("author__username",)
    list_display = ("author", "creationDate", "editDate")


admin.site.register(CommentModel, CommentAdmin)


class ContactAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    list_display = ("email", "creationDate")


admin.site.register(ContactModel, ContactAdmin)
