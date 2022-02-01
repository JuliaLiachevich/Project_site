from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import RestoranForm, BludaForm
from django.views.generic import DetailView
from django.contrib import  auth

def text(request):
    restoran=Restoran.objects.all()
    username = auth.get_user(request).username
    if username:
        return render(request, 'restoran/restorani.html', {'restoran': restoran, 'username': username}, )
    else:
        return render(request, 'restoran/restoran_vse.html', {'restoran': restoran, 'username': username}, )

def reg_restoran(request):
    error = ''
    if request.method =='POST':
        form= RestoranForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restoran')
        else:
            error = 'Форма была неверной'
    form=RestoranForm()
    username = auth.get_user(request).username
    data={
        'form':form,
        'error':error,
        'username': username
    }
    return render(request, 'restoran/reg_restoran.html', data)

class AboutDetailView(DetailView):
    model = Restoran
    template_name = 'restoran/about_rest.html'
    context_object_name = 'restoran'

def reg_food(request):
    error = ''
    if request.method =='POST':
        form= BludaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restoran')
        else:
            error = 'Форма была неверной'
    form=BludaForm()
    username=auth.get_user(request).username
    data={
        'form':form,
        'error':error,
        'username':username }
    return render(request, 'restoran/food.html', data)


def bezlactoz(request):
    objects_to_exclude = ['молоко', 'молочный','сливки','сливоч','творог','творожный','сыр','сырный', 'майонез']
    bluda = Bluda.objects.all()
    for i in objects_to_exclude:
        bluda = bluda.exclude(full_text__icontains=i)
    return render(request, 'main/bezlactoz.html', {'bluda': bluda})

def allergia_prod(request):
    user_text = request.GET['usertext']
    user_text=user_text.split(' ')
    objects_to_exclude = user_text
    bluda = Bluda.objects.all()
    for i in objects_to_exclude:
        bluda = bluda.exclude(full_text__icontains=i)
    return render(request, 'main/allergia2.html',  {'bluda': bluda})
#
def diabet(request):
    objects_to_exclude = ['сахар','семечки','майонез','консерв','варенье','джем','сливки','маскарпоне','сливочное масло',
                          'скумбрия','баранина','халва','шоколад','мороженое','батон', 'белый хлеб', 'утка', 'дрожжи'
                          'утин','баранина','баран','сало','маргарин','кондитерский жир','спред', 'картошка фри', 'бургер', 'воздушная кукуруза'
                          'курага','финики','инжир','изюм','хурма','дыня','виноград','бананы',]
    bluda = Bluda.objects.all()
    for i in objects_to_exclude:
        bluda = bluda.exclude(full_text__icontains=i)
    return render(request, 'main/diabet.html', {'bluda': bluda, })

def bezgluten(request):
    objects_to_exclude = ['пшеница', 'рожь','спельта','ячмень','овес','камут','тритикале','пшеничная','ржаная',
                          'овсяная','глютен','пшеничный крахмал','панировочные сухари','макароны','кетчуп', 'томатная паста',
                          'сгущенное молоко','отруби','виски','пиво','джин','квас',]
    bluda = Bluda.objects.all()
    for i in objects_to_exclude:
        bluda = bluda.exclude(full_text__icontains=i)
    return render(request, 'main/bezgluten.html', {'bluda': bluda})

def vegan(request):
    objects_to_exclude = ['купица','перепелка','утка','цыпленок','мясо','кролик','крылышки',
                          'баранина','телятина','говядина','козлятина','конина','оленина','свинина',
                          'сердце','сердечки','почки','печень','шейки','желудочки','кальмар','креветки',
                          'устрицы','рыба','краб','треска','окунь','сибас','сельдь','горбуша','форель', 'скумбрия',]
    bluda = Bluda.objects.all()
    for i in objects_to_exclude:
        bluda = bluda.exclude(full_text__icontains=i)
    return render(request, 'main/vegan.html', {'bluda': bluda, })

def control():
    pass




