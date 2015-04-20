from django.contrib import admin
from euskal.models import UserPreferences, Choices, Option, UserProfile

# Register your models here.

admin.site.register(Choices)


class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'left_choices', 'right_choices')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'has_voted_group_name')


class OptionAdmin(admin.ModelAdmin):
    list_display = ('option_name', 'votes')

admin.site.register(UserPreferences, UserPreferencesAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(UserProfile, UserProfileAdmin)