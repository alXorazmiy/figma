from email.policy import default
from random import choices
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.

class Homiylar(models.Model):
    sana = (datetime.today().strftime("%d.%m.%Y"))
    yangi = 'yangi'
    moderatsiyada = 'moderatsiyada'
    tasdiqlangan = 'tasdiqlangan'
    bekor_qilingan = 'bekor qilingan'
    
    holat_choices = [
        (yangi, 'yangi'), 
        (moderatsiyada, 'moderatsiyada'),
        (tasdiqlangan, 'tasdiqlangan'), 
        (bekor_qilingan, 'bekor qilingan'),
    ]
    
    fish = models.CharField(max_length = 500)
    phono = models.CharField(max_length = 500,blank = True)
    summasi = models.IntegerField(blank = True, default = 0)
    sarf_summa = models.IntegerField(blank = True, default = 0)
    sana = models.CharField(max_length= 200, default = sana)
    holat = models.CharField(max_length = 20, choices = holat_choices, default = yangi)
    shaxs = models.CharField(max_length = 300, blank = True)
    nomi = models.CharField(max_length = 300, blank = True)
    
    
    
    def __str__(self):
        return self.fish
    
    


class Tolovlar(models.Model):
    sana = (datetime.today().strftime("%d.%m.%Y"))
    sana = models.CharField(max_length= 200, default = sana) 
    homiy_id = models.IntegerField()
    talaba_id = models.IntegerField()
    homiy_summa = models.IntegerField()
    
    def __str__(self):
        return self.sana + '  ' + str(self.summa)
    
    
class Talabalar(models.Model):
    
    bakalavr = 'bakalavr'
    magister = 'magister'
    choice_turi = [
        (bakalavr, 'bakalavr'),
        (magister, 'magister'),
    ]
   
    fish = models.CharField(max_length = 500)
    turi = models.CharField(max_length = 100, choices = choice_turi, default= bakalavr)
    phono = models.CharField(max_length = 500,blank = True)
    otm = models.CharField(max_length = 500)
    aj_summa = models.IntegerField(blank = True, default = 0)
    contract = models.IntegerField()
    #tolovlari = models.ForeignKey(Tolovlar, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.fish