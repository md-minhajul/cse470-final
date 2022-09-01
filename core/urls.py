from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


from apps.services.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('account/', include('apps.accounts.urls', namespace='accounts')),
    path('service/', include('apps.services.urls', namespace='services')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
