"""定义learning_logs的URL模式"""

# from django.urls import path

from django.conf.urls import url

from . import views

app_name = 'learning_log'

urlpatterns = [
	# 主页
	url(r'^$', views.index, name='index'),
]