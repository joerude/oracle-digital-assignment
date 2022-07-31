from django.urls import path, include

from .views import (
    StudentListView,
    AddStudent,
    SearchResultListView,
    EditStudent,
    DeleteStudent
)

urlpatterns = [
    path("", StudentListView.as_view(), name="index"),
    path("search/", SearchResultListView.as_view(), name="search_results"),
    path("add_student/", AddStudent.as_view(), name="add_student"),
    path("edit_student/<uuid:pk>/", EditStudent.as_view(), name="edit_student"),
    path("delete_student/<uuid:pk>/", DeleteStudent.as_view(), name="delete_student"),
]
