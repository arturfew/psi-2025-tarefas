from django.shortcuts import render,get_object_or_404
from . models import Postagem,Footer,Header
# Create your views here.
def index(request):
    postagem = Postagem.objects.all()
    footer = Footer.objects.first()
    header = Header.objects.first()
    context = {"postagem":postagem, "footer":footer, "header":header}
    return render(request,'blog/index.html',context)
def noticia(request, id_post):
    postagem = get_object_or_404(Postagem, id=id_post)
    footer = Footer.objects.first()
    header = Header.objects.first()
    context = {"postagem":postagem, "footer":footer, "header":header}
    return render(request,'blog/noticia.html',context)