# Generated by Django 3.1.1 on 2022-05-16 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CityName', models.CharField(max_length=100, null=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=150, null=True)),
                ('Email', models.CharField(max_length=100, null=True)),
                ('Phone', models.CharField(max_length=15, null=True)),
                ('Message', models.CharField(max_length=250, null=True)),
                ('EnquiryDate', models.DateTimeField(auto_now_add=True)),
                ('IsRead', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MobileNumber', models.CharField(max_length=100, null=True)),
                ('RegDate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodId', models.CharField(max_length=150, null=True)),
                ('FoodItems', models.CharField(max_length=250, null=True)),
                ('Description', models.CharField(max_length=300, null=True)),
                ('PickupDate', models.DateField(null=True)),
                ('PickupAddress', models.CharField(max_length=250, null=True)),
                ('ContactPerson', models.CharField(max_length=150, null=True)),
                ('CPMobNumber', models.CharField(max_length=15, null=True)),
                ('Image', models.FileField(blank=True, null=True, upload_to='')),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodwaste.city')),
                ('donorid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodwaste.donor')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StateName', models.CharField(max_length=100, null=True)),
                ('RegDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Foodrequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestNumber', models.CharField(max_length=150, null=True)),
                ('fullName', models.CharField(max_length=250, null=True)),
                ('mobileNumber', models.CharField(max_length=15, null=True)),
                ('message', models.CharField(max_length=350, null=True)),
                ('requestDate', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('donorRemark', models.CharField(max_length=250, null=True)),
                ('requestCompletionDate', models.DateField(null=True)),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodwaste.food')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodwaste.state'),
        ),
    ]