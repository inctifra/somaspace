import pytest


@pytest.mark.django_db
def test_profile_model_return(profile_factory):
    profile = profile_factory.create(fname="john", lname="doe")
    result = str(profile)
    flname = profile.get_full_name
    assert isinstance(result, str)
    assert flname == f"{profile.fname} {profile.lname}"
