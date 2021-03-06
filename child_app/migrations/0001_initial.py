# Generated by Django 3.2.8 on 2021-11-04 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('_name', models.CharField(max_length=50)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('studyLevel', models.PositiveIntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='storage/images')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('_name', models.CharField(max_length=50)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='storage/images')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('attitude', models.FloatField()),
                ('childplaces', models.ManyToManyField(to='child_app.Child')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='idParent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='child_app.parent'),
        ),
    ]
