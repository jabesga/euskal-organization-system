from django.contrib import admin
from euskal.models import UserPreferences, Choices

# Register your models here.

admin.site.register(Choices)


class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'left_choices', 'right_choices')

admin.site.register(UserPreferences, UserPreferencesAdmin)