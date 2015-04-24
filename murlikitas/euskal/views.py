from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from euskal.forms import UserForm, ChoicesForm, OptionsForm, NewOptionForm
from euskal.models import UserProfile, UserPreferences, Option

from euskal.algorithm import Person, run_algorithm


def index(request):
    if request.user.is_authenticated():
        up = UserProfile.objects.get(user=request.user)  # Get the UserProfile using the User.
        return render(request, 'euskal/dashboard.html', {'up': up})
    else:
        return render(request, 'euskal/index.html')


def auth_register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            upf = UserProfile()
            upf.user = user
            upf.save()

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
                return redirect('dashboard')
            else:
                return render(request, 'euskal/login.html', {'invalid': 'Cuenta deshabilitada'})
        else:
            print "Invalid login details: {0} {1}".format(username, password)
            return render(request, 'euskal/login.html', {'invalid': 'Datos de sesion incorrectos'})
    else:
        return render(request, 'euskal/login.html')


@login_required
def dashboard(request):
    up = UserProfile.objects.get(user=request.user)  # Get the UserProfile using the User.
    return render(request, 'euskal/dashboard.html', {'up': up})


@login_required
def auth_logout(request):
    logout(request)
    return redirect('/euskal/')


@login_required
def preferences(request):
    if request.user.username == 'admin':
        return HttpResponse("Admin doesn't have preferences")
    else:
        up = UserProfile.objects.get(user=request.user)  # Get the UserProfile using the User.

        if request.method == 'POST':

            left_choices_form = ChoicesForm(request.POST, prefix='left', up=up)  # Get the info from the form.
            right_choices_form = ChoicesForm(request.POST, prefix='right', up=up)  # Get the info from the form.

            try:
                upref = UserPreferences.objects.get(user_profile=up)  # Try to find the UserPreferences from the User.

            except UserPreferences.DoesNotExist:  # If they dont exists...
                upref = UserPreferences(user_profile=up)  # create it
                upref.save()  # and save it.

            if left_choices_form.is_valid() and right_choices_form.is_valid():  # Validate the forms

                left_choices = left_choices_form.save(commit=False)  # Save data from the form but don't save it
                right_choices = right_choices_form.save(commit=False)  # Save data from the form but don't save it
                left_choices.user_preferences = upref  # Assign the UserPreferences from the User
                right_choices.user_preferences = upref  # Assign the UserPreferences from the User
                left_choices.save()
                right_choices.save()

                # If there were choices saved in the UserPreferences before (The form was created before)...
                if upref.left_choices is not None:
                    old_lc = upref.left_choices  # save the old choices in another variable...
                if upref.right_choices is not None:
                    old_rc = upref.right_choices

                upref.left_choices = left_choices  # assign the new choices to the UserPreferences
                upref.right_choices = right_choices
                upref.save()  # and save.

                try:
                    # and delete the old choices. This way is possible to have only two choices objects per UserPreferences.
                    old_lc.delete()
                    old_rc.delete()
                except UnboundLocalError:
                    pass

                return render(request, 'euskal/preferences.html', {'left_choices_form': left_choices_form,
                                                                   'right_choices_form': right_choices_form,
                                                                   'saved': True})

            else:
                print left_choices_form.errors, right_choices_form.errors

        else:
            left_choices_form = ChoicesForm(prefix='left', up=up)  # Create the left_choices form.
            right_choices_form = ChoicesForm(prefix='right', up=up)  # Create the right_choices form.

        return render(request, 'euskal/preferences.html', {'left_choices_form': left_choices_form,
                                                           'right_choices_form': right_choices_form,
                                                            'saved': False})


def status(request):

    people_list = []

    for preference in UserPreferences.objects.all():
        left_choices_list = [preference.left_choices.first_choice.encode('utf-8').strip(),
                             preference.left_choices.second_choice.encode('utf-8').strip(),
                             preference.left_choices.third_choice.encode('utf-8').strip()]
        right_choices_list = [preference.right_choices.first_choice.encode('utf-8').strip(),
                              preference.right_choices.second_choice.encode('utf-8').strip(),
                              preference.right_choices.third_choice.encode('utf-8').strip()]

        p = Person(str(preference.user_profile), left_choices_list, right_choices_list)
        people_list.append(p)

    run_algorithm(people_list)

    return render(request, 'euskal/status.html', {'people_list': people_list})


@login_required
def vote_group_name(request):
    up = UserProfile.objects.get(user=request.user)  # Get the UserProfile using the User.
    if request.user.username == 'admin':
        return HttpResponse("Admin can't vote")
    elif not up.has_voted_group_name:
        if request.method == 'POST':
            options_form = OptionsForm(request.POST)
            if options_form.is_valid():
                name_choice = options_form.cleaned_data['name_choice']
                o = Option.objects.get(option_name=name_choice)
                o.votes += 1
                o.save()

            new_option_form = NewOptionForm(request.POST)
            if new_option_form.is_valid():
                try:
                    proposed_name = new_option_form.cleaned_data['option_name']
                    op = Option.objects.get(option_name=proposed_name)
                    if op:
                        options_form = OptionsForm()
                        return render(request, 'euskal/votegroupname.html', {'options_form': options_form,
                                                                             'already': True})
                except Option.DoesNotExist:
                    option = new_option_form.save(commit=False)
                    option.votes = 1
                    option.save()

            up.has_voted_group_name = True
            up.save()
            return render(request, 'euskal/votegroupname.html', {'voted': True})
        else:
            options_form = OptionsForm()
            new_option_form = NewOptionForm()

        return render(request, 'euskal/votegroupname.html', {'options_form': options_form,
                                                             'new_option_form': new_option_form,})
    else:
        return HttpResponse(
            "<h1 style='color:red'>Ya has votado anteriormente!</h1><a href='/euskal/'>Volver al inicio</a>")


def voting_results(request):
        option_list = Option.objects.order_by('-votes')
        return render(request, 'euskal/votingresults.html', {'option_list': option_list,})