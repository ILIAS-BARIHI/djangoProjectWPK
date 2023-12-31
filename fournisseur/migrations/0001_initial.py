# Generated by Django 4.2.3 on 2023-07-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('idFournisseur', models.AutoField(primary_key=True, serialize=False)),
                ('nomFournisseur', models.CharField(max_length=200)),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=15)),
            ],
        ),
    ]
