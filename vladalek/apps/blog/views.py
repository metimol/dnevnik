import string
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Articles, Categories

def index(request):
	category = request.GET.get('category', '')
	page_num = request.GET.get('page', '')
	categories_list = Categories.objects.order_by('category')
	if category:
		try:
			cat = Categories.objects.get(category=category)
			articles_list = cat.articles.order_by('-id')
		except:
			return render(request, "404.html")
	else:
		articles_list = Articles.objects.order_by('-id')
	if articles_list:
		paginator = Paginator(articles_list, 10)
		if not page_num:
			page_num = 1
		page = paginator.get_page(page_num)
		page_list = []
		if paginator.num_pages>1:
			if paginator.num_pages>7:
				if int(page_num)<paginator.num_pages-5:
					for i in range(int(page_num), int(page_num)+5):
						page_list.append(i)
				else:
					for i in range(paginator.num_pages-5, paginator.num_pages):
						page_list.append(i)
			else:
				for i in range(1, paginator.num_pages+1):
					page_list.append(i)
		context = {'page': page, 'articles_list': page.object_list, 'categories_list': categories_list, 'category': category, 'paginator': paginator, 'page_list':page_list}
	else:
		return render(request, "blog/index.html", {"categories_list": categories_list})
	
	return render(request, 'blog/index.html', context,)

def detail(request, article_id):
	try:
		a = Articles.objects.get(id = article_id)
	except:
		return render(request, "404.html")
	context = {'a': a}
	
	return render(request, 'blog/detail.html', context,)
