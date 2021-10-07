from django.db import models
import csv

class SanctionMain(models.Model):
    ent_num = models.PositiveIntegerField(primary_key=True, verbose_name='제재번호')
    sdn_name = models.TextField()
    sdn_type = models.CharField(max_length=20)
    program = models.TextField()
    title = models.TextField()
    call_sign = models.CharField(max_length=20)
    vess_type = models.TextField()
    tonnage = models.CharField(max_length=20)
    grt = models.CharField(max_length=10)
    vess_flag = models.CharField(max_length=50)
    vess_owner = models.CharField(max_length=200)
    remarks = models.TextField()
    is_sdn = models.CharField(max_length=2)

    def __str__(self):
        return self.sdn_name

    class Meta:
        db_table = 'sanction_main'


class SanctionAdd(models.Model):
    ent_num = models.PositiveIntegerField()
    add_num = models.PositiveIntegerField(primary_key=True)
    address = models.TextField()
    address_more = models.TextField()
    country = models.TextField()
    add_remarks = models.TextField()

    class Meta:
        db_table = 'sanction_add'

class SanctionAlt(models.Model):
    ent_num = models.PositiveIntegerField()
    alt_num = models.PositiveIntegerField(primary_key=True)
    alt_type = models.TextField()
    alt_remarks = models.TextField()

    class Meta:
        db_table = 'sanction_alt'
