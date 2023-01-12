from django.db import models
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Animal(models.Model):
    idanimal = models.AutoField(primary_key=True)
    tipoanimal = models.CharField(max_length=50)

    def info_completa(self):
        return "{}".format(self.idanimal,self.tipoanimal)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'animal'


# Create your models here.
class Mascota(models.Model):

    opcion_genero = (
        ('M', 'Macho'),
        ('H', 'Hembra'),
    )


    idpet = models.AutoField(primary_key=True)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    idanimal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=opcion_genero)
    estado = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/pet', blank=True, null=True)
    edad = models.PositiveIntegerField()
    peso = models.FloatField()
    comida = models.CharField(max_length=50)
    deportivo = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator (1)])
    jugueton = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator (1)])
    sociable = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator (1)])
    miedoso = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator (1)])
    # Esterelizado
    esterelizado = models.CharField(max_length=1)
    fecha_esterelizado = models.DateField(blank=True, null=True)
    lugar_esterelizado = models.CharField(max_length=100,blank=True, null=True)
    descripcion_esterelizado = models.CharField(max_length=200,blank=True, null=True)
    # Desparacitado
    desparacitado = models.CharField(max_length=1)
    fecha_desparacitado = models.DateField(blank=True, null=True)
    lugar_desparacitado = models.CharField(max_length=100,blank=True, null=True)
    descripcion_desparacitado = models.CharField(max_length=200,blank=True, null=True)

    def all_info_user(self):
        return '{}'.format(self.idpet,self.iduser, self.idanimal,self.nombre,self.genero,self.estado,self.descripcion,
        self.edad,self.peso, self.comida, self.deportivo, self.jugueton, self.sociable, self.miedoso, self.esterelizado,
        self.fecha_esterelizado, self.lugar_esterelizado, self.descripcion_esterelizado, self.desparacitado,
        self.fecha_desparacitado, self.lugar_desparacitado, self.descripcion_desparacitado)

    def __str__(self):
        return self.all_info_user()
    
    class Meta:
        verbose_name='Mascota'
        verbose_name_plural='Mascotas'
        db_table = 'mascota'




