from django.contrib import admin
from django.urls import path, include
from employee import views  # ✅ Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls')),  # routes to employee app
]
