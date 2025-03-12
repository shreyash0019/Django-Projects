from django.urls import path
from core import views


urlpatterns = [
 path('get-transactions/',views.get_transaction),  

]