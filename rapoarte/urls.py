from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('rapoarte/', views.rapoarte_page, name='rapoarte'),
    path('contracte/', views.contracte_page, name='contracte'),
]