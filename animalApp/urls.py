from django.urls import path,include 
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('reports/',views.Pdf.as_view(),name='reports'),
    path('manager_reports/',views.Pdf_manager.as_view(),name='report_manager'),
    path('prescription_reports/',views.Pdf_prescription.as_view(),name='report_pre'),
    path('production_reports/',views.Pdf_production.as_view(),name='report_production'),
    path('ai_reports/',views.Pdf_ai.as_view(),name='report_ai'),
    path('vet_reports/',views.Pdf_vet.as_view(),name='report_vet'),
    path('vet-visit-reports/',views.Pdf_visit.as_view(),name='report_visit'),
    path('supplement_reports/',views.Pdf_supp.as_view(),name='report_supplement'),
    path('signup/',views.signup,name='sign-up'),
    path('accounts/',include('django.contrib.auth.urls')), 
    path('addmanager/',views.addmanager,name='add-manager'),
    path('addvetofficer/',views.addvetofficer,name='add-vet'),
    path('addmilkproduction/',views.addmilkproduction,name='add-production'),
    path('addanimal/',views.addanimal,name='add-animal'),
    path('addvisists/',views.addvetvisists,name='add-visists'),
    path('addsupplement/',views.addsupplement,name='add-supplement'),
    path('addai/',views.addai,name='add-ai'),
    path('addprescription/',views.addprescription,name='add-prescription'),

    #delete
    path('deletemanager/<str:pk>/',views.deletemanager,name='delete-manager'),
    path('deletevet/<str:pk>/',views.deletevet,name='delete-vet'),
    path('delete-vet-visit/<str:pk>/',views.delete_visit,name='delete-visit'),
    path('deletsupplement/<str:pk>/',views.deletesuppliment,name='delete-supplement'),
    path('deleteproduction/<str:pk>/',views.deleteproduction,name='delete-production'),
    path('deleteanimal/<str:pk>/',views.deleteanimal,name='delete-animal'),
    path('deleteai/<str:pk>/',views.deleteai,name='delete-ai'),
    path('deleteprescription/<str:pk>/',views.deleteprescription,name='delete-prescription'),
   
   #update
   path('updateai/<str:pk>/',views.updateai,name='update-ai'),
   path('updateanimal/<str:pk>/',views.updateanimal,name='update-animal'),
   path('updatesupplement/<str:pk>/',views.updatesupplement,name='update-supplement'),
   path('updatemanager/<str:pk>/',views.updatemanager,name='update-manager'),
   path('updatevet/<str:pk>/',views.updatevet,name='update-vet'),
   path('update-vet-visit/<str:pk>/',views.update_vet_visit,name='update-visit'),
   path('updateprescription/<str:pk>/',views.updateprescription,name='update-prescription'),
   path('updateproduction/<str:pk>/',views.updateproduction,name='update-production'),
   #update-prescription


   #list
   path('manager-ailist',views.ai_list,name='manager-ailist'),
   path('owner-ailist',views.ai_list_owner,name='owner-ailist'),
   path('manager-prescriptionlist',views.prescription_list,name='manager-prescriptionlist'),
   path('owner-prescriptionlist',views.prescription_list_owner,name='owner-prescriptionlist'),
   path('vetlist/',views.vetlist,name='vet-list'),
   path('vet-visists/',views.vet_visists_list,name='visit-list'),
   path('ailist/',views.ailist,name='ai-list'),
   path('prescriptionlist/',views.prescriptionlist,name='prescription-list'),
   path('managerlist/',views.managerlist,name='manager-list'),
   path('animallist/',views.animalslist,name='animal-list'),
   path('productionlist/',views.productionlist,name='production-list'),
   path('supplementlist/',views.supplimentlist,name='supplement-list'),

   #graphs
   path('production-graph/',views.production_graph,name='production-graph'),
   path('supplement-graph/',views.supplement_graph,name='supplement-graph'),
   #searching
   path('animal-search/',views.animal_view,name='animal-search')

]