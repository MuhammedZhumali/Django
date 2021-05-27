from django.urls import path, include
from . import views
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
router.register('language', views.LanguageView)
router.register('paradigm', views.ParadigmView)
router.register('programmer', views.ProgrammerView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]