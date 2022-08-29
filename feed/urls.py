from django.urls import path
from .views import HomePageView


# create a namespace
app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]
