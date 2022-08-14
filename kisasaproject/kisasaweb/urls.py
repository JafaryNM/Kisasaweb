from django.urls import path
from .views import AboutPage, IndexTemplate, BaseTemplate, AboutPage,ContactUs, ServicesPage

urlpatterns = [
    path('' , IndexTemplate.as_view() , name='index_page'),
    path('About/', AboutPage.as_view(), name='about_page'),
    path('Contact/',ContactUs.as_view(), name='contact_page'),
    path('Services/', ServicesPage.as_view(), name='service_page')
    #path('', BaseTemplate.as_view() , name='basepage')
]
