from django.urls import path
from editable.views import MyView, MyEdit
from . import views


urlpatterns = [
	path('',views.home, name='home'),
	path('test/',MyView.as_view(), name='test'),
	path('edit/',MyEdit.as_view(), name='test'),
]
