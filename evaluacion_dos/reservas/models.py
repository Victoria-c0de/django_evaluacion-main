from django.db import models

# Create your models here.
class Reserva(models.Model):
    ESTADOS = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    )


    id = models.AutoField(primary_key=True)
    #el nombre no debe superar los 80 caracteres
    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=50)
    fecha_reserva = models.DateField()
    #hora de reserva
    hora_reserva = models.TimeField()
    #cantidad de personas debe estar en 1 y 15
    cantidad_personas = models.IntegerField()
    #validadcion de correo electronico
    
    correo = models.CharField(max_length=50)
    #estado de la reserva
    estado = models.CharField(max_length=20, choices=ESTADOS, default='RESERVADO')
    observacion = models.TextField(blank=True, null=True)

