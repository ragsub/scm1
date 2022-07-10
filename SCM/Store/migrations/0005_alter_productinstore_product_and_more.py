# Generated by Django 4.0.4 on 2022-06-06 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_alter_product_options_alter_product_category_and_more'),
        ('Store', '0004_alter_productinstore_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstore',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Product.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='productinstore',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Store.store', verbose_name='Store'),
        ),
    ]