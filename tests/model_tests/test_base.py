from core.models.base import BaseModel, ParentChildModel


def test_base_model():
    base = BaseModel()
    assert callable(base._list_to_query_safe_list)
    assert isinstance(base._list_to_query_safe_list(["test_string"]), str)
    assert isinstance(base._list_to_query_safe_list("some_strring"), str)


def test_parent_child_model():
    model = ParentChildModel()
    assert callable(model.get_children)
