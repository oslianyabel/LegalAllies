from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),  # type: ignore
    path("profile/", views.profile, name="profile"),  # type: ignore
    path("category/<slug:slug>/", views.category_articles, name="category_articles"),  # type: ignore
    path("<slug:slug>/", views.article_detail, name="article_detail"),  # type: ignore
    # Auth
    path("accounts/register/", views.register, name="register"),  # type: ignore
    path("accounts/login/", views.login_view, name="login"),  # type: ignore
    path("accounts/logout/", views.logout_view, name="logout"),  # type: ignore
    path("accounts/change-password/", views.change_password, name="change_password"),  # type: ignore
]
