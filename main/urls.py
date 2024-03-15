from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aloqa/', views.aloqa, name='aloqa'),
    path('avtoservis_haqida/', views.avtoservis_haqida, name='avtoservis_haqida'),
    path('xizmatlar/', views.xizmatlar, name='xizmatlar'),
    path('xodimlarimiz/', views.xodimlarimiz, name='xodimlarimiz'),
    path('blog/', views.blog, name='blog'),
]