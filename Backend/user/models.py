from django.db import models

# Create your models here.
class User(models.Model):
    user_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=100,unique=True)
    direction = models.CharField(max_length=200)
    phone = models.CharField(max_length=45)
    age = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/user', null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone','password']

    def all_info_user(self):
        return '{}'.format(self.user_id, self.name, self.email,self.direction,self.phone,self.age,self.points,self.image)

    def __str__(self):
        return self.all_info_user()
    
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
        db_table = 'user'