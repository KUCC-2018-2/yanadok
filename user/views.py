from django.conf import settings
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from user.exceptions import DuplicateUserException
from yanadok.exceptions import BadRequestException, InvalidArgumentException
from .forms import CustomUserChangeForm
from .models import User
from .tokens import account_activation_token


def signup(request):
    if request.method == 'POST':
        body = extract_registration_body(request)

        try:
            check_invalid_signup_request(body)
            user = User.from_registration_info(body)
            user.save()
            return redirect('login')
        except (DuplicateUserException, BadRequestException, InvalidArgumentException) as e:
            return render_with_error_message(request, 'user/signup.html', e.message)

    return render(request, 'user/signup.html')


def check_invalid_signup_request(body):
    if is_user_exists(body['email']):
        raise DuplicateUserException

    if body['password'] != body['password_check']:
        raise BadRequestException('비밀번호를 확인해주세요.')

    return None


def render_with_error_message(request, template, message):
    return render(request, template, {"error": {"message": message}})


def is_user_exists(email):
    return User.objects.filter(email=email).exists()


def extract_registration_body(request):
    return {key: request.POST[key] for key in ['email', 'password', 'password_check', 'university', 'name', 'nickname']}


def login_view(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['username']).first()
        if not user or not user.check_password(request.POST['password']):
            return render_with_error_message(request,
                                             'user/login.html',
                                             '아이디나 비밀번호가 일치하지 않습니다.')
        login(request, user)
        return redirect('home')

    return render(request, 'user/login.html')


def send_registration_email(request, user):
    current_site = get_current_site(request)
    mail_subject = 'Activate your blog account.'
    message = render_to_string('user/acc_active_email.html', {
        'user': user,
        'domain': settings.EMAIL_AUTH_HOST if settings.EMAIL_AUTH_HOST else 'localhost',
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token': account_activation_token.make_token(user),
    })
    email = EmailMessage(
        mail_subject, message, to=[user.email]
    )
    email.send()


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    #     usolved problem
    except(TypeError, ValueError, OverflowError, IntegrityError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'user/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/user/profile')

    else:
        form = CustomUserChangeForm(instance=request.user)
        args = {'form': form, 'user': request.user}
        return render(request, 'user/edit_profile.html', args)
