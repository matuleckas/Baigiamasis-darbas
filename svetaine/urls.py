from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="Pagrindinis"),
  path("about/", views.about, name="Apie mus"),
  path("contact/", views.contact, name="Kontaktai")
]
