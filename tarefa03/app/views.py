from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    user_list = [
        {"nome": "Artur", "matricula": "00010", "idade": "17", "cidade": "Santa Maria"},
        {"nome": "Igor Murilo", "matricula": "00011", "idade": "17", "cidade": "São tome"},
        {"nome": "william", "matricula": "00012", "idade": "21", "cidade": "São pedro"},
        {"nome": "Dinho", "matricula": "00013", "idade": "25", "cidade": "Machado"},
        {"nome": "Pedro Lucas", "matricula": "00014", "idade": "19", "cidade": "São tome"}
    ]

    context = {
        "usuarios" : user_list
    }

    return render(request, "usuarios.html" , context)
