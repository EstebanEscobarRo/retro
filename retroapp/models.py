from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genero(models.Model):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Juego(models.Model):

    title=models.CharField(max_length=200)
    empresa=models.ForeignKey('Empresa', on_delete=models.SET_NULL, null=True)

    summary=models.TextField(max_length=1000)
    isbn=models.CharField('ISBN', max_length=13)
    genero=models.ManyToManyField(Genero)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this game"""
        return reverse('juego-detail', args=[str(self.id)])

class JuegoInstance(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    juego=models.ForeignKey('Juego', on_delete=models.SET_NULL, null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('r', 'RPG'),
        ('v', 'Visual Novel'),
        ('a', 'Accion'),
        ('m', 'Multijugador')
    )

    status=models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Game availability'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.juego.title})'

class Empresa(models.Model):
    """Model representing an Empresa."""
    emp_name=models.CharField(max_length=100)
    edi_name=models.CharField(max_length=100)
    date_of_update=models.DateField(null=True, blank=True)
    last_update=models.DateField('Updated', null=True, blank=True)

    class Meta:
        ordering = ['edi_name', 'emp_name']

    def get_absolute_url(self):
        return reverse('empresa-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.edi_name}, {self.emp_name}'