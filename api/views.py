from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# My Info
class MyInfoListCreate(generics.ListCreateAPIView):
    queryset = MyInfo.objects.all()
    serializer_class = MyInfoSerializer

class MyInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyInfo.objects.all()
    serializer_class = MyInfoSerializer


# Skills
class SkillListCreate(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


# Projects
class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# Education
class EducationListCreate(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EducationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


# Certifications
class CertificationListCreate(generics.ListCreateAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class CertificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer