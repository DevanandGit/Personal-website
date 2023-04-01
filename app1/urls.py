from django.urls import path
from .views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('index/', index)
]
urlpatterns += staticfiles_urlpatterns()


