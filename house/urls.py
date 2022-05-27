from django.urls import path
from house import views

app_name = 'house'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('global/', views.global_page, name='global_page'),
    path('house_create/', views.house_create, name='house_create'),
    path('house/', views.house_view, name='house_view'),
    path('house/add_expense/', views.add_expense, name='add_expense'),
    path('house/edit_expense/<int:id>/', views.edit_expense, name='edit_expense'),
    path('house/delete_expense/<int:id>/', views.delete_expense, name='delete_expense'),
    path('house/edit_house/', views.edit_house, name='edit_house'),
]
