import pytest


@pytest.mark.django_db
def test_institution_model(institution_factory):
    instance = institution_factory.create(name="uon")
    assert instance.name == "uon"
    assert str(instance) == "uon"


@pytest.mark.django_db
def test_campus_model(campus_factory):
    instance = campus_factory.create(name="kimbo juja campus")
    assert instance.name == "kimbo juja campus"
    assert str(instance) == "kimbo juja campus"


@pytest.mark.django_db
def test_academic_unit_model(academic_unit_factory):
    instance = academic_unit_factory.create(name="test academic unit")
    assert instance.name == "test academic unit"
    assert str(instance) == "test academic unit"


@pytest.mark.django_db
def test_program_model(program_factory):
    instance = program_factory.create(level="degree")
    result = str(instance)
    assert isinstance(result, str)
