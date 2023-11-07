from django.urls import path
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.index, name='dashboard'),
    path('dashboard/form', views.form, name='form'),
    path('dashboard/team', views.team, name='team'),
    path('dashboard/products', views.products, name='products'),
    path('dashboard/team-edit/<int:id>', views.team_edit, name='team_edit'),
    path('dashboard/team-delete/<int:id>', views.team_delete, name='team_delete'),
]