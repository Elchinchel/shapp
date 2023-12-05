from django.urls import path

from shapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("groups", views.GroupListView.as_view(), name="groups"),
    path("students", views.StudentListView.as_view(), name="students"),
    path("subjects", views.SubjectListView.as_view(), name="subjects"),
]
