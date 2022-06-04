# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccData(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(unique=True, max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'acc_data'


class Admin(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(primary_key=True, max_length=50)
    dept_num = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_num', blank=True, null=True)
    email = models.ForeignKey(AccData, models.DO_NOTHING, db_column='email', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class App1Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=140)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app1_post'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Casedetail(models.Model):
    case_num = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    time_served = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'casedetail'


class Department(models.Model):
    dept_num = models.DecimalField(primary_key=True, max_digits=25, decimal_places=0)
    dept_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Offenders(models.Model):
    ssn = models.DecimalField(primary_key=True, max_digits=13, decimal_places=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    house_num = models.CharField(max_length=50)
    street_num = models.CharField(max_length=50, blank=True, null=True)
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    reg_no = models.DecimalField(unique=True, max_digits=10, decimal_places=0)
    case_n = models.ForeignKey(Casedetail, models.DO_NOTHING, db_column='case_n', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offenders'


class ThumbnailKvstore(models.Model):
    key = models.CharField(primary_key=True, max_length=200)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'thumbnail_kvstore'


class Users(models.Model):
    ssn = models.DecimalField(primary_key=True, max_digits=13, decimal_places=0)
    email = models.ForeignKey(AccData, models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'users'
