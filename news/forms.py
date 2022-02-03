from django import forms
from django.core.exceptions import ValidationError
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article
from re import match


class ArticleForm(forms.ModelForm):
    # Без связи с БД
    # title = forms.CharField(max_length=255, label='Заголовок новости',
    #                         widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}))
    #
    # text = forms.CharField(label='Контент',
    #                        widget=forms.Textarea(attrs={'class': 'form-control',
    #                                                     'id': 'exampleFormControlTextarea1',
    #                                                     'rows': '3'}))
    #
    # author = forms.CharField(max_length=100, label='Автор',
    #                          widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}))
    #
    # is_published = forms.BooleanField(label='Опубликовать?', required=False,
    #                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input',
    #                                                                     'id': 'exampleCheck1'}))
    #
    # category = forms.ModelChoiceField(Category.objects.all(), label='Категории', empty_label='Выбери категорию',
    #                                   widget=forms.Select(attrs={'class': "form-select"}))

    class Meta:
        model = Article
        # fields = "__all__"  # все поля
        fields = ['title', 'text', 'author', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}),
            # 'text': forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea1', 'rows': '3'}),
            'text': CKEditorUploadingWidget(attrs={'class': 'form-control',
                                                   'id': 'exampleFormControlTextarea1', 'rows': '3'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'exampleCheck1'}),
            'category': forms.Select(attrs={'class': "form-select"})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        else:
            return title
