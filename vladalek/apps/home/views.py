from django.shortcuts import render
from blog.models import Articles

def index(request):
	articles_list = Articles.objects.order_by('-id')[:3]
	context = {'articles_list': articles_list}
	return render(request, 'home/index.html', context,)
