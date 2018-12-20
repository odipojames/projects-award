from django.test import TestCase
from .models import *

# Create your tests here.

class RateTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1, username='k')
        self.task = Project.objects.create(by=self.user,
                                           title='k',
                                           description='l',
                                           link='m')
        self.rate = Rate.objects.create(rater=self.user,
                                        task=self.task,
                                        design='4',
                                        content='4',
                                        usability='4',
                                        average='4',
                                        review='k')

    def test_instance(self):
        self.assertTrue(isinstance(self.rate,Rate))

class ProjectTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1, username='k')
        self.task = Project.objects.create(id=1,
                                           by=self.user,
                                           title='k',
                                           description='l',
                                           link='m')

    def test_instance(self):
        self.assertTrue(isinstance(self.task,Project))

    def test_get_project(self):
        self.task.save()
        project = Project.get_project('k')
        self.assertTrue(len(project)>0)

    def test_search(self):
        self.task.save()
        project = Project.search('k')
        self.assertTrue(len(project)>0)

    def test_single_project(self):
        self.task.save()
        project = Project.single_project(1)
        self.assertTrue(len(project)>0)

class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1, username='k')
        self.task = Project.objects.create(id=1,
                                           by=self.user,
                                           title='k',
                                           description='l',
                                           link='m')
        self.profile = Profile.objects.create(name=self.user,
                                              bio='m',
                                              projects=self.task,
                                              contact='m')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile('k')
        self.assertTrue(len(profile)>0)
