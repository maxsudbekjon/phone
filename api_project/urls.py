from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from phones.views import PhoneListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/phones/', PhoneListView.as_view(), name='phone-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
