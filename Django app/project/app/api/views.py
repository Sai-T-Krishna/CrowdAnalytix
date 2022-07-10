# import all required modules, packages
from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from app.models import Project, Tasks
from .serializers import ProjectSerializer, TaskSerializer, RegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from . import pagination
from .permissions import AdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

####################### Token Based Authentication #######################

# Logout view
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        
        data = request.data
        data ={}
        data['response'] = 'Logout successful!'
        request.user.auth_token.delete()
        return Response(data, status=status.HTTP_200_OK)

# Registration view
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Registration successful!'
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user = account).key
            data['token'] = token

        else:
            data = serializer.errors
        
        return Response(data)

###################### Project related views ###########################      
# get the list of projects
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','start_date','end_date']
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication,TokenAuthentication]
    pagination_class = pagination.ProjectListPagination

# get the single project details
class singleproject(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AdminOrReadOnly, IsAuthenticated]
    authentication_classes = [BasicAuthentication,TokenAuthentication]

# get the list of all tasks
class alltasks(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication,TokenAuthentication]


class ProjectSpecificTasks(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Tasks.objects.all() 
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication,TokenAuthentication]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Tasks.objects.filter(pk=pk)

# view for creating a task
class TaskCreate(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication,TokenAuthentication]

    def get_queryset(self):
        return Tasks.objects.all()

   
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        project = Project.objects.get(pk=pk)
        review_queryset = Tasks.objects.filter(project = project)

        serializer.save(project=project)
    
