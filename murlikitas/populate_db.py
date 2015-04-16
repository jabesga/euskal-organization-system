import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'murlikitas.settings')

import django
django.setup()


from euskal.models import UserPreferences, User


def assign_choice(list, i):
    try:
        temp = list[i]
    except IndexError:
        temp = ""
    return temp


def populate():
    f = open('data.txt', 'r')
    for line in f:
        temp = line.split(';')
        leftlist = temp[0].split(',')
        name = temp[1]
        rightlist = temp[2].split(',')

        gen_email = name + '@' + name + '.' + name
        u = User.objects.create_user(name, gen_email, name)
        u.set_password(name)
        u.save()

        up = UserPreferences()
        up.user = u
        up.first_left_choice = assign_choice(leftlist, 0)
        up.second_left_choice = assign_choice(leftlist, 1)
        up.third_left_choice = assign_choice(leftlist, 2)
        up.first_right_choice = assign_choice(rightlist, 0)
        up. second_right_choice = assign_choice(rightlist, 1)
        up. third_right_choice = assign_choice(rightlist, 2)
        up.save()


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()