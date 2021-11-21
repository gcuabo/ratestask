from core.models.base import ParentChildModel
from core.models.port import Port


def test_port():
    port = Port()
    assert isinstance(port, ParentChildModel)
    assert callable(port.get_children)
    assert callable(port.exists)
    assert callable(port.get_one)

    assert isinstance(port.get_children("uk_main"), list)
