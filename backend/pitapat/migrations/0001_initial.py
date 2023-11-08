# Generated by Django 4.1.2 on 2023-11-08 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pitapat.models.custom_field.unsigned_auto_field
import pitapat.models.pitapat_user_manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("reg_dt", models.DateTimeField(auto_now_add=True)),
                ("reg_id", models.CharField(max_length=50)),
                ("upd_dt", models.DateTimeField(auto_now=True)),
                ("upd_id", models.CharField(max_length=50)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", pitapat.models.pitapat_user_manager.PitapatUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Chatroom",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("user_count", models.IntegerField()),
                ("reg_dt", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="College",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("reg_dt", models.DateTimeField(auto_now_add=True)),
                ("reg_id", models.CharField(max_length=50)),
                ("upd_dt", models.DateTimeField(auto_now=True)),
                ("upd_id", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("type", models.CharField(max_length=20)),
                ("reg_dt", models.DateTimeField(auto_now_add=True)),
                ("reg_id", models.CharField(max_length=50)),
                ("upd_dt", models.DateTimeField(auto_now=True)),
                ("upd_id", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="University",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("location", models.CharField(max_length=20)),
                ("email_domain", models.CharField(max_length=20)),
                ("reg_dt", models.DateTimeField(auto_now_add=True)),
                ("reg_id", models.CharField(max_length=50)),
                ("upd_dt", models.DateTimeField(auto_now=True)),
                ("upd_id", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name_plural": "Universities",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "baseuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("nickname", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=20, null=True)),
                ("status", models.CharField(max_length=1)),
                ("gender", models.CharField(max_length=1)),
                ("interested_gender", models.CharField(max_length=1)),
                ("birthday", models.DateField()),
            ],
            options={
                "abstract": False,
            },
            bases=("pitapat.baseuser",),
            managers=[
                ("objects", pitapat.models.pitapat_user_manager.PitapatUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Major",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("reg_dt", models.DateTimeField(auto_now_add=True)),
                ("reg_id", models.CharField(max_length=50)),
                ("upd_dt", models.DateTimeField(auto_now=True)),
                ("upd_id", models.CharField(max_length=50)),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="majors",
                        to="pitapat.college",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="college",
            name="university",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="colleges",
                to="pitapat.university",
            ),
        ),
        migrations.CreateModel(
            name="UserTag",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="pitapat.tag"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.RESTRICT, to="pitapat.user"
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "tag")},
            },
        ),
        migrations.CreateModel(
            name="UserChatroom",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "chatroom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pitapat.chatroom",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="pitapat.user"
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "chatroom")},
            },
        ),
        migrations.AddField(
            model_name="user",
            name="chatrooms",
            field=models.ManyToManyField(
                through="pitapat.UserChatroom", to="pitapat.chatroom"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="college",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="pitapat.college"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="major",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="pitapat.major"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="tags",
            field=models.ManyToManyField(through="pitapat.UserTag", to="pitapat.tag"),
        ),
        migrations.AddField(
            model_name="user",
            name="university",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="pitapat.university"
            ),
        ),
        migrations.CreateModel(
            name="Pitapat",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "is_from",
                    models.ForeignKey(
                        db_column="from",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="pitapat_sent",
                        to="pitapat.user",
                    ),
                ),
                (
                    "to",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="pitapat_received",
                        to="pitapat.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("name", models.ImageField(max_length=50, upload_to="")),
                ("path", models.CharField(max_length=256)),
                ("reg_dt", models.DateTimeField(auto_now_add=True)),
                ("reg_id", models.CharField(max_length=50)),
                ("upd_dt", models.DateTimeField(auto_now=True)),
                ("upd_id", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="pitapat.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Introduction",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("content", models.TextField()),
                ("reg_dt", models.DateTimeField(auto_now_add=True)),
                ("reg_id", models.CharField(max_length=50)),
                ("upd_dt", models.DateTimeField(auto_now=True)),
                ("upd_id", models.CharField(max_length=50)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="pitapat.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Chat",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("valid", models.CharField(max_length=1)),
                ("content", models.TextField()),
                ("reg_dt", models.DateTimeField(auto_now_add=True)),
                ("upd_dt", models.DateTimeField(auto_now=True)),
                (
                    "chatroom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chats",
                        to="pitapat.chatroom",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pitapat.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Block",
            fields=[
                (
                    "id",
                    pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "is_from",
                    models.ForeignKey(
                        db_column="from",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="block_sent",
                        to="pitapat.user",
                    ),
                ),
                (
                    "to",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="block_received",
                        to="pitapat.user",
                    ),
                ),
            ],
        ),
    ]
