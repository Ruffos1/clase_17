from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    "Esto se usa para que nos devuelvan el tipo de datos que queremos en cada variable de clase, Charfield s campo de texto por ejemplo"
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True)
    "Este NULL=TRUE sirve para saber que este dato es opcional"
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    "Este es un tipo de ato FK, lo recibiria como lo quisimos en su modelo local, Y el on delete sirve que para cuando esta FK se borre en su formato local nos salte Null el cliente a lque se le atribuyo"
    def __str__(self):
        return f"{self.nombre } {self.apellido}"
