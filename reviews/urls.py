from django.urls import path
from . import views


app_name = "reviews"

urlpatterns = [
  path("create/<int:pk>", views.create_review, name="create"),
  path("delete/<int:pk>", views.DeleteReview.as_view(), name="delete"),
  ]