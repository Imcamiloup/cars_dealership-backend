from django.urls import path , include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from BackOrder import views

#api router
router = routers.DefaultRouter()
router.register(r'car_dealer', views.carsWaitListView, 'car_dealer')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Cars Dealer API'))
]

