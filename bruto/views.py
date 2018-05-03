from django.shortcuts import render

def home(request):
    return render(request, 'views/home.html', {
        'site_title': 'Página Principal'
    })

def upload(request):
    return render(request, 'views/upload.html', {
        'site_title': 'Enviar horários'
    })

def browser(request):
    return render(request, 'views/browser.html', {
        'site_title': 'Ver horários'
    })
