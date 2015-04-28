from django.contrib import admin
from euskal.models import UserPreferences, Choices, Option, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'has_voted_group_name')


class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'left_choices', 'right_choices')


class OptionAdmin(admin.ModelAdmin):
    list_display = ('option_name', 'votes')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserPreferences, UserPreferencesAdmin)
admin.site.register(Choices)

admin.site.register(Option, OptionAdmin)
