from django.contrib import admin
from django.urls import path, include
from rs_tool.views import CreateDoc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CreateDoc.as_view(), name='index'),
    path('api/', include('rs_tool.urls'))
]
