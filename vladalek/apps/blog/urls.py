from django.urls import path
from .views import index, detail, categories

app_name = 'blog'
urlpatterns = [
	path('categories/', categories, name='categories'),
	path('articles/', index, name='index'),
	path('<int:article_id>/', detail, name='detail'),
]