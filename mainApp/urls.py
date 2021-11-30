from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('registeruser',views.UserRegistrationViewSets,basename='register-user')

urlpatterns = [
    path('', include(route.urls) ),
    path('get_allnews/',views.getAllNews),
    path('join/',views.registration_form),
    
    path('all_blog_posts/',views.getAllBlogpost),
    path('blogDetail/<int:blogID>/',views.getBlogDetail),

    path('login/',views.UserLogin.as_view(),name='login'),

]