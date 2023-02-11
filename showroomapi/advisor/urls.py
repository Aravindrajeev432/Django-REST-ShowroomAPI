from django.urls import path
from .views import MakeOnline,AvailableAdvisors,CurrentJobs,JobAssignerToBay,\
    AdvisorDashboard
urlpatterns = [
    path('makeonline/<int:advisor>',MakeOnline.as_view()),
    path('available',AvailableAdvisors.as_view()),
    path('current-jobs/<int:advisor_id>',CurrentJobs.as_view()),
    path('assign-job-to-bay',JobAssignerToBay.as_view()),
    path('dashboard-data',AdvisorDashboard.as_view())

    ]