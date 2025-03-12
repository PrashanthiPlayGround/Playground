from django.urls import path
from .views import creature_ranking

urlpatterns = [
    path('', creature_ranking, name='creature_ranking'),
]
