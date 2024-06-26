# Generated by Django 5.0.4 on 2024-05-06 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0004_alter_product_details_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMst',
            fields=[
                ('p_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('model', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_module.productmst')),
            ],
        ),
    ]
