from django.urls import path
from . import views
urlpatterns = [
    path('MatricQuestion/', views.QuizforMatricViewSet.as_view(), name='Matric Question'),
    path('InterQuestion/', views.QuizforInterViewSet.as_view(), name='Inter Question'),

]
