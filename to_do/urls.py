from django.urls import path
from . import views

urlpatterns = [
    path('',views.ToDoListView.as_view(),name='to-do'),
    path('do-register/',views.DoRegisterView.as_view(), name='do-register'),
    path('<int:pk>/',views.DetailDoView.as_view(),name='detail-do'),
    path('<int:pk>/update',views.UpdateToDoView.as_view(),name='update-do'),
    path('<int:pk>/delete',views.DeleteToDoView.as_view(),name='delete-do'),
]
