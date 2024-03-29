# Generated by Django 2.2.4 on 2019-09-18 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_quizs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizs',
            options={'verbose_name_plural': 'Quizess'},
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('prompt', models.TextField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Quizs')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
