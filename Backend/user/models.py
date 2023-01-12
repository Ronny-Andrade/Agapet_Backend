from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    iduser= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=100,unique=True)
    direction = models.CharField(max_length=200,  blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    age = models.PositiveIntegerField( blank=True, null=True)
    points = models.PositiveIntegerField( blank=True, null=True)
    image = models.ImageField(upload_to='media/user', blank=True,null=True)
    imagen64 = models.TextField(blank=True, null=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def all_info_user(self):
        return '{}'.format(self.iduser, self.name, self.email,self.direction,self.phone,self.age,self.points,self.image, self.imagen64)

    def __str__(self):
        return self.all_info_user()
    
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
        db_table = 'user'