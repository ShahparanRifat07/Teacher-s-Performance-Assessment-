from django.urls import path
from .views import add_student, add_teacher, add_administrator, signin, dashboard

urlpatterns = [
    path('my/', dashboard, name='dashboard'),
    path('login/', signin, name='signin'),
    path('add_student/', add_student, name='add-student'),
    path('add_teacher/', add_teacher, name='add-teacher'),
    path('add_administrator/', add_administrator, name="add-administrator"),
]
