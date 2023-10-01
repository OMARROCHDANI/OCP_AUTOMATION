from django.urls import path,include
from . import views
urlpatterns = [
    path('' ,views.home, name='home' ),
    path('signup/' ,views.signup, name='signup' ),
    path('signin/' ,views.signin, name='signin' ),
    path('signout/' ,views.signout, name='signout ' ),
    path('authenticationindex2/', views.authenticationindex2, name='authenticationindex2'),
]