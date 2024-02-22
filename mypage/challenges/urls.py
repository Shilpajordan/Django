from django.urls import path
from . import views # from the same folder 
# here we create the urls we want to support in the website

urlpatterns = [
    #path("january", views.january), # we are telling django, if a request reaches /january then execute the views.index function
    #path("february", views.february),
    #path("march", views.march),
    path("", views.index, name="index"), #this will trigger  /challenges/
    path("<int:month>", views.my_page_challenge_by_number),
    path("<str:month>", views.my_page, name="month-challenge"), # dynamic path placeholder <month>
]