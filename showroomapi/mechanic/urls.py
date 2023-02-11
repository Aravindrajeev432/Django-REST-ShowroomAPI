from django.urls import path
from .views import GetBays,BayJoin,MyCurrentJob,CompatibleParts,ServicePartsUpdator ,\
    ServiceMechanicCompleter,MakeBayFree
urlpatterns = [
path('getbays',GetBays.as_view()),
    path('join-bay/<int:pk>',BayJoin.as_view()),
    path('my-current-job',MyCurrentJob.as_view()),
    path('compatible-parts/<int:pk>', CompatibleParts.as_view()),
    #pk service's id
    path('services-part-update/<int:pk>',ServicePartsUpdator.as_view()),
    path('service-mech-finish/<int:pk>',ServiceMechanicCompleter.as_view()),
    path('make-bay-free/<int:pk>',MakeBayFree.as_view()),
]