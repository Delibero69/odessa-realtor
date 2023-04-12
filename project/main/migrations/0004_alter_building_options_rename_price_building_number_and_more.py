# Generated by Django 4.2 on 2023-04-13 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_title_building_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.RenameField(
            model_name='building',
            old_name='price',
            new_name='number',
        ),
        migrations.AddField(
            model_name='building',
            name='ochered',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='building',
            name='price_za_kvadrat',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='building',
            name='sdacha_sekcii',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='building',
            name='total_price',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='building',
            name='zabronirivat',
            field=models.BooleanField(default=False),
        ),
    ]
