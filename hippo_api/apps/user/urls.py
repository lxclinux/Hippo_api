from django.urls import re_path
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'login/', obtain_jwt_token),
]

