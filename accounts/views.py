from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authentifier l'utilisateur
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Connexion de l'utilisateur
                auth_login(request, user)
                # Rediriger vers la page d'accueil ou une page protégée
                return redirect('home')  # Remplacez 'home' par l'URL de la page de redirection souhaitée
            else:
                # Si l'utilisateur n'est pas trouvé ou les informations sont incorrectes
                form.add_error(None, 'Identifiants invalides')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    # Déconnecter l'utilisateur
    auth_logout(request)
    # Rediriger vers la page de connexion ou une autre page de votre choix
    # return redirect('login')  # Remplacez 'login' par l'URL de la page de connexion ou autre
    return render(request, 'accounts/logout.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Crée l'utilisateur
            return redirect('login')  # Redirige vers la page de connexion après l'inscription
    else:
        form = RegisterForm()

    # return render(request, 'accounts/register.html', {'form': form})
    return render(request, 'accounts/register.html')

def profile(request):
    # L'utilisateur est déjà authentifié grâce au décorateur @login_required
    user = request.user  # On récupère l'objet User de l'utilisateur connecté

    # Tu peux ajouter d'autres informations de profil si tu en as besoin
    context = {
        'user': user,  # On passe l'utilisateur à notre template
    }

    return render(request, 'accounts/profile.html', context)
    # return render(request, 'accounts/profile.html')

def edit_profile(request):
    if request.user.is_authenticated:
        # Passer les informations de l'utilisateur au template
        return render(request, 'accounts/edit_profile.html', {'user': request.user})
    else:
        # Si l'utilisateur n'est pas connecté, redirige-le vers la page de connexion
        return redirect('login')
    # return render(request, 'accounts/edit_profile.html')

def change_password(request):
    if request.method == 'POST':
        # Création d'un formulaire de changement de mot de passe avec l'utilisateur actuel
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            # Enregistrer le nouveau mot de passe
            form.save()
            # Mettre à jour la session de l'utilisateur pour qu'il n'ait pas besoin de se reconnecter
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Votre mot de passe a été modifié avec succès.')
            return redirect('profile')  # Redirige l'utilisateur vers son profil après le changement
        else:
            # Si le formulaire est invalide, renvoie les erreurs
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'accounts/change_password.html', {'form': form})
    # return render(request, 'accounts/change_password.html')

def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "Aucun utilisateur trouvé avec cet email.")
                return render(request, 'accounts/forgot_password.html', {'form': form})

            # Générer un token de réinitialisation et l'envoyer par email
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(user.pk.encode())

            # Créer le lien de réinitialisation
            reset_link = f'http://{get_current_site(request).domain}/reset-password/{uid}/{token}/'

            # Créer le contenu de l'email
            subject = "Réinitialisation de votre mot de passe"
            message = render_to_string('accounts/password_reset_email.html', {
                'reset_link': reset_link,
                'user': user,
            })

            send_mail(subject, message, 'no-reply@monapplication.com', [email])

            messages.success(request, 'Un lien de réinitialisation a été envoyé à votre adresse email.')
            return redirect('login')  # Rediriger l'utilisateur vers la page de connexion
    else:
        form = PasswordResetForm()

    return render(request, 'accounts/forgot_password.html', {'form': form})
    # return render(request, 'accounts/forgot_password.html')

def reset_password(request):
    try:
        uid = urlsafe_base64_decode(uid).decode()
        user = get_object_or_404(User, pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, default_token_generator):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Votre mot de passe a été réinitialisé avec succès.')
                return redirect('login')
        else:
            form = SetPasswordForm(user)
        
        return render(request, 'accounts/reset_password.html', {'form': form})
    else:
        messages.error(request, 'Le lien de réinitialisation est invalide ou a expiré.')
        return redirect('forgot_password')
    # return render(request, 'accounts/reset_password.html')