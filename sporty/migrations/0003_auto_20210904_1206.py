# Generated by Django 3.1.5 on 2021-09-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sporty', '0002_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='star',
            name='match',
            field=models.IntegerField(default=69),
        ),
    ]