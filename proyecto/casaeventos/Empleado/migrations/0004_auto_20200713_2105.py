# Generated by Django 3.0.8 on 2020-07-14 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empleado', '0003_evento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='telefono',
            new_name='presupuesto',
        ),
    ]
