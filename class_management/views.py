from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import SignUpForm, SignInForm
from .models import Student


class StudentListView(ListView):
    template_name = "student_list.html"
    model = Student
    paginate_by = 3


class SearchResultListView(ListView):
    model = Student
    template_name = "class_management/search_results.html"
    form_class = SignInForm
    context_object_name = "student_list"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Student.objects.filter(
            Q(full_name__icontains=query) | Q(email__icontains=query)
        )


class AddStudent(CreateView):
    template_name = "class_management/add_student.html"
    model = Student
    fields = "__all__"
    success_url = reverse_lazy("index")


class EditStudent(UpdateView):
    model = Student
    # form_class = AddStudentForm
    # fields = ['full_name', 'email', 'birth_date', 'classroom', 'gender']
    fields = ['full_name', 'email', 'birth_date', 'class_name', 'gender']
    template_name = 'class_management/edit_student.html'
    success_url = reverse_lazy("index")


class DeleteStudent(DeleteView):
    model = Student
    template_name = 'class_management/delete_student.html'
    success_url = reverse_lazy('index')
