
from rest_framework import routers
from .views import ArticleViewSets

router = routers.SimpleRouter()
router.register(r'article', ArticleViewSets)

urlpatterns = router.urls


from django.conf.urls import url
from .views import getConfig
urlpatterns = urlpatterns+[
    url(r'^getConfig', getConfig, name='getConfig'),
]