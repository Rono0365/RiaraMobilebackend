from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from noticeboard import views
from students import views1
from django.contrib.auth.models import User
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('id/', views1.PostListx.as_view()),
    path('id/<int:pk>/', views1.PostDetailx.as_view()),
    path('units/', views1.unitListx.as_view()),
    path('units/<int:pk>/', views1.unitDetailx.as_view()),
    #path('course/<int:pk>/', views1.courseDetailx.as_view()),
    path('course/', views1.courseListx.as_view()),
    #path('api-token-auth/',obtain_auth_token ),
    path('api-token-auth/', views.CustomAuthToken.as_view()),#CustomAuthToken.as_view()
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
    #path('id/', views.id.as_view()),#(?P<first_name>\w+)/(?P<last_name>\w+)
]#'',''
urlpatterns = format_suffix_patterns(urlpatterns)