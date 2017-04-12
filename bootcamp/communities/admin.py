from django.contrib import admin
from bootcamp.communities.models import  Community ,User


admin.site.register(User)
# Register your models here.
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('pk','name','parent','description')

admin.site.register(Community , CommunityAdmin)
