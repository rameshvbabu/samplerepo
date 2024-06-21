def test_requires_approved_tag(dagbag):
    """
    Test if DAGS contain one or more tags from list of approved tags only.
    """
    Expected_tags = {"tutorial", "CI/CD"}
    dagIds = dagbag.dag_ids

    for id in dagIds:
        dag = dagbag.get_dag(id)
        assert dag.tags
        if Expected_tags:
            assert not set(dag.tags) - Expected_tags