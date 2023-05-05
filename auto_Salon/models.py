from django.db  import models

class Car(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['name']


class Stamp(models.Model):
    name = models.CharField(max_length=50, verbose_name='Модель')
    descreption = models.TextField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        ordering = ['name']


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Страна')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name']

    
class Releasedate(models.Model):
    releasedate = models.CharField(max_length=100, verbose_name='Дата выпуска')

    def __str__(self) -> str:
        return str(self.releasedate)
    
    class Meta:
        verbose_name = 'Дата выпуска'
        verbose_name_plural = 'Даты выпуска'
        ordering = ['releasedate']


class Fuel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Топливо')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Топливо'
        verbose_name_plural = 'Топливы'
        ordering = ['name']

class Typeofcar(models.Model):
    name = models.CharField(max_length=50, verbose_name='Типы автобиля')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Типы автомобиля'
        verbose_name_plural = 'Типы автомобилей'
        ordering = ['name']


class Create(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    stamp = models.ForeignKey(Stamp, on_delete=models.CASCADE, verbose_name='Модель')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')
    releasedate = models.ForeignKey(Releasedate, on_delete=models.CASCADE, verbose_name='Дата выпуска')
    price = models.CharField(max_length=100, verbose_name='Цена')
    specifications = models.TextField(max_length=10000, verbose_name='Характеристики')
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, verbose_name='Топливо')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    typeofcar = models.ForeignKey(Typeofcar, on_delete=models.CASCADE, verbose_name='Типы автомобилей')
    image = models.ImageField(upload_to='photos/', verbose_name='Фото', blank=True)

    # def __str__(self):
    #     return f'{self.car} - {self.stamp} ({self.releasedate})'
    
    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'Создание манины'
        verbose_name_plural = 'Создание машиней'
        ordering = ['car']