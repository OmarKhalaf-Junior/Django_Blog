from django.urls import path
from . import views

urlpatterns = [
    path('add_category/', views.add_category, name= "add_category"),
    path('add_article/', views.add_post, name= "add_article"),
    path('', views.index, name= "HomePage"),      ## Opened First
    path('<slug:detail_slug>/', views.details, name= "details"),     ## Opened Second
    path('category/<slug:category_slug>/', views.category, name= "category"),      # Opened Third
    path('delete/<slug:delete_slug>/', views.delete_post, name= "delete"),
    path('update/<slug:update_slug>/', views.update_post, name= "update"),
]
