from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^validate_username/$', views.validate_username, name='validate_username'),
]
