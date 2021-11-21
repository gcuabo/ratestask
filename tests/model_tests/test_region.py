from core.models.base import ParentChildModel
from core.models.region import Region


def test_region():
    region = Region()
    assert isinstance(region, ParentChildModel)
    assert callable(region.get_children)
    assert callable(region.exists)
    assert callable(region.get_one)
    assert callable(region.get_ports)

    assert isinstance(region.get_children("uk_main"), list)
    assert isinstance(region.get_ports("uk_main"), list)
    assert isinstance(region.get_one("uk_main"), tuple)
