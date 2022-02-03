from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article, Category

# Register your models here.
# sudo ilya 1111


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'category', 'author', 'created_at', 'updated_at', 'is_published', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author')  # регистр не имеет значения только на англ
    list_filter = ('category', 'is_published')
    list_editable = ('is_published', )
    actions_on_top = True
    fields = ('title', 'category', 'author', 'text', 'is_published', 'image', 'get_image', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'get_image')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="Не прогрузилась" width=75>')

    get_image.short_description = 'Картинка'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
