import os
import pytest
from model.creature import Creature
from errors import Missing, Duplicate

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import init, creature


@pytest.fixture
def sample() -> Creature:
    return Creature(name="Yeti", description="Abominable Snowman", location="Himalayas")


def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        resp = creature.create(sample)


def test_get_exists(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        resp = creature.get_one("boxturtle")


def test_modify(sample):
    creature.location = "Sesame Street"
    resp = creature.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    bob: Creature = Creature(name="bob", description="some guy", location="somewhere")
    with pytest.raises(Missing):
        resp = creature.modify(bob.name, bob)


def test_delete(sample):
    resp = creature.delete(sample.name)
    assert resp is None


def test_delete_missing(sample):
    with pytest.raises(Missing):
        resp = creature.delete(sample.name)
