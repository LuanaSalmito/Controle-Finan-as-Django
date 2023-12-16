
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastro, name='cadastrar'),
    path('entrar/', views.entrar, name='entrar'),
    path('login/', views.usuario_login, name='login'),
    path('logout/', views.usuario_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

]








