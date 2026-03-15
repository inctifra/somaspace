from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampModel


class Institution(TimeStampModel):
    class InstitutionType(models.TextChoices):
        university = "university", "University"
        tvet = "tvet", "Tvet"
        college = "college", "College"
        vocational = "vocational", "Vocational"

    name = models.CharField(max_length=200, verbose_name=_("Institution Name"))
    type = models.CharField(
        max_length=100,
        choices=InstitutionType.choices,
        default=InstitutionType.university,
    )
    county = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True, upload_to="logo/")
    verified = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "type", "county"], name="unique_institution_name_county"
            )
        ]

    def __str__(self):
        return self.name


class Campus(TimeStampModel):
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name="campuses"
    )
    name = models.CharField(verbose_name=_("Campus Name"), max_length=255)
    county = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "institution", "county"],
                name="unique_campus_institution_name_county",
            )
        ]

    def __str__(self):
        return self.name


class AcademicUnit(TimeStampModel):
    class AcademicUnitType(models.TextChoices):
        college = "college", "College"
        school = "school", "School"
        faculty = "faculty", "Faculty"
        department = "department", "Department"

    campus = models.ForeignKey(
        Campus, on_delete=models.CASCADE, related_name="campus_academicunits"
    )
    institution = models.ForeignKey(
        Institution,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="institution_academicunits",
    )
    name = models.CharField(
        verbose_name=_("Academic Unit Name"),
        max_length=255,
        help_text="Just a academic unit name",
    )
    type = models.CharField(
        max_length=100,
        choices=AcademicUnitType.choices,
        default=AcademicUnitType.college,
    )
    county = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "campus", "type"],
                name="unique_campus_academic_unit_name_county",
            )
        ]

    def __str__(self):
        return self.name


class Program(TimeStampModel):
    class ProgramLevel(models.TextChoices):
        certificate = "certificate", "Certificate"
        diploma = "diploma", "Diploma"
        degree = "degree", "Degree"
        masters = "masters", "Masters"

    academic_unit = models.ForeignKey(
        AcademicUnit, on_delete=models.CASCADE, related_name="programs"
    )
    name = models.CharField(verbose_name=_("Program Name"), max_length=255)
    level = models.CharField(
        max_length=100,
        choices=ProgramLevel.choices,
        default=ProgramLevel.degree,
    )
    duration_years = models.PositiveIntegerField(default=4)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["academic_unit", "name", "level"],
                name="unique_academic_unit_name_level",
            )
        ]

    def __str__(self):
        return self.name
