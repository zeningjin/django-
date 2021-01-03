from django.urls import path
from apps.user.views import *

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('perCen/<int:user_id>/', perCen, name='perCen'),
    path('addr_default/', addr_default, name='addr_default'),
    path('sending/sms/', sending_sms),
    path('sending/sms1/', sending_sms1),
path('register1/', register1, name='register1'),
]
