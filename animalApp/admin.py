#admin
from django.contrib import admin
from .models import user,farm_owner,manager,animal_types,milk_production,suppliment,vet_visists,vet_visist_prescription,AI_services,farm_vertinary_officer

# Register your models here.
admin.site.register(user)
admin.site.register(farm_owner)
admin.site.register(manager)
admin.site.register(farm_vertinary_officer)
admin.site.register(animal_types)
admin.site.register(milk_production)
admin.site.register(suppliment)
admin.site.register(vet_visists)
admin.site.register(vet_visist_prescription)
admin.site.register(AI_services)