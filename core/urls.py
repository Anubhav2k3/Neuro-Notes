from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),

    path('notes/', views.notes_list, name='notes_list'),
    path('notes/create/', views.note_create, name='note_create'),
    path('notes/edit/<int:pk>/', views.note_edit, name='note_edit'),
    path('notes/delete/<int:pk>/', views.note_delete, name='note_delete'),
    path('notes/ai/<int:pk>/', views.note_ai_tools, name='note_ai_tools'),
    
]
