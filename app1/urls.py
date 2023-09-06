from django.urls import path
from .views import detail,all_questions


urlpatterns = [
    path('all/',all_questions),
    path('detail/<int:question_id>',detail),
    
]