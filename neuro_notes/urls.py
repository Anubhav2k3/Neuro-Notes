from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls')),
    path('', include('core.urls')),       # Core app routes
    path('theme/', include('theme1.urls'))  # Tailwind test/preview routes
]
