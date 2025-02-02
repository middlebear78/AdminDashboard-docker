from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import VacationViewSet, CountryViewSet, LikeViewSet, VacationStatistics, LikesStatistics

router = DefaultRouter()
router.register(r'vacations', VacationViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = router.urls + [
    path('statistics/vacations/', VacationStatistics.as_view(),
         name="vacation-statistics"),
    path('statistics/likes/', LikesStatistics.as_view(), name="like statistics")
]
