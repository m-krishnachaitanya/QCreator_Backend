# Generated by Django 3.2.8 on 2021-11-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('questionid', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('quizid', models.CharField(max_length=10)),
                ('question', models.CharField(max_length=2048)),
                ('option1', models.CharField(max_length=2048)),
                ('option2', models.CharField(max_length=2048)),
                ('option3', models.CharField(max_length=2048)),
                ('option4', models.CharField(max_length=2048)),
                ('answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quizes',
            fields=[
                ('quizid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]