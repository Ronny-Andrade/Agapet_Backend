from django.db import models
from pet.models import Animal, Mascota

# Create your models here.
class Vacuna(models.Model):
    vacuna_id = models.AutoField(primary_key=True)
    idanimal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    nombre_vacuna = models.CharField(max_length=200)
    descripcion_vacuna = models.CharField(max_length=200)
    
    def info_completa(self):
        return "{}".format(self.vacuna_id,self.idanimal, self.nombre_vacuna, self.descripcion_vacuna)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'vacuna'

class Vacuna_Mascota(models.Model):
    vacuna_mascota_id = models.AutoField(primary_key=True)
    vacuna_id = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    idpet = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    imagen_blob = models.BinaryField(blank=True, null=True) 
    feche_inicio = models.DateField(blank=True, null=True)
    feche_fin = models.DateField(blank=True, null=True)

    def info_completa(self):
        return "{}".format(self.vacuna_mascota_id,self.vacuna_id, self.idpet, self.feche_inicio, self.feche_fin, self.imagen_blob)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'vacuna_mascota'
