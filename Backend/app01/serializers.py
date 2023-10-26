from rest_framework import serializers
from app01.models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"