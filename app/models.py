from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Rate(models.Model):
    Rating_choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    rater = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey('app.Project',on_delete=models.CASCADE,related_name='rates')
    design = models.PositiveIntegerField(choices=Rating_choices, default=0,validators=[MaxValueValidator(10), MinValueValidator(0)])
    usability = models.PositiveIntegerField(choices=Rating_choices, default=0,validators=[MaxValueValidator(10), MinValueValidator(0)])
    content = models.PositiveIntegerField(choices=Rating_choices, default=0,validators=[MaxValueValidator(10), MinValueValidator(0)])
    average = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10), MinValueValidator(0)])
    review = models.TextField(blank = True, null=True)

    def __str__(self):
        return self.rater.username


class Project(models.Model):
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 60)
    homepage = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    link = models.CharField(max_length = 60)
    rating = models.ForeignKey(Rate, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    @classmethod
    def get_project(cls,identity):
        project = Project.objects.filter(by__username__icontains = identity)
        return project

    @classmethod
    def search(cls,name):
        project = cls.objects.filter(title__icontains = name)
        return project

    @classmethod
    def single_project(cls,id):
        project = Project.objects.filter(id =id)
        return project


class Profile(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE )
    profile_pic = models.ImageField(upload_to = 'images/')
    bio = models. TextField()
    projects = models.ForeignKey(Project, on_delete=models.CASCADE,null = True,blank=True)
    contact = models.TextField()

    def __str__(self):
        return self.name.username

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls,identity):
        profile = Profile.objects.filter(name__username__icontains = identity)
        return profile
