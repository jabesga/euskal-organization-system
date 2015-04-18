import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'murlikitas.settings')

import django
django.setup()

from euskal.models import User, UserProfile


def assign_choice(list, i):
    try:
        temp = list[i]
    except IndexError:
        temp = ""
    return temp


def populate():

    username = 'test'
    email = 'test@test'
    password = 'test'
    first_name = 'testn'
    last_name = 'testa'
    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    up = UserProfile()
    up.user = user
    up.save()
    # f = open('test_data.txt', 'r')

    # for line in f:
    #     temp = line.split(';')
    #     left_list = temp[0].split(',')
    #     name = temp[1]
    #     right_list = temp[2].split(',')
    #
    #     gen_email = name + '@' + name + '.' + name



        #
        # up = UserPreferences()
        # up.user = u
        # up.first_left_choice = assign_choice(leftlist, 0)
        # up.second_left_choice = assign_choice(leftlist, 1)
        # up.third_left_choice = assign_choice(leftlist, 2)
        # up.first_right_choice = assign_choice(rightlist, 0)
        # up. second_right_choice = assign_choice(rightlist, 1)
        # up. third_right_choice = assign_choice(rightlist, 2)
        # up.save()


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()