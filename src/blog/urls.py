from django.urls import path
from .views import (
    my_fbv,
    CourseView,
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
)

app_name='courses'
urlpatterns = [
    path('',CourseListView.as_view(),name='course-list'),
    path('create/',CourseCreateView.as_view(),name='course-create'),
    path('<int:id>/update/',CourseUpdateView.as_view(),name='course-upate'),
    path('<int:id>/delete/',CourseDeleteView.as_view(),name='course-delete'),
    # path('',CourseView.as_view(),name='course-list'),
    path('<int:id>/',CourseView.as_view(),name='course-detail')
]