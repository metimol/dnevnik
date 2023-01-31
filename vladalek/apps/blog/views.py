from django.shortcuts import render
from .models import Articles
from django.db.models.functions import Extract

def index(request):
	def get_articles_by_date(articles, date):
		RUSSIAN_MONTH_NAMES = (
			'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
			'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
		)
		month_name, year = date.split(' - ')
		month = RUSSIAN_MONTH_NAMES.index(month_name) + 1
		return articles.filter(pub_date__month=month, pub_date__year=year)
	def get_dates(articles):
		def get_russian_month_name(month_number):
			RUSSIAN_MONTH_NAMES = (
				'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
				'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
			)
			return RUSSIAN_MONTH_NAMES[month_number - 1]
		dates = articles.annotate(month = Extract('pub_date', 'month'), year = Extract('pub_date', 'year')).values('month', 'year').distinct()
		text_dates = [f'{get_russian_month_name(date["month"])} - {date["year"]}' for date in dates]
		return text_dates
	date = request.GET.get('date', '')
	articles = Articles.objects.all()
	if date:
		try:
			articles_list = get_articles_by_date(articles, date)
			images = ["https://images.unsplash.com/photo-1491900177661-4e1cd2d7cce2?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=2250&q=80", "https://images.unsplash.com/photo-1498307833015-e7b400441eb8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=2600&q=80", "https://images.unsplash.com/photo-1482192505345-5655af888cc4?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=2600&q=80", "https://images.unsplash.com/photo-1564604761388-83eafc96f668?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=2250&q=801.2.1&auto=format&fit=crop&w=2167&q=80"]
		except:
			return render(request, "404.html")
		context = {'articles_list': articles_list, 'images': images}
		return render(request, 'blog/index.html', context,)
	else:
		dates = get_dates(articles)
		context = {'dates': dates}
		return render(request, 'blog/categories.html', context,)

def detail(request, article_id):
	try:
		a = Articles.objects.get(id = article_id)
	except:
		return render(request, "404.html")
	context = {'a': a}
	
	return render(request, 'blog/detail.html', context,)
