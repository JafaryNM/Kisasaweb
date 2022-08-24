from django.urls import path
from .views import *
urlpatterns = [
    path('' , IndexTemplate.as_view() , name='index_page'),
    path('About/', AboutPage.as_view(), name='about_page'),
    path('Contact/',ContactUs.as_view(), name='contact_page'),
    path('Services/', ServicesPage.as_view(), name='service_page'),
    path('Masanja/', SingleProfile.as_view(), name='masanjaprofile'),
    path('Nkunda/', SingleProfileNkunda.as_view(), name='nkundaprofile'),
    path('Organization/',OrganizationTemplate.as_view(), name='organization_page'),
    path('Vision/', VisionMissionTemplate.as_view(), name='vision_page')
    #path('', BaseTemplate.as_view() , name='basepage')

]
