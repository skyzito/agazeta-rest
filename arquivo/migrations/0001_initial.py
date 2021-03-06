# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-17 00:42
from __future__ import unicode_literals

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
            name='CardPlayed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=20)),
                ('turn_played', models.IntegerField()),
                ('is_spawned', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('match_id',),
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField(unique=True)),
                ('match_mode', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('blue_rank', models.IntegerField(blank=True, null=True)),
                ('blue_hero', models.CharField(max_length=30)),
                ('blue_deck', models.CharField(blank=True, max_length=80, null=True)),
                ('red_hero', models.CharField(blank=True, max_length=30)),
                ('red_deck', models.CharField(blank=True, max_length=80, null=True)),
                ('turns_played', models.IntegerField(blank=True, null=True)),
                ('red_starts', models.BooleanField()),
                ('blue_won', models.BooleanField()),
                ('blue_played_cards', models.ManyToManyField(related_name='_match_blue_played_cards_+', to='arquivo.CardPlayed')),
                ('red_played_cards', models.ManyToManyField(related_name='_match_red_played_cards_+', to='arquivo.CardPlayed')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('f', 'Free'), ('p', 'Paid'), ('d', 'Demo'), ('c', 'Consultant'), ('s', 'Staff')], default=('f', 'Free'), max_length=30)),
                ('avatar', models.IntegerField(blank=True)),
                ('partner_sub', models.BooleanField(default=True)),
                ('newsletter_sub', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TobToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('token', models.CharField(max_length=80)),
                ('server', models.CharField(choices=[('a', 'Americas'), ('e', 'Europa'), ('c', 'Asia')], default=('a', 'Americas'), max_length=10)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cardplayed',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arquivo.Match'),
        ),
        migrations.AlterUniqueTogether(
            name='tobtoken',
            unique_together=set([('username', 'token')]),
        ),
    ]
