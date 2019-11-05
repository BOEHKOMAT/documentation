from django.contrib import admin
from .models import Medicine, User, Order


admin.site.register(Medicine)
admin.site.register(User)
admin.site.register(Order)
