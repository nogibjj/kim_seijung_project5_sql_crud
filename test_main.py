from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    create,
    read,
    update,
    delete,
    count_survivors_by_class,
    avg_fare_by_embarkation,
)


def test_extract():
    """Test the extract function."""
    data = extract()
    assert data == "data/titanic.csv"


def test_load():
    """Test the load function."""
    data = load()
    assert data == "TitanicDB.db"


def test_create():
    """Test the create function."""
    result = create()
    assert result == "Create Success"


def test_read():
    """Test the read function."""
    result = read()
    assert result == "Read Success"


def test_update():
    """Test the update function."""
    result = update()
    assert result == "Update Success"


def test_delete():
    """Test the delete function."""
    result = delete()
    assert result == "Delete Success"


def test_count_survivors_by_class():
    """Test the count_survivors_by_class function."""
    result = count_survivors_by_class()
    assert result == "Count Survivors by Class Success"


def test_avg_fare_by_embarkation():
    """Test the avg_fare_by_embarkation function."""
    result = avg_fare_by_embarkation()
    assert result == "Average Fare by Embarkation Success"
