# Generated by Django 4.1 on 2022-08-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_category_category_p_alter_category_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='title',
            field=models.CharField(blank=True, help_text='Choose the color of your product', max_length=100, null=True, unique=True, verbose_name='color'),
        ),
    ]
