from django.contrib.gis.db import models

class EmployeeInfo(models.Model):
    employee = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Çalışan")
    current_location = models.PointField(verbose_name="Anlık Konumu")
    home_location = models.PointField(verbose_name="Ev Konumu")
    field = models.ForeignKey("employees.Field",verbose_name="Çalıştığı Bölge",on_delete=models.NOT_PROVIDED)
    salary = models.IntegerField(verbose_name="Maaşı")

    def __str__(self):
        return self.employee.username

class Field(models.Model):
    name = models.TextField(verbose_name="Bölge Adı")
    line = models.LineStringField(verbose_name="Bölge")

    def __str__(self):
        return self.name
