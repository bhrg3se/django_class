# Generated by Django 2.2.2 on 2019-07-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Anonymous', max_length=5)),
                ('content', models.TextField()),
            ],
        ),
    ]
