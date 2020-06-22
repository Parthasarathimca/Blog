from django.urls import path
from django.conf.urls import url, include
from blog import views




urlpatterns = [
    url(r'^login/$',views.user_login,name="user_login"),
    url(r'^logout/$',views.user_logout,name="user_logout"),
    url(r'^blogs/$',views.blogs,name="view_blogs"),
    url(r'^likes/$',views.likes,name="add_likes"),

]   