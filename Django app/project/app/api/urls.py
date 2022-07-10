from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # login-logout url routes
    path('login/', obtain_auth_token, name = 'login'),
    path('register/', views.registration_view, name = 'register'),
    path('logout/', views.logout_view, name = 'logout'),
    
    # app related urls
    path('projectlist/', views.ProjectList.as_view(), name='projectlist'),
    path('projectlist/<int:pk>', views.singleproject.as_view(), name='projectdetail'),
    path('projectlist/<int:pk>/task-create', views.TaskCreate.as_view(), name='taskcreate'),
    path('projectlist/tasklist', views.alltasks.as_view(), name = 'tasklist'),
    path('projectlist/<int:pk>/tasks', views.ProjectSpecificTasks.as_view(), name = 'projecttasks')

]