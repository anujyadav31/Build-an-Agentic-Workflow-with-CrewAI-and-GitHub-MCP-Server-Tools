
from django.urls import path
from . import views


# Task 4: Add the URL of the documentation_interface view
#------------- me -----------------
path('', views.documentation_interface, name='documentation_interface'),
#------------- me -----------------
# Task 11: Add the URL of the generate_documentation view
urlpatterns = [

]
#------- me ----------
urlpatterns = [
    path('generate/', views.generate_documentation, name='generate_documentation'),
]
#------- me ----------   
