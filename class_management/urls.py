from django.contrib.auth.views import LogoutView
from django.urls import path, include

from config import settings
from .views import (
    StudentListView,
    SignInUser,
    SignUpUser,
    AddStudent,
    SearchResultListView,
    EditStudent,
    DeleteStudent
)

urlpatterns = [
    path("", StudentListView.as_view(), name="index"),
    path("signup/", SignUpUser.as_view(), name="signup"),
    path("signin/", SignInUser.as_view(), name="signin"),
    path(
        "signout/",
        LogoutView.as_view(),
        {"next_page": settings.LOGOUT_REDIRECT_URL},
        name="signout",
    ),
    path("search/", SearchResultListView.as_view(), name="search_results"),

    path("add_student/", AddStudent.as_view(), name="add_student"),
    path("edit_student/<uuid:pk>/", EditStudent.as_view(), name="edit_student"),
    path("delete_student/<uuid:pk>/", DeleteStudent.as_view(), name="delete_student"),
]
