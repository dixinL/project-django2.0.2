from django.urls import path
from . import register, index, user_info, log

urlpatterns = [
    path('login/', log.login_view,name='login'),
    path('logout/', log.logout_view, name='logout'),
    path('', index.index_view, name='index'),
    path('register/', register.register_view, name='register'),
    # path('detailed/', ),
    path('user-info/', user_info.user_info_view, name='user_info'),
]