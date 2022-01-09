from django.contrib import admin
from .models import Article, Category

# Register your models here.
# sudo ilya 1111


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author')  # регистр не имеет значения только на англ
    list_filter = ('category', 'is_published')
    list_editable = ('is_published', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
