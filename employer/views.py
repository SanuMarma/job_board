from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
class IndustryViewset(viewsets.ModelViewSet):
    queryset = models.Industry.objects.all()
    serializer_class = serializers.IndustrySerializer
    permission_classes = [IsAdminUser|ReadOnly]
    
class LocationViewset(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = [IsAdminUser|ReadOnly]
    

class JobPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class JobForSpecificEmployer(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        employer_id = request.query_params.get("employer")
        if employer_id:
            return queryset.filter(employer__id=employer_id)
        return queryset
    

# class JobForSpecificEmployer(filters.BaseFilterBackend):
#     def filter_queryset(self, request, queryset, view):
#         employer_id = request.query_params.get('employer', None)
#         if employer_id is not None:
#             queryset = queryset.filter(employer__id=employer_id)
#         return queryset



class JobViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer
    filter_backends = [JobForSpecificEmployer]
    pagination_class = JobPagination


class EmployerViewset(viewsets.ModelViewSet):
    queryset = models.Employer.objects.all()
    serializer_class = serializers.EmployerSerializer
    permission_classes = [IsAdminUser|ReadOnly]
    
 