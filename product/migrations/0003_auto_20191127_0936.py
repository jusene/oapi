# Generated by Django 2.2.7 on 2019-11-27 09:36

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20191126_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='product_picture',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='pictures/%Y%m%d', verbose_name='产品图片'),
        ),
    ]
