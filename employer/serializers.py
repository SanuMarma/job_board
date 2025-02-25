from rest_framework import serializers
from . import models

class EmployerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Employer
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    employer = serializers.StringRelatedField(many=False)
    industry = serializers.StringRelatedField(many=False)
    location = serializers.StringRelatedField(many=False)
    job_type = serializers.StringRelatedField(many=False)
    job_level = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = models.Job
        fields = '__all__'

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Industry
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'
        
        
