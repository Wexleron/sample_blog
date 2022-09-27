from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from sample_blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('api/', include('blog_api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
