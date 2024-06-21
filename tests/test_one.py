@pytest.fixture()

def dagbag():
    return DagBag(dag_folder="dags")

def test_no_import_errors(dagbag):
    """
    Test Dags to contain no import errors.
    """
    assert not dagbag.import_errors
