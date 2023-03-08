from django.urls import path
from demo_app import views 

# urlpatterns = [
#     path('home/', views.home, name="home"),
# ] 

urlpatterns = [
    path('dishes/<str:dish>', views.menuitems),
]