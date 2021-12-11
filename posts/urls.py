from django.urls import path
from .views import homeView
urlpatterns = [ 
    path('', homeView.as_view(), name = 'home'),
]