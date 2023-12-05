from typing import Any
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render

from shapp.models import Group, Student, Subject


class GroupListView(generic.ListView):
    model = Group
    queryset = Group.objects.all()
    template_name = 'group_list.html'


class StudentListView(generic.ListView):
    model = Student
    queryset = Student.objects.all()
    template_name = 'student_list.html'


class SubjectListView(generic.ListView):
    model = Subject
    queryset = Subject.objects.all()
    template_name = 'subject_list.html'


def index(request):
    data = {
        'group_count': Group.objects.count(),
        'student_count': Student.objects.count(),
        'subject_count': Subject.objects.count(),
    }
    return render(request, 'index.html', context=data)
