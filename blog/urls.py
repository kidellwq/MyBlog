from django.urls import path
from .views import IndexView, PostDetailView, ArchivesView, CategoryView, TagView, search


app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', ArchivesView.as_view(), name='archives'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('tag/<int:pk>/', TagView.as_view(), name='tag'),
    path('search/', search, name='search'),
]
