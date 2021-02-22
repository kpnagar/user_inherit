from django.urls import path, include
from .views import (
                        ArticleListView,
                        ArticleUpdateView,
                        ArticleDetailView,
                        ArticleDeleteView, # new
                        ArticleCreateView,
                    )

urlpatterns = [
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'), # new
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'), # new
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'), # new
    path('', ArticleListView.as_view(), name='article_list'),
]
