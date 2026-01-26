# from django.urls import path
# from . import views
# from
# urlpatterns = [
#     path('', views.home, name='home'),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import call_rest_api

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('list/', views.student_list, name='student_list'),
    path('detail/<int:pk>/', views.student_detail, name='student_detail'),
    path('api_call/', views.call_rest_api, name='api_call'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
