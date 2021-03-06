# Generated by Django 3.2.6 on 2022-06-04 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_zakattable_zakatdue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakattable',
            name='AmtVal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='zakattable',
            name='ZakatDue',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='zakattable',
            name='ZakatRate',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='zakattable',
            name='category',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='zakattable',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
