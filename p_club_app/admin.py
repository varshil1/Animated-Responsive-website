from django.contrib import admin
from p_club_app.models import Events,Resources,Login,Timeline,About_us,Team,Home_about_us,Home_desc
# Register your models here.

admin.site.register(Events)
admin.site.register(Timeline)
admin.site.register(Resources)
# admin.site.register(Resources_indi)
admin.site.register(Login)
admin.site.register(About_us)
admin.site.register(Team)
admin.site.register(Home_about_us)
admin.site.register(Home_desc)