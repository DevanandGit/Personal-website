from django.urls import path
from .views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('Home/', index),
    # path('about/', about),
]
# urlpatterns += staticfiles_urlpatterns()


