from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import *
from .serializer import *

# Create your views here.
# @login_required(login_url='/accounts/login/')
def home(request):
    '''
    function that returns the index page
    '''
    project = Project.objects.all
    return render(request,'index.html',{'content': project})

@login_required(login_url='/accounts/login/')
def profile(request,iden):
    '''
    function to return the profile of users
    '''
    profile = Profile.get_profile(identity=iden)
    project = Project.get_project(identity=iden)
    return render(request,'profile.html',{'project':project,'profile':profile})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.by = current_user
            project.save()
        return redirect('home')

    else:
        form= NewProjectForm()

    return render(request, 'new_project.html', {'form':form})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'project' in request.GET and request.GET['project']:
        name = request.GET.get('project')
        project = Project.search(name)

        return render(request, 'search.html', {'title':name, 'content':project})

    else:
        return render(request,'search.html')

@login_required(login_url='/accounts/login/')
def project(request,id):
    '''
    function to return a single project
    '''
    project = Project.search(name=id)
    return render(request,'project.html',{'project': project})

@login_required(login_url='/accounts/login/')
def rate(request,id):
    current_user = request.user
    item = Project.single_project(id=id)
    project = get_object_or_404(Project, pk= id)
    if  request.method == 'POST':
        form = RatingForm(request.POST, request.FILES)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.rater = current_user
            rate.task = project
            rate.average = (rate.content + rate.design + rate.usability)/3
            rate.save()

        return redirect('home')

    else:
        form = RatingForm()

    return render(request,'rate.html',{'form':form,'project':item})

class ProfApi(APIView):
    def get (self, request, format=None):
        profile = Profile.objects.all()
        prof = Profileserializer(profile,many=True)

        return Response(prof.data)

class ProjApi(APIView):
    def get(self, request, format=None):
        project = Project.objects.all()
        proj = Projectserializer(project, many=True)

        return Response(proj.data)

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.name = current_user
            profile.save()
        return redirect('home')

    else:
        form= NewProfileForm()

    return render(request, 'new_profile.html', {'form':form})
