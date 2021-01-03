from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('apps.user.urls')),
    path('goods/', include('apps.goods.urls')),
    path('cart/', include('apps.cart.urls')),
    path('order/', include('apps.order.urls')),
    url(r'^(?P<path>.*)$', serve, {'document_root': settings.IMAGES_ROOT}),

]
