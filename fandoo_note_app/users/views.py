from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework_jwt.settings import api_settings

from .forms import UseRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your Account has been created..!!You are now able to login')
            return redirect('login')
    else:
        form = UseRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Account has been updated!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


def get_jwt_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    print(payload)
    return jwt_encode_handler(payload)


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                data = get_jwt_token(user)
                # return HttpResponse(data)
                myToken = get_jwt_token(user)
                print(myToken)
                myUrl = '/login/'
                # head = {'Authorization': 'token {}'.format(myToken)}
                headers = {'Content-Type': 'application/json'}
                # response = requests.post(myUrl, headers=head)
                response = redirect(myUrl)
                response['Token'] = data
                # requests.get("Content-Type", "application/json")
                # print(response)
                # return HttpResponse(data)
                # return response
                return HttpResponseRedirect('/profile')
                # return render(request, 'users/profile.html', context)

            else:
                return HttpResponse("Your account was inactive.")

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'users/login.html', {})

    # # Bearer Tokens from Gmail Actions will always specify this issuee.
    # GMAIL_ISSUEE = 'gmail@system.gserviceaccount.com'
    #
    # # Intended audience of the token, based on the sender's domain
    # AUDIENCE = 'https://example.com'
    #
    # # Get this value from the request's Authorization HTTP header.
    # # For example, for "Authorization: Bearer AbCdEf123456" use "AbCdEf123456"
    # BEARER_TOKEN = 'AbCdEf123456'
    #
    # try:
    #     # Verify valid token, signed by google.com, intended for a third party.
    #     token = get_jwt_token.verify_id_token(BEARER_TOKEN, AUDIENCE)
    #     print('Token details: %s' % token)
    #
    #     if token['azp'] != GMAIL_ISSUEE:
    #         print('Invalid issuee')
    # except:
    #
    #     print('Invalid token')
    #
    # # Token originates from Google and is targeted to a specific client.
    # print('The token is valid')


# response = requests.get('https://website.com/id', headers = {'Authorization': 'access_token myToken'})


