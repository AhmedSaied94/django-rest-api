# Generated by Django 3.2.9 on 2021-11-12 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Catigorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('plot', models.TextField(null=True)),
                ('relased', models.DateField(null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='entertainment/series/images')),
                ('casts', models.ManyToManyField(to='entertainment.Cast')),
                ('catigories', models.ManyToManyField(to='entertainment.Catigorie')),
            ],
            options={
                'verbose_name_plural': 'Serieses',
                'ordering': ['-relased'],
            },
        ),
        migrations.CreateModel(
            name='Seisson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('plot', models.TextField(null=True)),
                ('relased', models.DateField(null=True)),
                ('casts', models.ManyToManyField(to='entertainment.Cast')),
                ('catigories', models.ManyToManyField(to='entertainment.Catigorie')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_title', to='entertainment.series')),
            ],
            options={
                'verbose_name_plural': 'Seissons',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('plot', models.TextField(null=True)),
                ('relased', models.DateField(null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='entertainment/movies/images')),
                ('run_time', models.IntegerField(null=True)),
                ('casts', models.ManyToManyField(to='entertainment.Cast')),
                ('catigories', models.ManyToManyField(to='entertainment.Catigorie')),
            ],
            options={
                'ordering': ['-relased'],
            },
        ),
        migrations.CreateModel(
            name='Eposides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('plot', models.TextField(null=True)),
                ('relased', models.DateField(null=True)),
                ('runtime', models.IntegerField()),
                ('casts', models.ManyToManyField(to='entertainment.Cast')),
                ('catigories', models.ManyToManyField(to='entertainment.Catigorie')),
                ('seisson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seisson_title', to='entertainment.seisson')),
            ],
            options={
                'verbose_name_plural': 'Eposides',
            },
        ),
    ]
