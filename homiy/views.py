from django.shortcuts import render
from .models import Homiylar, Talabalar, Tolovlar
from django.shortcuts import redirect
from django.urls import reverse

from django.core.paginator import Paginator
from datetime import datetime




# Create your views here.

def HomePageView(request):
    
    return render(request, 'home.html', {})


def DonePageView(request):
    print(request.POST)
    
   
    if request.method == 'POST':
        if request.POST.get('ism') and request.POST.get('phone'):
            
            
            ism = request.POST.get('ism')
            phone = request.POST.get('phone')
            summa = request.POST.get('summa')
            shaxs = 'jismoniy'
            
            
            if request.POST.get('boshqa_summa'):
                summa = request.POST.get('boshqa_summa')
            
            if request.POST.get('tashkilot_nomi'):
                print('yessssssssssssssssssssss')
                nomi = request.POST.get('tashkilot_nomi')
                shaxs = 'yuridik'
                post = Homiylar.objects.create(fish = ism, phono =phone, summasi = summa,  shaxs = shaxs, nomi = nomi )
            else:   
                post = Homiylar.objects.create(fish = ism, phono =phone, summasi = summa, shaxs = shaxs )
                
        
            

    return render(request, 'done.html', {})





# Create your views here.

def DashboardPageView(request):
    
    talabalar = Talabalar.objects.values_list('contract')
    talabalar = sum( [item[0] for item in talabalar])
    
    homiylar = Homiylar.objects.values_list('sarf_summa')
    homiylar =sum( [item[0] for item in homiylar])
    natija = talabalar - homiylar
    
   
    
    return render (request, 'admin_dashboard.html', {
        'jami':homiylar,
        'talab': talabalar,
        'kerak': natija,
        }
    )

def HomiylarPageView (request):
    button_if = 0
    x = 4  
    print(request.GET)
    homiylar =Homiylar.objects.all()
    homiylar2 =Homiylar.objects.all()
    
    
    try:
        if request.method == 'GET':
            if request.GET.get('izlash'):
                print('yessssssssssssssssssssssssssssssssssssssssssss')
                homiylar = Homiylar.objects.filter(fish__contains = request.GET.get('izlash'))
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            if request.GET.get('select') == 'barchasi' and request.GET.get('partydate') == '' and ( not request.GET.get('summa')):
                homiylar =Homiylar.objects.all()
            
            elif request.GET.get('select') != 'barchasi'  and request.GET.get('summa') and request.GET.get('partydate') != '':
                sana2 = request.GET.get('partydate')
                kun = sana2[8:]
                oy = sana2[5:7]
                yil = sana2[:4]
                sana2 = kun + "." + oy + '.' +yil
                homiylar = Homiylar.objects.filter(holat = request.GET.get('select'),summasi = request.GET.get('summa'), sana = sana2)
                
            
            
            elif request.GET.get('select') != 'barchasi'  and request.GET.get('summa'):
                homiylar = Homiylar.objects.filter(holat = request.GET.get('select'),summasi = request.GET.get('summa'))
                
                
            elif request.GET.get('select') != 'barchasi' and request.GET.get('partydate') != '':
                sana2 = request.GET.get('partydate')
                kun = sana2[8:]
                oy = sana2[5:7]
                yil = sana2[:4]
                sana2 = kun + "." + oy + '.' +yil
                homiylar = Homiylar.objects.filter(holat = request.GET.get('select'), sana = sana2)
                
            elif request.GET.get('partydate') != ''  and request.GET.get('summa'):
                sana2 = request.GET.get('partydate')
                kun = sana2[8:]
                oy = sana2[5:7]
                yil = sana2[:4]
                sana2 = kun + "." + oy + '.' +yil
                homiylar = Homiylar.objects.filter(sana = sana2)
                homiylar = Homiylar.objects.filter(summasi = request.GET.get('summa'),sana = sana2)
                
            elif request.GET.get('select') != 'barchasi':
                homiylar = Homiylar.objects.filter(holat = request.GET.get('select'))
                
            elif request.GET.get('partydate') != '':
                sana2 = request.GET.get('partydate')
                kun = sana2[8:]
                oy = sana2[5:7]
                yil = sana2[:4]
                sana2 = kun + "." + oy + '.' +yil
                homiylar = Homiylar.objects.filter(sana = sana2)
                
                
            elif request.GET.get('summa'):
                homiylar = Homiylar.objects.filter(summasi = request.GET.get('summa'))
                                
           
            
            
            
    except:
       pass
    
    
    button_if = len(homiylar)
    paginator = Paginator(homiylar, x )
    page = request.GET.get('page')
    homiy = paginator.get_page(page)
    
    
    if button_if % 4 == 0:
        button_list = [x+1 for x in range(int((button_if ) / 4 ))]
    else:
        button_list = [x+1 for x in range(int((button_if) / 4 )+1)]
    
    
    try:
    
        x= 1 
        x2 =1
        x = int( 4 * int(page)-3)
        x2 =int(int(4) * int(page))
    except:
        x= 1 
        x2 =1
        x = int( 4 * int(x)-3)
        x2 =int(int(4) * int(x))
        
    return render (request, 'admin_homiylar.html', {
        'homiylar': homiylar,
        'homiy': homiy,
        'button_if':button_if,
        'button_list': button_list,
        'x':x,
        'x2':x2,
        'homiylar2':homiylar2,
    })
    
    
def HomiylarSinglePageView(request,pk):
    try:
        update = Homiylar.objects.get(id = pk)
        update.fish = request.POST.get('ism')
        update.phono = request.POST.get('phone')
        update.summasi = request.POST.get('select_summa')
        update.holat = request.POST.get('select_holat')
        
        
        if request.POST.get('nomi'):
            update.nomi = request.POST.get('nomi')
        
        update.save()    
    except:
        pass
    homiy = Homiylar.objects.get(id = pk)
    
    return render (request, 'admin_homiylar_single.html', {
        'homiy':homiy,
    })
   
    
def TalabalarPageView(request):
    button_if = 0
    x = 4  
    talabalar =Talabalar.objects.all()
    
    otm = Talabalar.objects.values_list('otm')
    otm = set( [item[0] for item in otm])
    
    
    if request.method == 'GET':
       
        
        if request.GET.get('select_turi') == 'barchasi' and request.GET.get('otm') == 'barchasi':
            print('1')
            talabalar =Talabalar.objects.all()
            
        elif request.GET.get('select_turi') != 'barchasi' and request.GET.get('otm') != 'barchasi':
            print('2')
            talabalar =Talabalar.objects.filter(turi = request.GET.get('select_turi') , otm =request.GET.get('otm'))
            
            if (len(talabalar)) == 0:
                if request.GET.get('izlash'):
                    talabalar = Talabalar.objects.filter(fish__contains = request.GET.get('izlash'))
                else:
                    talabalar =Talabalar.objects.all()
                
            
        elif request.GET.get('select_turi') != 'barchasi' and request.GET.get('otm') == 'barchasi':
            print('3')
            talabalar =Talabalar.objects.filter(turi = request.GET.get('select_turi') )
        elif request.GET.get('select_turi') == 'barchasi' and request.GET.get('otm') != 'barchasi':
            print('4')
            talabalar =Talabalar.objects.filter( otm =request.GET.get('otm'))
            
    
    button_if = len(talabalar)
    paginator = Paginator(talabalar, x )
    page = request.GET.get('page')
    homiy = paginator.get_page(page)
    
    
    if button_if % 4 == 0:
        button_list = [x+1 for x in range(int((button_if ) / 4 ))]
    else:
        button_list = [x+1 for x in range(int((button_if) / 4 )+1)]
    
    
    try:
    
        x= 1 
        x2 =1
        x = int( 4 * int(page)-3)
        x2 =int(int(4) * int(page))
    except:
        x= 1 
        x2 =1
        x = int( 4 * int(x)-3)
        x2 =int(int(4) * int(x))
    return render (request, 'admin_talabalar.html', {
        'homiy': homiy,
        'button_if':button_if,
        'button_list': button_list,
        'x': x,
        'x2': x2,
        'otm': otm,
        
    })
    
def TalabalarAddPageView (request):
    
    if request.POST:
        if request.POST.get('ism') and request.POST.get('phone') and request.POST.get('otm') and request.POST.get('select_turi') and request.POST.get('summa'):
            create = Talabalar.objects.create(fish = request.POST.get('ism'), phono =request.POST.get('phone'), otm = request.POST.get('otm'), turi =request.POST.get('select_turi') , contract = request.POST.get('summa') )
            create.save()
            
            id = Talabalar.objects.get(fish = request.POST.get('ism'))
            return redirect(f'https://metsenat.herokuapp.com/talabalar/{id.id}')
    else:
    
        otm = Talabalar.objects.values_list('otm')
        otm = set( [item[0] for item in otm])
        return render (request, 'admin_talabalar_add.html',{
            'otm': otm,
        })
    


    
    
def TalabalarSinglePageView(request,pk):
    try:    
        if request.POST.get('ism') and request.POST.get('phone') and request.POST.get('otm') and request.POST.get('summa'):
           
            update = Talabalar.objects.get(id = pk)
            update.fish = request.POST.get('ism')
            update.phono = request.POST.get('phone')
            update.otm = request.POST.get('otm')
            update.contract = request.POST.get('summa')
            
            update.save()    
            
        if request.POST.get('homiyism') != 'Homiyni tanlang' and request.POST.get('homiysumma'):
            
            homiy_id = Homiylar.objects.get(fish = request.POST.get('homiyism'))
            print(homiy_id.summasi)
            talaba_id = Talabalar.objects.get(id = pk)
            print(talaba_id)
            
            if int(homiy_id.summasi) >= int(request.POST.get('homiysumma')):
                print('yessssssssssssssssssssssssssss')
                tolovlar = Tolovlar.objects.create(homiy_id = homiy_id.id, talaba_id = pk, homiy_summa = request.POST.get('homiysumma'))
                tolovlar.save()
                homiy_id.summasi = int(homiy_id.summasi) - int(request.POST.get('homiysumma'))
                homiy_id.sarf_summa = int(homiy_id.sarf_summa) + int(request.POST.get('homiysumma'))
                homiy_id.save()
                talaba_id.aj_summa = int(talaba_id.aj_summa ) + int(request.POST.get('homiysumma'))
                talaba_id.save()
                
        if request.POST.get("delete"):
            print('delete')
        if request.POST.get("saqlash"):
            print('delete')
           
    except:
        pass
    
    homiylar = Homiylar.objects.filter(holat = 'tasdiqlangan')
    talaba = Talabalar.objects.get(id = pk)
    tolovlar = Tolovlar.objects.filter(talaba_id = pk)

    tolov_list = []
    bor = False
    for item in tolovlar:
        homiy_ism = Homiylar.objects.get(id = item.homiy_id)
      
        item.homiy_id = homiy_ism
        tolov_list.append(item)
        bor = True
   
    

    otm = Talabalar.objects.values_list('otm')
    otm = set( [item[0] for item in otm])
    return render (request, 'admin_talabalar_single.html', {
        'talaba': talaba,
        'otm':otm,
        'homiylar':homiylar,
        'tolovlar':tolov_list,
        'bor': bor,
                
 })  
    
    

