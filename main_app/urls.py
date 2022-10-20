from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/', views.api, name='api'),

    path('foods/', views.foods_index, name='foods_index'),
    path('foods/<int:food_id>/', views.foods_detail, name='foods_detail'),
    path('foods/create/', views.FoodsCreate.as_view(), name='foods_create'),
    path('foods/<int:pk>/update/', views.FoodsUpdate.as_view(), name='foods_update'),
    path('foods/<int:pk>/delete/', views.FoodsDelete.as_view(), name='foods_delete'),

    path('accounts/signup/', views.signup, name='signup'),

]