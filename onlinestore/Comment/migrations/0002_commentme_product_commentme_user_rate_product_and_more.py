# Generated by Django 4.0.6 on 2022-07-17 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0002_category_category_p_details_pro_id_and_more'),
        ('Comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentme',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commenttoproduct', to='Products.product', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='commentme',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commenttouser', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='rate',
            name='product',
            field=models.ManyToManyField(to='Products.product'),
        ),
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratetocustomer', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
