import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'murlikitas.settings')

import django
django.setup()

from euskal.models import User, UserProfile, UserPreferences, Choices


def populate():
    f = open('test_data.txt', 'r')
    for line in f:
        div = line.split(';')
        username = div[2]
        email = 'johndoe@test.com'
        password = '123'
        first_name = div[0]
        last_name = div[1]
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        up = UserProfile()
        up.user = user
        up.save()

        upref = UserPreferences(user_profile=up)
        upref.save()

        left_choices = Choices(user_preferences=upref)
        left_list = div[3].split(',')
        try:
            left_choices.first_choice = left_list[0]
        except IndexError:
            left_choices.first_choice = ''
        try:
            left_choices.second_choice = left_list[1]
        except IndexError:
            left_choices.second_choice
        try:
            left_choices.third_choice = left_list[2]
        except IndexError:
            left_choices.third_choice = ''
        left_choices.save()
        right_choices = Choices(user_preferences=upref)
        right_list = div[4].split(',')
        try:
            right_choices.first_choice = right_list[0]
        except IndexError:
            right_choices.first_choice = ''
        try:
            right_choices.second_choice = right_list[1]
        except IndexError:
            right_choices.second_choice = ''
        try:
            right_choices.third_choice = right_list[2]
        except IndexError:
            right_choices.third_choice = ''
        right_choices.save()

        upref.left_choices = left_choices
        upref.right_choices = right_choices
        upref.save()

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()