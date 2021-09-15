from django.urls import path
from . import views

app_name= "Accounts"
urlpatterns = [
    path('signup/', views.signup, name= "signup"),
    path('create_profile/', views.create_profile, name= "create_profile"),
    path('show_profile/<int:pk>/', views.show_profile, name= "show_profile"),
    path('update_profile/<int:pk>/', views.update_profile, name= "update_profile"),
]
