from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('rest_auth.urls')),
    url(r'^registrar/', include('rest_auth.registration.urls'))
]