
from django.contrib import admin
from django.urls import include, path
from django.conf import Settings


urlpatterns = [
    path('admin/', admin.site.urls),
     path('accounts/', include('allauth.urls')),
     path('', include('core.urls', namespace='core')),
]

# if Settings.DEBUG:
#     import debug_toolbar
#     urlpatterns+=[path('__debug__/',include(debug_toolbar.urls))]