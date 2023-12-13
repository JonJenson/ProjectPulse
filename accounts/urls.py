from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView , PasswordChangeDoneView
from .views import CustomPasswordChangeView


urlpatterns=[
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register-customer/',views.register_customer,name='register-customer'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('change-password/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

]