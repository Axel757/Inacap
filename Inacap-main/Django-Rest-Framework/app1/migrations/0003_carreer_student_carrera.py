# Generated by Django 4.2.7 on 2023-11-30 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carreer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('años', models.IntegerField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='carrera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.carreer'),
            preserve_default=False,
        ),
    ]