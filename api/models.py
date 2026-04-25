
# Create your models here.
from django.db import models

# 1. My Information
class MyInfo(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    information = models.TextField()
    email = models.EmailField()
    location = models.CharField(max_length=100)

    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    x = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# 2. Technical Skills
class Skill(models.Model):
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name


# 3. Projects
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_interface = models.ImageField(upload_to='projects/')
    about_project = models.TextField()
    key_features = models.TextField()
    used_technologies = models.TextField()

    def __str__(self):
        return self.project_name


# 4. Education
class Education(models.Model):
    college_name = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    about = models.TextField()
    gpa = models.FloatField()
    college_image = models.ImageField(upload_to='education/')

    def __str__(self):
        return self.college_name


# 5. Certifications
class Certification(models.Model):
    name = models.CharField(max_length=200)
    certification_image = models.ImageField(upload_to='certifications/')
    about = models.TextField()

    def __str__(self):
        return self.name

class MyPhoto(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='myphotos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else "Photo"