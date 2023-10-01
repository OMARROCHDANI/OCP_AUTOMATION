from django.urls import path
from . import views
urlpatterns = [
    path('' ,views.firstFunction, name="firstFunction" ),
    path('run_script/', views.run_script, name='run_script'),
    path('progress_demo/', views.progress, name='progress'),
    path('run_script_json/', views.run_script_json, name='run_script_json'),
    path('run_script_csv/', views.run_script_csv, name='run_script_csv'),
   

]