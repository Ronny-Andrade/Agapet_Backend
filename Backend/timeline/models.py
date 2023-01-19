from django.db import models
from user.models import User
from pet.models import Mascota

# Create your models here.
class Timeline(models.Model):
    opcion_estado = (
        ('A', 'Aprobado'),
        ('S', 'Suspendido'),
        ('E', 'Espera')
    )
    tipo_fase = (
        ('F', 'Formulario'),
        ('W', 'Entrevista por whatsapp'),
        ('V', 'Visita al domicilio'),
        ('C', 'Firma de contrato'),
        ('E', 'Entrega'),
        ('S', 'Seguimiento')
    )
    idtimline = models.AutoField(primary_key=True)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    idpet = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=1, choices=opcion_estado)
    tipo = models.CharField(max_length=1, choices=tipo_fase)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)

    def all_info_user(self):
        return '{}'.format(self.idtimline, self.iduser, self.idpet, self.descripcion, self.estado, self.tipo, self.fecha_inicio, self.fecha_final)

    def __str__(self):
        return self.all_info_user()
    
    class Meta:
        verbose_name='timeline'
        verbose_name_plural='timelines'
        db_table = 'timeline'