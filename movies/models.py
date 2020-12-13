from django.db import models

# Create your models here.


class Movie(models.Model):
    titleDistribution = models.CharField(verbose_name='Titulo de Distribucion',max_length=70)
    titleOriginal = models.CharField(verbose_name='Titulo Original',max_length=70)
    gender = models.CharField(verbose_name='Genero',max_length=30)
    languaje = models.CharField(verbose_name='Idioma',max_length=30)
    yearProducction = models.CharField(verbose_name='Año de Produccion',max_length=4)
    web = models.CharField(verbose_name='Direccion web',max_length=100)
    duration = models.TimeField(verbose_name='Duracion')
    score = models.CharField(verbose_name='Calificacion',max_length=10)
    premiereDate = models.DateField(verbose_name='Premier')
    description = models.CharField(verbose_name='Descripcion',max_length=600)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.titleOriginal,self.duration,self.description)

    class Meta:
        verbose_name='Pelicula'
        verbose_name_plural='Peliculas'


class Subtitle(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Pelicula')
    name = models.CharField(verbose_name='Nombre',max_length=40)
    nationality = models.CharField(verbose_name='Nacionalidad',max_length=30)

    def __str__(self):
        return "{0} -- {1} -- {2}".format(self.movie_id,self.name,self.nationality)

    class Meta:
        verbose_name='Subtitulo'
        verbose_name_plural='Subtitulos'


class DistributionData(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Pelicula')
    languajeSubtitle = models.CharField(verbose_name='Idioma del subtitulo',max_length=30)

    def __str__(self):
        return "{0} - {1}".format(self.movie_id,self.languajeSubtitle)

    class Meta:
        verbose_name='Datos del Reparto'


class DistributionMovie(models.Model):
    distributionData_id = models.ForeignKey(DistributionData, on_delete=models.CASCADE, verbose_name='Nombre del reparto')
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE,verbose_name='Pelicula')
    role = models.CharField(verbose_name='Rol', max_length=20)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.distributionData_id,self.movie_id,self.role)

    class Meta:
        verbose_name='Reparto por Pelicula'


class Cinema(models.Model):
    name = models.CharField(verbose_name='Nombre del Cine', max_length=100)
    address = models.CharField(verbose_name='Direccion', max_length=300)
    phone = models.CharField(verbose_name='Telefono', max_length=20)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name,self.address,self.phone)

    class Meta:
        verbose_name='Cine'
        verbose_name_plural='Cines'


class Room(models.Model):
    name = models.CharField(verbose_name='Nombre de la Sala', max_length=100)
    number = models.IntegerField(verbose_name='Numero')
    capacity = models.IntegerField(verbose_name='Capacidad')

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name,self.number,self.capacity)

    class Meta:
        verbose_name='Sala'
        verbose_name_plural='Salas'


class Function(models.Model):
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE,verbose_name='Pelicula')
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Sala')
    date = models.DateField(verbose_name='Fecha')
    time = models.TimeField(verbose_name='Duracion')

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.movie_id,self.room_id,self.date,self.time)

    class Meta:
        verbose_name='Funcion'
        verbose_name_plural='Funciones'


class Commentary(models.Model):
    function_id = models.ForeignKey(Function,on_delete=models.CASCADE,verbose_name='Funcion')
    personName = models.CharField(verbose_name='Nombre del cliente',max_length=100)
    age = models.CharField(verbose_name='Edad',max_length=2)
    date = models.DateField(verbose_name='Fecha')
    score = models.CharField(verbose_name='puntuacion',max_length=10)
    commentary = models.CharField(verbose_name='Comentario',max_length=500)

    def __str__(self):
        return "{0} - {1} - {2} - {3} - {4} - {5}".format(self.function_id,self.personName,self.age,self.date,self.score,self.commentary)

    class Meta:
        verbose_name='Opinion'
        verbose_name_plural='Opiniones'