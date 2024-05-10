from django.urls import path
from .views import *

urlpatterns = [path("test", TestConnection().as_view())]
