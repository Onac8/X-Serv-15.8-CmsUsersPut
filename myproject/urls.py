from django.conf.urls import include, url
from django.contrib import admin
from cms_users_put import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name="Pagina Principal"),
    url(r'^logout', views.logout, name="Pagina que desconecta al usuario"),
    url(r'^(.+)', views.resource, name="Devuelve la pagina asociada al recurso"),
]
