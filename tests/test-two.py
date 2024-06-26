def test_expected_dags(dagbag):
    """
    Test whether expected dag Ids are present.
    """
    expected_dags_ids = ["airflow-ci-cd-tutorial"]

    for dag_id in expected_dags_ids:
        dag = dagbag.get_dag(dag_id)

        assert dag is not None
        assert dag_id == dag.dag_id
