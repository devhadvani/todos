from django.urls import path
from .views import TaskList, TaskDetails, TaskCreate, TaskUpdate, TaskDelete, CustomLogin, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetails.as_view(), name='task'),
    path('task-create',TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(), name='task-delete'),  

        url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),   
]