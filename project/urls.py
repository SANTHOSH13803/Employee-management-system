
from django.urls import path
from project import views

urlpatterns = [
    path('',views.home,name='home' ),
    path('create',views.create,name='create' ),
    path('edit/<int:id>',views.edit,name='edit' ),
    path('employee-view/<int:id>',views.employee_view ,name='employee_view'),
    path('employeelist',views.employee,name='employeelist' )
]
