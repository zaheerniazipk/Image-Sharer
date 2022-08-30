from django.urls import path
from .views import HomePageView, PostDetailView


# create a namespace
app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    # here pk is primary key will be assigned automagically
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
]
