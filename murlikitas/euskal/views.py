from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from euskal.forms import UserForm, PreferencesForm
from euskal.models import UserPreferences
from euskal.orgascript import Member


def index(request):
    return render(request, 'euskal/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_prefs = UserPreferences()
            user_prefs.user = user
            user_prefs.save()


            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render(request, 'euskal/register.html', {'user_form': user_form, 'registered': registered})


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('/euskal/preferences')
            else:
                return render(request, 'euskal/login.html', {'invalid': 'Account disabled'})
        else:
            print "Invalid login details: {0} {1}".format(username, password)
            return render(request, 'euskal/login.html', {'invalid': 'Invalid login details supplied'})
    else:
        return render(request, 'euskal/login.html')


@login_required
def preferences(request):
    if request.method == 'POST':
        preferences_form = PreferencesForm(data=request.POST)
        if preferences_form.is_valid():
            # BOOOOOOOOOOOOOOOOM
            try:
                UserPreferences.objects.get(user=request.user).delete()
            except UserPreferences.DoesNotExist:
                pass
            pref = preferences_form.save(commit=False)
            pref.user = request.user
            pref.save()

            return render(request, 'euskal/preferences.html', {'preferences_form': preferences_form,
                                                        'saved': 'Preferences saved',})
        else:
            print preferences_form.errors
    else:
        preferences_form = PreferencesForm()

    return render(request, 'euskal/preferences.html', {'preferences_form': preferences_form})

@login_required
def auth_logout(request):
    logout(request)
    return redirect('/euskal/')

def status(request):
    list = []

    for u in UserPreferences.objects.all():
        name = u.user.username
        leftlist = [str(u.first_left_choice), str(u.second_left_choice), str(u.third_left_choice)]
        rightlist = [str(u.first_right_choice), str(u.second_right_choice), str(u.third_right_choice)]
        m = Member(name, leftlist, rightlist)
        list.append(m)

    print list
    for i in range(3):
        for member in list:
            copy = list[:]
            member.check_left_preference(copy, i) # first round = 0

        for member in list:
            copy = list[:]
            member.check_right_preference(copy, i) # first round = 0

    print "========================"
    for member in list:
        member.print_locked()

    return render(request, 'euskal/status.html', {'list':list})