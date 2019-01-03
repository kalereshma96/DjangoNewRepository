from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from .forms import UseRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .exceptions import InvalidToken, TokenError


# def home(request):
#     return render(request, 'users/home.html')

class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        # return Response(content)
        return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created..!!You are now able to login')
            return redirect('login')
    else:
        form = UseRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


def get_authenticate_header(self, request):
    return '{0} realm="{1}"'.format(
        AUTH_HEADER_TYPES[0],
        self.www_authenticate_realm,
    )


def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except TokenError as e:
        raise InvalidToken(e.args[0])

    return Response(serializer.validated_data, status=status.HTTP_200_OK)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
