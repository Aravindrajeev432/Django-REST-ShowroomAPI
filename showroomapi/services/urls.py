from django.urls import path
from .views import AllServices,AddServiceInfo,GetUniCarNum,ShowServiceinfo,\
    GetDistinctUniCarNum,RequestService,Service,ServiceAssignAdvisor , GetFreeBays,\
    billgenerator,ServiceCompleter
urlpatterns = [
path('getunicarnum',GetUniCarNum.as_view()),
    path('addserviceinfo', AddServiceInfo.as_view()),
    path('showserivceinfo',ShowServiceinfo.as_view()),
    path('getdistinctunicarnum',GetDistinctUniCarNum.as_view()),
    path('requestservice',RequestService.as_view()),
    path('services/<str:service_status>', Service.as_view()),
    path('service-assign-advisor/<int:id>',ServiceAssignAdvisor.as_view()),
    path('getfreebays',GetFreeBays.as_view()),
    path('billgenerator/<int:id>',billgenerator),
    path('servicecompleter',ServiceCompleter.as_view())
]