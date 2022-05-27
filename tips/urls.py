from django.urls import path

from tips import views

app_name = 'tips'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_tip/', views.add_tip, name='add_tip'),
    path('edit_tip/<int:tip_id>/', views.edit_tip, name='edit_tip'),
    path('category/<str:category>/', views.filter_tip_by_category, name='category'),
    path('filtered_by_date/<str:date>/', views.filter_tip_by_date, name='filtered_by_date'),
    path('read_more/<int:tip_id>/', views.read_more_view, name='read_more'),
    path('delete_tip/<int:tip_id>/', views.delete_tip, name='delete_tip'),
]
