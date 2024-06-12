from django.shortcuts import render, redirect
from .forms import AgendamentoForm

def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Redireciona para a página de sucesso
    else:
        form = AgendamentoForm()
    return render(request, 'agendar.html', {'form': form})
