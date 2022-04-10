from django.urls import path

from . import views

app_name = 'markets'

urlpatterns = [
    path('', views.index, name='index'),
    path('markets/<str:name>/', views.market, name='market'),
]
