from django.urls import path

from house import views

app_name = 'house'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('global/', views.global_page, name='global_page'),
    path('login/', views.house_login, name='house_login'),
    path('<str:house_id>/', views.house_view, name='house_view'),
    path('house/add', views.add_house, name='add_house'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('<str:house_id>/edit_expense/<int:id>/', views.edit_expense, name='edit_expense'),
    path('<str:house_id>/delete_expense/<int:id>/', views.delete_expense, name='delete_expense'),
]
