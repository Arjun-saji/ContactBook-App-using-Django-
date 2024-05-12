from . import views
from django.urls import path
app_name = "contactlist"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/",views.addcontact,name="addcontact"),
    path("edit/<int:contact_id>/",views.editcontact, name="editcontact"),
    path("delete/<int:contact_id>/",views.deleteconfirmation,name="deleteconfirmation"),
    ]
   