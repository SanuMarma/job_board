from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('list', views.EmployerViewset) # router er antena
router.register('job_list', views.JobViewset) # router er antena
router.register('industry', views.IndustryViewset) # router er antena
router.register('location', views.LocationViewset) # router er antena

urlpatterns = [
    path('', include(router.urls)),
]