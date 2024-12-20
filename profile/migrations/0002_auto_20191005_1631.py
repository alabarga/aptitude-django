# Generated by Django 2.2.5 on 2019-10-05 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='institucion',
            options={'verbose_name_plural': 'Instituciones'},
        ),
        migrations.AddField(
            model_name='profile',
            name='perfil',
            field=models.IntegerField(blank=True, choices=[(0, 'enfermera especialista en geriatria'), (1, 'enfermera otros'), (2, 'médico general'), (3, 'equipo multidisciplinar'), (4, 'médico residente'), (5, 'otros')], null=True, verbose_name='Perfil profesional'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='institucion',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.DO_NOTHING, to='profile.Institucion'),
        ),
    ]
