from pyexpat import model
from rest_framework import serializers 
from homiy.models import Homiylar
from homiy.models import Talabalar
from homiy.models import Tolovlar


    
class TalabalarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Talabalar 
        fields = ('id', 'fish', 'phono', 'otm', 'turi', 'contract', 'aj_summa')
        


        
        
