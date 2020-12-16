from django.contrib import admin
from django.urls import include, path
from froala_editor import views

urlpatterns = [
    path('', include('sample_app.urls')),
    path('admin/', admin.site.urls),
    path('froala_editor/', include('froala_editor.urls'))
]
