from django.db import models

# Create your models here.
class Rol_User(models.Model):
    rol_id= models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    def all_info_rol(self):
        return '{}'.format(self.rol_id,self.description)
    
    def __str__(self):
        return self.all_info_rol()

    class Meta:
        verbose_name='Rol_User'
        verbose_name_plural='Rol_Users'
        db_table = 'rol_user'

    

class User(models.Model):
    user_id= models.AutoField(primary_key=True)
    rol_id = models.ForeignKey(Rol_User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=100,unique=True)
    direction = models.CharField(max_length=200)
    phone = models.CharField(max_length=45)
    age = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone','password']

    def all_info_user(self):
        return '{}'.format(self.user_id, self.name, self.email,self.direction,self.phone,self.age,self.points)

    def __str__(self):
        return self.all_info_user()
    
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
        db_table = 'user'
    


