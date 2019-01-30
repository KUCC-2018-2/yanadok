from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .models import User
from .forms import CustomUserChangeForm
from django.core.mail import EmailMessage

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            try:
                user.save()
            except IntegrityError:
                return render(request, 'user/signup.html', {
                    'form': form,
                    'invalid_email': "이미 사용중인 email 입니다.",
                })
            else:
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('user/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token':account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')

    else:
        form = CustomUserCreationForm()

    return render(request, 'user/signup.html', {'form': form})


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
        args = {'form': form, 'user':request.user}
        return render(request, 'user/edit_profile.html', args)
