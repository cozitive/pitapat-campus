# Generated by Django 4.1.2 on 2022-12-07 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pitapat.models.custom_field.unsigned_auto_field
import pitapat.models.pitapat_user_manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='user_key', primary_key=True, serialize=False)),
                ('nickname', models.CharField(db_column='nickname', max_length=30, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(max_length=1)),
                ('gender', models.CharField(max_length=1)),
                ('interested_gender', models.CharField(max_length=1)),
                ('birthday', models.DateField()),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('reg_id', models.CharField(max_length=50)),
                ('upd_dt', models.DateTimeField(auto_now=True)),
                ('upd_id', models.CharField(max_length=50)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'User',
                'db_table': 'E_User',
                'managed': True,
            },
            managers=[
                ('objects', pitapat.models.pitapat_user_manager.PitapatUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='chatroom_key', primary_key=True, serialize=False)),
                ('user_count', models.IntegerField(db_column='user_count')),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'E_Chatroom',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='college_key', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='college_name', max_length=20)),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('reg_id', models.CharField(max_length=50)),
                ('upd_dt', models.DateTimeField(auto_now=True)),
                ('upd_id', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'College',
                'db_table': 'E_College',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='tag_key', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tag_name', max_length=20)),
                ('type', models.CharField(db_column='tag_type', max_length=20)),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('reg_id', models.CharField(max_length=50)),
                ('upd_dt', models.DateTimeField(auto_now=True)),
                ('upd_id', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tag',
                'db_table': 'E_Tag',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='university_key', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='university_name', max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('email_domain', models.CharField(max_length=20)),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('reg_id', models.CharField(max_length=50)),
                ('upd_dt', models.DateTimeField(auto_now=True)),
                ('upd_id', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'Universities',
                'db_table': 'E_University',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserTag',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='user_tag_key', primary_key=True, serialize=False)),
                ('tag', models.ForeignKey(db_column='tag_key', on_delete=django.db.models.deletion.RESTRICT, to='pitapat.tag')),
                ('user', models.OneToOneField(db_column='user_key', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User-Tag Relationship',
                'db_table': 'R_UserTag',
                'managed': True,
                'unique_together': {('user', 'tag')},
            },
        ),
        migrations.CreateModel(
            name='UserChatroom',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='user_chatroom_key', primary_key=True, serialize=False)),
                ('chatroom', models.ForeignKey(db_column='chatroom_key', on_delete=django.db.models.deletion.CASCADE, to='pitapat.chatroom')),
                ('user', models.OneToOneField(db_column='user_key', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User-Chatroom Relationship',
                'db_table': 'R_UserChatroom',
                'managed': True,
                'unique_together': {('user', 'chatroom')},
            },
        ),
        migrations.CreateModel(
            name='Pitapat',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='pitapat_key', primary_key=True, serialize=False)),
                ('is_from', models.ForeignKey(db_column='from', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pitapat_sent', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(db_column='to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pitapat_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'pitapat',
                'db_table': 'R_Pitapat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='photo_key', primary_key=True, serialize=False)),
                ('name', models.ImageField(db_column='photo_name', max_length=50, upload_to='')),
                ('path', models.CharField(max_length=256)),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('reg_id', models.CharField(max_length=50)),
                ('upd_dt', models.DateTimeField(auto_now=True)),
                ('upd_id', models.CharField(max_length=50)),
                ('user', models.ForeignKey(db_column='user_key', on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Photo',
                'db_table': 'E_Photo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='major_key', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='major_name', max_length=20)),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('reg_id', models.CharField(max_length=50)),
                ('upd_dt', models.DateTimeField(auto_now=True)),
                ('upd_id', models.CharField(max_length=50)),
                ('college', models.ForeignKey(db_column='college_key', on_delete=django.db.models.deletion.RESTRICT, related_name='majors', to='pitapat.college')),
            ],
            options={
                'verbose_name': 'Major',
                'db_table': 'E_Major',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='introduction_key', primary_key=True, serialize=False)),
                ('content', models.TextField(db_column='content')),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('reg_id', models.CharField(max_length=50)),
                ('upd_dt', models.DateTimeField(auto_now=True)),
                ('upd_id', models.CharField(max_length=50)),
                ('user', models.OneToOneField(db_column='user_key', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Introduction',
                'db_table': 'E_Introduction',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='college',
            name='university',
            field=models.ForeignKey(db_column='university_key', on_delete=django.db.models.deletion.RESTRICT, related_name='colleges', to='pitapat.university'),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='chat_key', primary_key=True, serialize=False)),
                ('valid', models.CharField(max_length=1)),
                ('content', models.TextField()),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('upd_dt', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(db_column='from', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_chats', to=settings.AUTH_USER_MODEL)),
                ('chatroom', models.ForeignKey(db_column='chatroom_key', on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='pitapat.chatroom')),
            ],
            options={
                'db_table': 'E_Chat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('key', pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(db_column='block_key', primary_key=True, serialize=False)),
                ('is_from', models.ForeignKey(db_column='from', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='block_sent', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(db_column='to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='block_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'block',
                'db_table': 'R_Block',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='chatrooms',
            field=models.ManyToManyField(through='pitapat.UserChatroom', to='pitapat.chatroom'),
        ),
        migrations.AddField(
            model_name='user',
            name='college',
            field=models.ForeignKey(db_column='college_key', on_delete=django.db.models.deletion.RESTRICT, to='pitapat.college'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.ForeignKey(db_column='major_key', on_delete=django.db.models.deletion.RESTRICT, to='pitapat.major'),
        ),
        migrations.AddField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(through='pitapat.UserTag', to='pitapat.tag'),
        ),
        migrations.AddField(
            model_name='user',
            name='university',
            field=models.ForeignKey(db_column='university_key', on_delete=django.db.models.deletion.RESTRICT, to='pitapat.university'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]