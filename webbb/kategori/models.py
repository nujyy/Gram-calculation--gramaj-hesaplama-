from django.db import models

# Create your models here.
class Kategori(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Besin(models.Model):
    name=models.CharField(max_length=30)
    protein=models.DecimalField(max_digits=10,decimal_places=3)
    yağ=models.DecimalField(max_digits=10,decimal_places=3)
    karbonhidrat=models.DecimalField(max_digits=10,decimal_places=3)
    gram=models.DecimalField(max_digits=10,decimal_places=3)
    kalori=models.DecimalField(max_digits=10,decimal_places=3)
    kategori = models.ForeignKey(Kategori, on_delete=models.DO_NOTHING, related_name='besinler')

    def __str__(self):
        return self.name