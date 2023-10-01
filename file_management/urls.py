from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('' ,views.file_list, name="file_list" ),
    path('latest_file/',views.latest_file_view, name="latest_file_view")

]