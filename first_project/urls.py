"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ocp_scrape/', include('ocp_scrape.urls')),
    path('celery-progress/', include('celery_progress.urls')),
    path('authentication/', include('authentication.urls')),
    path('file_management/', include('file_management.urls')),

    


    #we want to delegate any path or url to url.py module in product app
    #/package
    # we add to original import include
    # to reference the product urls (without.py)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
