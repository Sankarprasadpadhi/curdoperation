from django.contrib import admin
from django.urls import path
from StudentRegisration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('show/', views.show, name="show"),
    path('add/', views.add_student, name="add"),
    path('edit/<int:id>', views.edit_student, name="edit"),
    path('delete/<int:id>', views.delete_student, name="delete"),
]
