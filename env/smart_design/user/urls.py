from django.urls import path
from .views import  user_signup, user_login 
urlpatterns = [
    path('signup/', user_signup),
    path('signin/', user_login ),
]
