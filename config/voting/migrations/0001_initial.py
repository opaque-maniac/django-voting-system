# Generated by Django 4.2.7 on 2023-12-18 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='candidate_images/')),
                ('vote_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'candidate',
                'verbose_name_plural': 'candidates',
            },
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('has_ended', models.BooleanField(default=False)),
                ('vote_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'election',
                'verbose_name_plural': 'elections',
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='party_images/')),
            ],
            options={
                'verbose_name': 'party',
                'verbose_name_plural': 'parties',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.candidate')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.election')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
            options={
                'verbose_name': 'vote',
                'verbose_name_plural': 'votes',
            },
        ),
        migrations.AddField(
            model_name='candidate',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.election'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.party'),
        ),
    ]
