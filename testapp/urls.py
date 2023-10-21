from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('registration',views.registration,name='registration'),
    path('login',views.emp_login,name='login'),
    path('emp_home',views.emp_home,name='emp_home'),
    path('profile',views.profile,name='profile'),
    path('logout',views.Logout,name='logout'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('my_experience',views.my_experience,name='my_experience'),
    path('edit_experience',views.edit_experience,name='edit_experience'),
    path('my_education',views.my_education,name='my_education'),
    path('edit_myeducation',views.edit_myeducation,name='edit_myeducation'),
    path('change_password',views.change_password,name='change_password'),
    path('change_passwordadmin',views.change_passwordadmin,name='change_passwordadmin'),
    path('all_employee',views.all_employee,name='all_employee'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('edit_education/<int:pid>',views.edit_education,name='edit_education'),
    path('delete_employee/<int:pid>',views.delete_employee,name='delete_employee'),
]
