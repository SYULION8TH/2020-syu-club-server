# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ClubTypes(models.Model):
    club_type_id = models.AutoField(primary_key=True)
    club_type_name = models.IntegerField(blank=True, null=True)
    club_type_desc = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'club_types'


class Clubs(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=200, blank=True, null=True)
    club_desc = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    club_type = models.ForeignKey(ClubTypes, models.DO_NOTHING, null=True)
    club_img_url = models.ImageField(upload_to="%Y/%m/%d", null=True)
    club_logo_url = models.CharField(max_length=1000, blank=True, null=True)
    established = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'clubs'


class ClubsMember(models.Model):
    club_member_id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Clubs, models.DO_NOTHING, blank=True, null=True)
    club_member_name = models.CharField(max_length=200, blank=True, null=True)
    club_member_img_url = models.CharField(max_length=1000, blank=True, null=True)
    club_member_position = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clubs_member'


class ClubsQna(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=150, blank=True, null=True)
    question_content = models.CharField(max_length=3000, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    club = models.ForeignKey(Clubs, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clubs_qna'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=150)
    post_content = models.CharField(max_length=3000)
    post_introduce = models.CharField(max_length=200, blank=True, null=True)
    post_img_url = models.CharField(max_length=1500, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)  # This field type is a guess.
    club = models.ForeignKey(Clubs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class PostsReplies(models.Model):
    post_reply_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey(Posts, models.DO_NOTHING, blank=True, null=True)
    parent_reply = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    post_reply_content = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0) 

    class Meta:
        managed = False
        db_table = 'posts_replies'


class PostsViews(models.Model):
    post = models.ForeignKey(Posts, models.DO_NOTHING, null=True)
    views_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    user_ip = models.IntegerField(blank=True, null=True)
    checked_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts_views'


class QnaReplies(models.Model):
    qna_reply_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(ClubsQna, models.DO_NOTHING, blank=True, null=True)
    parent_reply = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    qna_reply_content = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    is_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qna_replies'


class RelInterestClub(models.Model):
    interest_club_id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Clubs, models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, null=True, related_name='interest_club')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'rel_interest_club'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField(auto_now_add=True)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class UsersAdditionalInfo(models.Model):
    user_info = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    profile = models.CharField(max_length=5000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users_additional_info'


class PostsLike(models.Model):
    posts_like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False

@receiver(signals.post_save, sender=SocialAccount)
def create_addtional_user_info(sender, instance, created, **kwargs):
    if created:
        UsersAdditionalInfo.objects.create(user_info=instance.user, profile= instance.get_avatar_url())