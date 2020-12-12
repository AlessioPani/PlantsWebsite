from django.urls import path
from .views import about, homepage, IndexView


urlpatterns = [
    path('', homepage, name="homepage"),
    path('about/', about, name="about"),
    path('index/', IndexView.as_view(), name='index')
]
