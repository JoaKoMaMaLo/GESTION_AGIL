from django.db import models

# Create your models here.

class Usuario(models.Model):
    n_usuario     = models.CharField(max_length=20)
    contrasena  = models.CharField(max_length=15)
    def __str__(self):
        return str(self.n_usuario)
    

class Inventario(models.Model):
    id_prod = models.IntegerField(primary_key=True)
    nombre_prod = models.CharField(max_length=50)
    fecha_venc = models.DateField()
    stock = models.IntegerField()
    id_categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria', null=True)

    def __str__(self):
        return str(self.id_prod, self.nombre_prod, self.fecha_venc, self.stock, self.id_categoria) 

class Etiqueta(models.Model):
    id_etiqueta = models.AutoField(primary_key=True)
    nombre_etiqueta = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_etiqueta

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    nombre_ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_ubicacion

class Pieza(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    nombre_pieza = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    descripcion_pieza = models.TextField()
    cantidad_pieza = models.PositiveIntegerField()
    cantidad_minima_pieza = models.PositiveIntegerField()
    fecha_vencimiento = models.DateField(blank=True, null=True)
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    id_etiqueta = models.ForeignKey(Etiqueta, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre_pieza

class Kit(models.Model):
    id_kit = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Kit {self.id_kit}"

class Conjunto(models.Model):
    id_conjunto = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Conjunto {self.id_conjunto}"

class PiezaKit(models.Model):
    id_kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    id_pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_pieza.nombre_pieza} en {self.id_kit}"

class PiezaConjunto(models.Model):
    id_conjunto = models.ForeignKey(Conjunto, on_delete=models.CASCADE)
    id_pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_pieza.nombre_pieza} en {self.id_conjunto}"
