
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .views import  test5, test6, Home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include("Products.urls", namespace="product")),
    path('comment/', include('Comment.urls', namespace="comment")),
    path('user/', include('User.urls', namespace="user")),
    path("home/", Home.as_view(), name='home'),
    path("test5/", test5),
    path("test6/", test6),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
