from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Articles
from django.db.models.functions import Extract

def categories(request):
	def get_dates(articles):
		dates = articles.annotate(month = Extract('pub_date', 'month'), year = Extract('pub_date', 'year')).values('month', 'year').distinct()
		return [f'{date["month"]} - {date["year"]}' for date in dates]
	articles = Articles.objects.all()
	dates = get_dates(articles)
	context = {'dates': dates}
	return render(request, 'blog/categories.html', context,)

def index(request):
	def get_articles_by_date(articles, date):
		month, year = date.split(' - ')
		return articles.filter(pub_date__month=month, pub_date__year=year)
	date = request.GET.get('date', '')
	if date:
		articles = Articles.objects.all()
		articles_list = get_articles_by_date(articles, date)
		context = {'articles_list': articles_list}
		return render(request, 'blog/index.html', context,)
	else:
		return render(request, "404.html")

def detail(request, article_id):
	try:
		a = Articles.objects.get(id = article_id)
	except:
		return render(request, "404.html")
	context = {'a': a}
	
	return render(request, 'blog/detail.html', context,)
