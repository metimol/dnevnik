from django.urls import path
from .views import index, detail

app_name = 'blog'
urlpatterns = [
	path('', index, name='index'),
	path('<int:article_id>/', detail, name='detail'),
]