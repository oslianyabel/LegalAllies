from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.mail import send_mail
from django.conf import settings
from .models import HomeConfiguration, Category, SocialNetwork, Article
from django.db.models import Q


def index(request):
    """
    Vista principal del sitio.
    """
    # Manejo del formulario de contacto
    if request.method == 'POST' and 'contact_name' in request.POST:
        name = request.POST.get('contact_name')
        email = request.POST.get('contact_email')
        message_text = request.POST.get('contact_message')
        
        home_config = HomeConfiguration.objects.first()
        
        if home_config:
            subject = f'Mensaje de contacto de {name}'
            message = f'De: {name} ({email})\n\nMensaje:\n{message_text}'
            
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [home_config.contact_email],
                    fail_silently=False,
                )
                messages.success(request, '¡Mensaje enviado exitosamente!')
            except Exception as e:
                messages.error(request, 'Error al enviar el mensaje. Inténtalo de nuevo más tarde.')
        
        return redirect('app:index')
    
    # Búsqueda de artículos
    search_query = request.GET.get('search', '')
    search_results = None
    
    if search_query:
        search_results = Article.objects.filter(
            Q(title__icontains=search_query) | Q(body__icontains=search_query)
        ).select_related('category', 'author')[:10]
    
    home_config = HomeConfiguration.objects.first()
    categories = Category.objects.all()
    social_networks = SocialNetwork.objects.all()
    
    context = {
        'home_config': home_config,
        'categories': categories,
        'social_networks': social_networks,
        'search_query': search_query,
        'search_results': search_results,
    }
    
    return render(request, 'app/index.html', context)



def article_detail(request, slug):
    """
    Vista de detalle de un artículo.
    """
    article = get_object_or_404(Article, slug=slug)
    
    # Artículos relacionados de la misma categoría
    related_articles = Article.objects.filter(
        category=article.category
    ).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    
    return render(request, 'app/article_detail.html', context)


def category_articles(request, slug):
    """
    Vista de artículos por categoría.
    """
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category).select_related('author')
    other_categories = Category.objects.exclude(id=category.id)
    
    context = {
        'category': category,
        'articles': articles,
        'other_categories': other_categories,
    }
    
    return render(request, 'app/category_articles.html', context)


@login_required
def profile(request):
    """
    Vista del perfil de usuario.
    """
    return render(request, 'app/profile.html')


def register(request):
    """
    Vista de registro de usuario.
    """
    if request.user.is_authenticated:
        return redirect('app:index')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('app:index')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = UserCreationForm()
    
    return render(request, 'app/register.html', {'form': form})


def login_view(request):
    """
    Vista de inicio de sesión.
    """
    if request.user.is_authenticated:
        return redirect('app:index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            next_url = request.GET.get('next', 'app:index')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'app/login.html')


@login_required
def logout_view(request):
    """
    Vista de cierre de sesión.
    """
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('app:index')


@login_required
def change_password(request):
    """
    Vista de cambio de contraseña.
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
            return redirect('app:profile')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'app/change_password.html', {'form': form})

