from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^users$',views.index),
    url(r'^users/new$', views.new),
    url(r'^users/create', views.create),
    url(r'^users/(?P<user_id>\d+)$', views.show),
    url(r'^users/(?P<user_id>\d+)/edit$',views.edit),
    url(r'^users/(?P<user_id>\d+)/update$', views.update),
    url(r'^users/(?P<user_id>\d+)/destroy$',views.destroy)
    ]

    # url(r'^users/(?P<id>)\d+)/edit', views.edit),
    # url(r'^users/(?P<id>)\d+)', views.show),
     # url(r'^users/(?P<id>)\d+)/destroy', views.destroy),
    # url(r'^users/update$', views.update)

#1. homepage
# 2. template to make new user
# 3. template to edit user
# 4. template to show user
# 5. process to create new user
# 6. process to destroy a user
# 7. process to update a user