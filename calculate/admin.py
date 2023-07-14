from django.contrib import admin
from . models import User, Income, Expanse
# Register your models here.
admin.site.register(User)
admin.site.register(Income)
admin.site.register(Expanse)