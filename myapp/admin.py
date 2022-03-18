from django.contrib import admin
from .models import *

# Register your models here.
class detUsers(admin.ModelAdmin):
    list_display = ('id','name','email','phone','active')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10 

admin.site.register(Users,detUsers)
admin.site.register(Category)
admin.site.register(Signature)
admin.site.register(Movies)
admin.site.register(Favorite)
