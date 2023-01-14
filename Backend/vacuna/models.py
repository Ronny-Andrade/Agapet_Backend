from django.db import models
from pet.models import Animal, Mascota
from user.models import User

# Create your models here.
class Vacuna(models.Model):
    vacuna_id = models.AutoField(primary_key=True)
    idanimal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)
    idpet = models.ForeignKey(Mascota, on_delete=models.CASCADE, null=True)
    iduser =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nombre_vacuna = models.CharField(max_length=200)
    descripcion_vacuna = models.CharField(max_length=200)
    imagen64 = models.TextField(blank=True, null=True)
    lugar_vacuna = models.CharField(max_length=100,blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    
    def info_completa(self):
        return "{}".format(self.vacuna_id,self.idanimal,self.idpet, self.iduser ,self.nombre_vacuna, self.descripcion_vacuna, self.imagen64,self.fecha)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'vacuna'

