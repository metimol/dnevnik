from django.db import models
from tinymce.models import HTMLField

class Categories(models.Model):
	category = models.CharField(max_length=25,  verbose_name='Категория', help_text='Название категории')
	def __str__ (self):
		return self.category
	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

class Articles(models.Model):
	categories = models.ForeignKey(Categories, null=True, related_name = "articles", on_delete = models.SET_NULL, verbose_name='Категория')
	article_text = HTMLField(help_text='Текст статьи', verbose_name='Текст статьи')
	article_about = models.TextField(help_text='О чём статья', verbose_name='Описание статьи', null=True)
	article_private = models.BooleanField(default=False, verbose_name="Приватная")
	pub_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.pub_date)
	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'
