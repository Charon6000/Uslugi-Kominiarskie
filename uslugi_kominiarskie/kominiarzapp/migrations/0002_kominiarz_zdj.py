# Generated by Django 5.0.6 on 2024-05-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kominiarzapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kominiarz',
            name='zdj',
            field=models.CharField(default='https://scontent-waw2-1.cdninstagram.com/v/t51.2885-19/434052408_1404285370220069_8650032228286573407_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_cat=105&_nc_ohc=wc9crfMEzTMQ7kNvgEG0HUx&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AYC5wH2WLdZ05JZ1FsmWXDx297RTPW8ND5nMkEOoDhhjzQ&oe=664C1ACF&_nc_sid=8b3546', max_length=1000),
            preserve_default=False,
        ),
    ]
