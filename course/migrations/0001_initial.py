# Generated by Django 3.0.1 on 2019-12-25 19:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "course_id",
                    models.CharField(
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Course id",
                    ),
                ),
                (
                    "course_title",
                    models.CharField(
                        max_length=200, verbose_name="Course title"
                    ),
                ),
                (
                    "course_overview",
                    models.TextField(
                        blank=True, null=True, verbose_name="Course overview"
                    ),
                ),
                (
                    "course_outcome",
                    models.TextField(
                        blank=True, null=True, verbose_name="Course outcome"
                    ),
                ),
                (
                    "course_objective",
                    models.TextField(
                        blank=True, null=True, verbose_name="Course objective"
                    ),
                ),
                (
                    "course_credit",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=4,
                        verbose_name="Course credit",
                    ),
                ),
                (
                    "lecture_contact_hours_per_week",
                    models.DecimalField(decimal_places=2, max_digits=4),
                ),
                (
                    "tutorial_contact_hours_per_week",
                    models.DecimalField(decimal_places=2, max_digits=4),
                ),
                (
                    "practical_contact_hours_per_week",
                    models.DecimalField(decimal_places=2, max_digits=4),
                ),
                (
                    "course_resources",
                    models.TextField(
                        blank=True, null=True, verbose_name="Course resources"
                    ),
                ),
                (
                    "course_test",
                    models.TextField(
                        blank=True, null=True, verbose_name="Course test"
                    ),
                ),
            ],
            options={
                "verbose_name": "Course",
                "verbose_name_plural": "Courses",
            },
        ),
        migrations.CreateModel(
            name="Institute",
            fields=[
                (
                    "institute_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Institute id",
                    ),
                ),
                (
                    "institute_name",
                    models.CharField(
                        max_length=300, verbose_name="Institute name"
                    ),
                ),
            ],
            options={
                "verbose_name": "Institute",
                "verbose_name_plural": "Institutes",
            },
        ),
        migrations.CreateModel(
            name="Level",
            fields=[
                (
                    "level_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Level id",
                    ),
                ),
                (
                    "level_name",
                    models.CharField(max_length=50, verbose_name="Level name"),
                ),
                (
                    "institute",
                    models.ManyToManyField(
                        blank=True,
                        to="course.Institute",
                        verbose_name="Institutes",
                    ),
                ),
            ],
            options={"verbose_name": "Level", "verbose_name_plural": "Levels",},
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                (
                    "module_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Module id",
                    ),
                ),
                (
                    "module_title",
                    models.CharField(
                        max_length=200, verbose_name="Module title"
                    ),
                ),
                (
                    "module_overview",
                    models.TextField(
                        blank=True, null=True, verbose_name="Module overview"
                    ),
                ),
                (
                    "module_outcome",
                    models.TextField(
                        blank=True, null=True, verbose_name="Module outcome"
                    ),
                ),
                (
                    "module_objective",
                    models.TextField(
                        blank=True, null=True, verbose_name="Module objective"
                    ),
                ),
                (
                    "module_body",
                    models.TextField(
                        blank=True, null=True, verbose_name="Module body"
                    ),
                ),
                (
                    "module_resources",
                    models.TextField(
                        blank=True, null=True, verbose_name="Module resources"
                    ),
                ),
                (
                    "module_test",
                    models.TextField(
                        blank=True, null=True, verbose_name="Module test"
                    ),
                ),
                (
                    "course",
                    models.ManyToManyField(
                        blank=True, to="course.Course", verbose_name="Courses"
                    ),
                ),
            ],
            options={
                "verbose_name": "Module",
                "verbose_name_plural": "Modules",
            },
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "unit_number",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="Unit number",
                    ),
                ),
                (
                    "unit_name",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Unit name",
                    ),
                ),
                (
                    "unit_overview",
                    models.TextField(
                        blank=True, null=True, verbose_name="Unit overview"
                    ),
                ),
                (
                    "unit_outcome",
                    models.TextField(
                        blank=True, null=True, verbose_name="Unit outcome"
                    ),
                ),
                (
                    "unit_objective",
                    models.TextField(
                        blank=True, null=True, verbose_name="Unit objective"
                    ),
                ),
                (
                    "unit_body",
                    models.TextField(
                        blank=True, null=True, verbose_name="Unit body"
                    ),
                ),
                (
                    "unit_resources",
                    models.TextField(
                        blank=True, null=True, verbose_name="Unit resources"
                    ),
                ),
                (
                    "unit_test",
                    models.TextField(
                        blank=True, null=True, verbose_name="Unit test"
                    ),
                ),
                (
                    "module",
                    models.ManyToManyField(
                        blank=True, to="course.Module", verbose_name="Modules"
                    ),
                ),
            ],
            options={"verbose_name": "Unit", "verbose_name_plural": "Units",},
        ),
        migrations.CreateModel(
            name="Programme",
            fields=[
                (
                    "programme_code",
                    models.CharField(
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Programme code",
                    ),
                ),
                (
                    "programme_name",
                    models.CharField(
                        max_length=50, verbose_name="Programme name"
                    ),
                ),
                (
                    "programme_fees",
                    models.FloatField(
                        blank=True, null=True, verbose_name="Programme fees"
                    ),
                ),
                (
                    "level",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.Level",
                        verbose_name="Levels",
                    ),
                ),
            ],
            options={
                "verbose_name": "Programme",
                "verbose_name_plural": "Programmes",
            },
        ),
        migrations.CreateModel(
            name="Discipline",
            fields=[
                (
                    "discipline_code",
                    models.CharField(
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Discipline code",
                    ),
                ),
                (
                    "discipline_name",
                    models.CharField(
                        max_length=50, verbose_name="Discipline name"
                    ),
                ),
                (
                    "total_credits",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "programme",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.Programme",
                        verbose_name="Programmes",
                    ),
                ),
            ],
            options={
                "verbose_name": "Discipline",
                "verbose_name_plural": "Disciplines",
            },
        ),
        migrations.AddField(
            model_name="course",
            name="discipline",
            field=models.ManyToManyField(
                blank=True, to="course.Discipline", verbose_name="Disciplines"
            ),
        ),
    ]