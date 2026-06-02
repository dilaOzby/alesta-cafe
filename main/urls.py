from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),

    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('menu/', views.menu, name='menu'),
    path('davet/', views.davet, name='davet'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('rezervasyon/', views.rezervasyon, name='rezervasyon'),
]