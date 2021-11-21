from .base import ParentChildModel
from core.db import fetch_one
from core.queries import (
    check_region_exists,
    get_region_query,
    get_region_children_query,
)


class Region(ParentChildModel):
    GET_CHILDREN_QUERY = get_region_children_query

    @classmethod
    def exists(cls, slug: str) -> bool:
        query = check_region_exists.format(slug=slug)
        return fetch_one(query)

    @classmethod
    def get_one(cls, slug: str) -> tuple:
        query = get_region_query.format(slug=slug)
        return fetch_one(query)

    @classmethod
    def get_ports(cls, slug: str) -> list:
        from .port import Port

        regions_in = cls.get_children(slug)
        regions_in.append(slug)
        return Port().get_children(regions_in)
