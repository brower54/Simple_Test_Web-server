from django.urls import path
from . import apiviews


urlpatterns = [
    path('classes/', apiviews.classes_view),
    path('teachers/', apiviews.teachers_view),
    path('teachers/<int:teacher_id>/', apiviews.teacher_detail_view),
]