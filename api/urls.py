from django.urls import path
from .views import *

urlpatterns = [

    path('myinfo/', MyInfoListCreate.as_view()),
    path('myinfo/<int:pk>/', MyInfoDetail.as_view()),

    path('skills/', SkillListCreate.as_view()),
    path('skills/<int:pk>/', SkillDetail.as_view()),

    path('projects/', ProjectListCreate.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view()),

    path('education/', EducationListCreate.as_view()),
    path('education/<int:pk>/', EducationDetail.as_view()),

    path('certifications/', CertificationListCreate.as_view()),
    path('certifications/<int:pk>/', CertificationDetail.as_view()),
]