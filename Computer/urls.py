from django.urls import path

from Computer.views import ComputerCreateListView, RetriaveDeleteView

urlpatterns = [
  path('', ComputerCreateListView.as_view(), name='country_create_list'),
  path('<int:pk>/', RetriaveDeleteView.as_view(), name='computer_retriave_delete')
]