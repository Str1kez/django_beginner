from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ArticleForm
from .models import Article, Category


class NewsListView(ListView):
    model = Article
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 3
    # allow_empty = False  # Инициализирует доп запрос к бд
    # extra_context = {'title': 'News'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        # можно было использовать extra_context, так как тут он статичен
        return context

    def get_queryset(self):
        return Article.objects.select_related('category')


# Create your views here.
# def index(request):
    # articles = Article.objects.order_by('-created_at')  не нужно, так как в мете для админки уже отсортировали
    # articles = Article.objects.all()
    # return render(request, 'news/index.html', {'news': articles, 'title': 'Новости'})


# думаю можно унаследовать от предыдущего класса, так как атрибуты одинаковы
class NewsByCategoryListView(NewsListView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(id=self.kwargs.get('category_id'))
        return context

    def get_queryset(self):
        return Article.objects.filter(category=self.kwargs.get('category_id')).select_related('category')


# def get_category(request, category_id):
#     articles = Article.objects.filter(category_id=category_id)
#     category = Category.objects.get(id=category_id)
#     return render(request, 'news/index.html', {'news': articles, 'title': category})


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'news/article.html'
    # pk_url_kwarg = 'article_id'  Если не менять article_id в get_absolute_url и в url (по конвенции)


# def get_article(request, article_id):
#     article = get_object_or_404(Article, id=article_id)
#     return render(request, 'news/article.html', {'article': article})


class ArticleCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = 'news/add_article.html'
    permission_denied_message = 'Вы не авторизованы!'
    login_url = '/admin/'

    # success_url = reverse_lazy('home')  Если не хотим, чтобы переходило по пути absolute_url
    # reverse_lazy выполняется в ходе работы, обычный не знает, что за путь 'home'


# def add_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = form.save()
#             # article = Article.objects.create(**form.cleaned_data)
#             # так как там есть метод get_absolute_url
#             return redirect(article)
#     else:
#         form = ArticleForm()
#     return render(request, 'news/add_article.html', {'form': form})
