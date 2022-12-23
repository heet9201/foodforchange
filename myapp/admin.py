from django.contrib import admin

# from dim_prjt.myapp.views import sessions
from .models import profile,vsession

admin.site.register(profile)
admin.site.register(vsession)
