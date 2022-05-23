from django.urls import path

from house import views

app_name = 'house'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('global/', views.global_page, name='global_page'),
    path('house_create/', views.house_create, name='house_create'),
    path('house/', views.house_view, name='house_view'),
]
