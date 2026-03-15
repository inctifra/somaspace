import factory
from factory.django import DjangoModelFactory
from faker import Faker

from apps.institutions.models import AcademicUnit, Campus, Institution, Program
from tests.utils import DegreeCourseProvider

faker = Faker()
faker.add_provider(DegreeCourseProvider)


class InstitutionFactory(DjangoModelFactory):
    class Meta:
        model = Institution

    name = faker.name()
    type = faker.random_element(
        elements=[
            "university",
            "tvet",
            "college",
            "vocational",
        ]
    )
    county = faker.random_elements(
        elements=["kiambu", "migori", "nairobi", "kisumu", "turkana"]
    )
    website = faker.url()
    logo = factory.django.ImageField()
    verified = True


class CampusFactory(DjangoModelFactory):
    class Meta:
        model = Campus

    institution = factory.SubFactory(InstitutionFactory)
    name = factory.LazyFunction(lambda: f"{faker.city()} Campus")
    county = factory.LazyFunction(faker.city)
    city = factory.LazyFunction(faker.city)


class AcademicUnitFactory(DjangoModelFactory):
    class Meta:
        model = AcademicUnit

    # institution = factory.SubFactory(InstitutionFactory)
    campus = factory.SubFactory(CampusFactory)
    name = factory.LazyFunction(lambda: f"{faker.city()} Campus")
    county = factory.LazyFunction(faker.city)
    type = faker.random_element(
        elements=[
            "college",
            "school",
            "faculty",
            "department",
        ]
    )


class ProgramFactory(DjangoModelFactory):
    class Meta:
        model = Program

    academic_unit = factory.SubFactory(AcademicUnitFactory)
    name = factory.LazyFunction(faker.degree_course)
    level = faker.random_element(
        elements=[
            "certificate",
            "diploma",
            "degree",
            "masters",
        ]
    )
    duration_years = 4
