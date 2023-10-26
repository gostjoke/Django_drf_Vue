# Generated by Django 4.1.3 on 2023-10-26 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Author')),
                ('age', models.IntegerField(verbose_name='Age')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Publisher')),
                ('email', models.EmailField(max_length=254, verbose_name='Publisher Email')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Book Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('pub_date', models.DateField(verbose_name='Publish Date')),
                ('bread', models.IntegerField(verbose_name='Read')),
                ('bcomments', models.IntegerField(verbose_name='Comment')),
                ('authors', models.ManyToManyField(to='viewApp.author', verbose_name='Author')),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewApp.publish', verbose_name='Publisher')),
            ],
        ),
    ]