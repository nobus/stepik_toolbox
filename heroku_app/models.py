from django.db import models
from django.core.exceptions import ValidationError

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    print(fieldfile_obj.file.image.height, fieldfile_obj.file.image.width)
    megabyte_limit = 5.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

class TheCat(models.Model):
    name = models.CharField(max_length=7)
    fluffy = models.BooleanField(default=True)
    avatar = models.ImageField(
        upload_to='avatars',
        height_field='height_field',
        width_field='width_field',
        validators=[validate_image]
    )
    #avatar = models.ImageField(upload_to='avatars')
    logo = models.ImageField()
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        print(*args)
        print(**kwargs)
        super(TheCat, self).save(*args,**kwargs)

    def delete(self, *args, **kwargs):
        """storage, path = self.avatar.storage, self.avatar.path
        print(path)
        storage.delete(path)"""
        super(TheCat, self).delete(*args,**kwargs)


class Mushroom(models.Model):
    name = models.CharField(max_length=13)
    size = models.PositiveIntegerField()
    poisonousness = models.BooleanField()


class Postcard(models.Model):
    address = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    compliment = models.CharField(max_length=128)
    date_of_delivery = models.DateField(auto_now=True)
    email = models.EmailField(max_length=254)
