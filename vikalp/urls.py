from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign/$', views.sign, name='sign'),
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^addCompany/$', views.add_company, name='add_company'),
    url(r'^(?P<branch_id>[0-9]+)/$', views.list, name='list'),
    url(r'^(?P<company_id>[0-9]+)/detail/$', views.detail, name='detail')
]
