# Generated by Django 5.1.5 on 2025-02-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_bn',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_hi',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
