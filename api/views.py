
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from drf_yasg.utils import swagger_auto_schema
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from homiy.models import Homiylar, Talabalar, Tolovlar
from .serializers import TalabalarSerializers
# Create your views here.


class HomePage(GenericAPIView):
    #serializer_class = HomiyCreateSerializers
    def get(self,request):
        talabalar = Talabalar.objects.values_list('contract')
        talabalar = sum( [item[0] for item in talabalar])
        
        homiylar = Homiylar.objects.values_list('sarf_summa')
        homiylar =sum( [item[0] for item in homiylar])
        natija = talabalar - homiylar
        
        dict = {
            'tolangan':homiylar,
            'talab': talabalar,
            'kerak': natija,
        }
       
        return Response(dict)
    
    def post(self, request):
        print('yesssssssssss')
        print(request.data)
        nomi = ''
        shaxs = 'jiymoniy'
        if request.data['nomi']:
            nomi = request.data['nomi']
            shaxs = 'yurudik'
        post_new = Homiylar.objects.create(
            fish=request.data['fish'],
            phono=request.data['phono'],
            summasi=request.data['summasi'],
            nomi = nomi,
            shaxs = shaxs,
        )
        
        return Response({'Post': model_to_dict(post_new)})

class HomiylarPage(APIView):
    #serializer_class = HomiylarSerializers
    def get(self, request):
        homiylar = Homiylar.objects.all().values('id', 'fish', 'phono', 'summasi', 'sarf_summa' ,'sana', 'holat')
        print(homiylar)
        return Response(homiylar)
    
class HomiylarDetailPage(APIView):
    #serializer_class = HomiyUpdateSerializers
    def get(self, request, pk):
        homiy = Homiylar.objects.get(id = pk)
        return Response(model_to_dict(homiy))
    
    def put(self,request,pk):
        homiy_update = Homiylar.objects.get(id = pk)
        print(homiy_update.nomi)
        
        if homiy_update.shaxs == "yuridik":
            homiy_update.fish = request.data['fish']
            homiy_update.phono = request.data['phono']
            homiy_update.holat = request.data['holat']
            homiy_update.summasi = request.data['summasi']
            homiy_update.nomi = request.data['nomi']
            homiy_update.save()
        else:
            
            homiy_update.fish = request.data['fish']
            homiy_update.phono = request.data['phono']
            homiy_update.holat = request.data['holat']
            homiy_update.summasi = request.data['summasi']
            homiy_update.save()
        
        return Response(model_to_dict(homiy_update))
    
class TalabalarAPIView(APIView):
    #serializer_class = TalabalarSerializers
    def get(self, request):
        talabalar = Talabalar.objects.all().values() 
        return Response(talabalar)
    
  
class TalabalarDetailAPIView(GenericAPIView):
    serializer_class = TalabalarSerializers
    def get(self, request,pk):
        talaba = Talabalar.objects.get(id = pk)
        serializers = TalabalarSerializers(talaba)
        homiylar = Homiylar.objects.filter(holat = 'tasdiqlangan').values('id', 'fish')
        otmlar = set(Talabalar.objects.values_list('otm'))
        tolovlar = {}
        homiylar_bor = False
        tolovlar = Tolovlar.objects.filter(talaba_id=pk).values('id', 'homiy_id', 'homiy_summa')
        for item in tolovlar:
            homiy_ism = Homiylar.objects.get(id =item['homiy_id'] )                   
            item['homiy_fish'] = homiy_ism.fish  
            homiylar_bor = True
        
        return Response({ 
                'talaba':serializers.data, 
                'talabaga_homiylar':tolovlar, 
                'homiylar': homiylar , 
                'otmlar': otmlar
            } )
        
   
    
    def put(self, request, pk): 
    
        talaba_update = Talabalar.objects.get(id = pk)
        talaba_update.fish = request.data['fish']
        talaba_update.phono = request.data['phono']
        talaba_update.otm = request.data['otm']
        talaba_update.contract = request.data['contract']
        talaba_update.save()
        return Response(model_to_dict(talaba_update))
    
    
    def post(self,request, pk):
        
        homiy = Homiylar.objects.get(id = request.data['homiy_id'])
        talaba = Talabalar.objects.get(id = pk)
        
        if int(homiy.summasi) >= int(request.data['homiy_summa']) and int(talaba.aj_summa ) + int(request.data['homiy_summa']) <= int(talaba.contract):
            tolovlar = Tolovlar.objects.create(homiy_id = homiy.id, talaba_id = pk, homiy_summa = request.data['homiy_summa'])
            tolovlar.save()
            homiy.summasi = int(homiy.summasi) - int(request.data['homiy_summa'])
            homiy.sarf_summa = int(homiy.sarf_summa) + int(request.data['homiy_summa'])
            homiy.save()
            talaba.aj_summa = int(talaba.aj_summa ) + int(request.data['homiy_summa'])
            talaba.save()
            return self.get(request, pk)
        else:
            return self.get(request, pk)
    #
    
    def delete(self, request,pk):
        tolov_delete = Tolovlar.objects.get(id = request.data['id'])
        tolov_delete.delete()
        return self.get(request,pk)
    
    
class TalabalarAddAPIView(GenericAPIView):
    #serializer_class = TalabalarCreateSerializers
    def get(self, request):
        turi = ['bakalavr', 'magister']
        otmlar = set(Talabalar.objects.values_list('otm')) 
        return Response({'otmlar': otmlar, 'talabalik_turi': turi})
    def post(self, request):
        post_talaba = Talabalar.objects.create(
            fish = request.data['fish'],
            phono = request.data['phono'],
            otm = request.data['otm'],
            turi = request.data['turi'],
            contract = request.data['contract'],
        )
        return Response(model_to_dict(post_talaba))