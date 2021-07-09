# Generated by Django 3.2.4 on 2021-07-08 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desarrollador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_desarrollador', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('categoria', models.CharField(max_length=50)),
                ('fecha_lanzamiento', models.DateField()),
                ('desarrollador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.desarrollador')),
            ],
        ),
    ]
