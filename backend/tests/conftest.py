import pytest
from rest_framework.test import APIRequestFactory

from tests.accounts.factories import ProfileFactory
from tests.institutions.factories import (
    AcademicUnitFactory,
    CampusFactory,
    InstitutionFactory,
    ProgramFactory,
)


@pytest.fixture
def api_factory():
    return APIRequestFactory()


@pytest.fixture
def institution_factory():
    return InstitutionFactory


@pytest.fixture
def campus_factory():
    return CampusFactory


@pytest.fixture
def academic_unit_factory():
    return AcademicUnitFactory


@pytest.fixture
def program_factory():
    return ProgramFactory


### Profile Fixtures
# ------------------------------------------------
@pytest.fixture
def profile_factory():
    return ProfileFactory
