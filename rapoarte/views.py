from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autentificarea utilizatorului
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirecționare către pagina corespunzătoare în funcție de rolul utilizatorului
            if user.type == 1:  # Administrator
                return redirect('pagina_administrator')
            elif user.type == 2:  # Angajat
                return redirect('pagina_angajat')
            elif user.type == 3:  # Contracte
                return redirect('pagina_contracte')
        else:
            # Dacă autentificarea nu reușește, afișați un mesaj de eroare
            error_message = "Nume de utilizator sau parolă incorecte."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def rapoarte_page(request):
    return render(request, 'rapoarte.html', context={})

def contracte_page(request):
    return render(request, 'contracte.html', context={})
