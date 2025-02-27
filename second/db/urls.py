from django.urls import path
from .views import employee_delete,employee_form,employee_list


urlpatterns = [
    path('',employee_form,name='employee_insert'),
    path('<int:id>/',employee_form,name='employee_update'),
    path('delete/<int:id>/',employee_delete,name='employee_delete'),
    path('list/',employee_list,name='employee_list'),
    
   
]
