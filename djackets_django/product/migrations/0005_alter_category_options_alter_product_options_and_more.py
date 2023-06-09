# Generated by Django 4.2 on 2023-04-27 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-date_added',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты товаров'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(verbose_name='слаг'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='миниатюра'),
        ),
    ]
