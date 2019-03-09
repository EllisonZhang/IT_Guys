from django.shortcuts import render


# Create your views here.
def index(request):
    response = render(request, 'wegame/home.html')
    return response

def about(request):
    response = render(request, 'wegame/about.html')
    return response

def login(request):
    response = render(request, 'wegame/login.html')
    return response

def logout(request):
    response = render(request, 'wegame/logout.html')
    return response

def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            profile = profile_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True

        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)

    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    
    return render(request, 
                'registration/registration.html', 
                {'user_form': user_form,
                  'profile_form': profile_form,
                  'registered': registered})

def games(request):
    response = render(request, 'wegame/games.html')
    return response
