from django.urls import path

from tips import views

app_name = 'tips'
urlpatterns = [
    path('', views.board, name='board'),
    path('add_tip/', views.add_tip, name='add_tip'),
    path('edit_tip/<int:tip_id>/', views.edit_tip, name='edit_tip'),
    path('delete_tip/<int:tip_id>/', views.delete_tip, name='delete_tip'),
]
