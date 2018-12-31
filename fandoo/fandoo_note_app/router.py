from users.api.viewsets import ProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', ProfileViewSet, base_name='user')


for url in router.urls:
    print(url, '\n')