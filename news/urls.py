from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import NewsListView, NewsByCategoryListView, ArticleDetailView, ArticleCreateView

app_name = 'news'

urlpatterns = [
    # path('', index, name='home'),
    path('', NewsListView.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    # в as_view можно передать атрибуты класса, не указывая их в views
    path('category/<int:category_id>/', NewsByCategoryListView.as_view(), name='category'),
    # path('article/<int:article_id>/', get_article, name='article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    # path('add_article', add_article, name='add_article')
    path('add_article', ArticleCreateView.as_view(), name='add_article')
]

# так как картинка находится просто в варчар 100, то нужно указать, куда ее сохраняют
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
