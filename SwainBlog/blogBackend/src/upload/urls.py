
from django.conf.urls import url
from .views import imageUpload
urlpatterns = [
    url(r'^imageUpload', imageUpload, name='imageUpload'),
]