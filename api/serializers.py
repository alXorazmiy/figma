from pyexpat import model
from rest_framework import serializers 
from homiy.models import Homiylar
from homiy.models import Talabalar
from homiy.models import Tolovlar


    
class TalabalarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Talabalar 
        fields = "__all__"
        
        
class TalabalarAddGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Talabalar 
        fields = ('turi', 'otm')
        
        
class TalabalarAddPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Talabalar 
        fields = ('fish', 'phono', 'otm', 'turi', 'contract')
        
        
class HomiylarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Homiylar 
        fields  = "__all__"
    
class HomiylarCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Homiylar 
        fields = ('fish', 'phono', 'summasi', 'nomi')
        
        
class HomiylarDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Homiylar 
        fields = ('fish', 'phono', 'holat', 'summasi', 'nomi')
        

class TolovlarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tolovlar 
        fields = ('homiy_id', 'homiy_summa')
        
class TolovlarDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tolovlar 
        fields = ('id','homiy_summa')