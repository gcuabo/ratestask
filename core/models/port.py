from .base import ParentChildModel
from core.db import fetch_one
from core.queries import check_port_exists, get_port_query, get_port_children_query


class Port(ParentChildModel):
    GET_CHILDREN_QUERY = get_port_children_query

    @staticmethod
    def exists(code: str) -> bool:
        query = check_port_exists.format(code=code)
        return fetch_one(query)

    @staticmethod
    def get_one(code: str):
        query = get_port_query.format(code=code)
        return fetch_one(query)
