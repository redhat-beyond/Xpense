from django.urls import path

from house import views

app_name = 'house'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('global/', views.global_page, name='global_page'),
    path('login', views.house_login, name='house_login'),
    path('<int:house_id>/', views.house_view, name='house_view'),
    path('house_create/', views.house_create, name='house_create'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
