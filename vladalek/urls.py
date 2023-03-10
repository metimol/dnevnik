from django.contrib import admin
from django.urls import path, include

urlpatterns = [
		path('grappelli/', include('grappelli.urls')),
		path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
]

handler404 = "vladalek.views.page_not_found_view"
