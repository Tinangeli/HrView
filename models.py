# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Courses(models.Model):
    course_name = models.CharField(max_length=255, blank=True, null=True)
    course_slug = models.CharField(max_length=255, blank=True, null=True)
    course_code = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'


class DeanProfessor(models.Model):
    dean = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    professor = models.ForeignKey('Users', models.DO_NOTHING, related_name='deanprofessor_professor_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dean_professor'


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


class Evaluation(models.Model):
    evaluation_name = models.CharField(max_length=255, blank=True, null=True)
    categories = models.ForeignKey('StudentCategories', models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    schedule = models.ForeignKey('Schedules', models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    instructor_categories = models.ForeignKey('InstructorCategories', models.DO_NOTHING, blank=True, null=True)
    student_categories = models.ForeignKey('StudentCategories', models.DO_NOTHING, related_name='evaluation_student_categories_set', blank=True, null=True)
    comments = models.ForeignKey('EvaluationComments', on_delete=models.CASCADE, related_name="evaluation_comments")  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'evaluation'


class EvaluationComments(models.Model):
    evaluation = models.ForeignKey(Evaluation, models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluation_comments'


class EvaluationMarks(models.Model):
    evaluation = models.ForeignKey(Evaluation, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('StudentCategories', models.DO_NOTHING, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluation_marks'


class InstructorCategories(models.Model):
    overall_lecture = models.IntegerField(blank=True, null=True)
    overall_realtime_writing = models.IntegerField(blank=True, null=True)
    overall_moving_guiding = models.IntegerField(blank=True, null=True)
    overall_answer_student_question = models.IntegerField(blank=True, null=True)
    overall_pose_question = models.IntegerField(blank=True, null=True)
    overall_follow_up_question = models.IntegerField(blank=True, null=True)
    overall_individual_discussion = models.IntegerField(blank=True, null=True)
    overall_demonstrate_video = models.IntegerField(blank=True, null=True)
    overall_administrative_task = models.IntegerField(blank=True, null=True)
    overall_waiting = models.IntegerField(blank=True, null=True)
    overall_other = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor_categories'


class ModelHasPermissions(models.Model):
    permission = models.ForeignKey('Permissions', models.DO_NOTHING, blank=True, null=True)
    model_type = models.CharField(max_length=255, blank=True, null=True)
    model = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_has_permissions'


class ModelHasRoles(models.Model):
    role = models.ForeignKey('Roles', models.DO_NOTHING, blank=True, null=True)
    model_type = models.CharField(max_length=255, blank=True, null=True)
    model = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_has_roles'


class Permissions(models.Model):
    permission_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class RoleHasPermissions(models.Model):
    role = models.ForeignKey('Roles', models.DO_NOTHING, blank=True, null=True)
    permission = models.ForeignKey(Permissions, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'


class Roles(models.Model):
    role_name = models.CharField(max_length=255, blank=True, null=True)
    guard_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Rooms(models.Model):
    room = models.CharField(max_length=255, blank=True, null=True)
    room_slug = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'


class Schedules(models.Model):
    course = models.ForeignKey(Courses, models.DO_NOTHING, blank=True, null=True)
    professor = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, blank=True, null=True)
    room = models.ForeignKey(Rooms, models.DO_NOTHING, blank=True, null=True)
    schedule = models.CharField(max_length=255, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    semester = models.CharField(max_length=255, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedules'


class StudentCategories(models.Model):
    overall_listening = models.IntegerField(blank=True, null=True)
    overall_individual_thinking = models.IntegerField(blank=True, null=True)
    overall_group_activity = models.IntegerField(blank=True, null=True)
    overall_answer_question = models.IntegerField(blank=True, null=True)
    overall_ask_question = models.IntegerField(blank=True, null=True)
    overall_whole_class_discussion = models.IntegerField(blank=True, null=True)
    overall_student_presentation = models.IntegerField(blank=True, null=True)
    overall_test = models.IntegerField(blank=True, null=True)
    overall_waiting = models.IntegerField(blank=True, null=True)
    overall_other = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_categories'


class Subjects(models.Model):
    subject_name = models.CharField(max_length=255, blank=True, null=True)
    subject_slug = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjects'


class TeachingLoad(models.Model):
    users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    schedules = models.ForeignKey(Schedules, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teaching_load'


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

# Create your models here.
