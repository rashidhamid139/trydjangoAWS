from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
]
