from core.db import fetch_many
from core.queries import get_rates_query

from .base import BaseModel


class Price(BaseModel):
    @classmethod
    def get_rates(cls, date_from, date_to, origin: str, destination: str) -> tuple:
        from .region import Region

        region = Region()

        if region.exists(origin):
            origin = region.get_ports(origin)

        if region.exists(destination):
            destination = region.get_ports(destination)

        records = fetch_many(
            get_rates_query.format(
                date_from=date_from,
                date_to=date_to,
                origins=cls._list_to_query_safe_list(cls, origin),
                destinations=cls._list_to_query_safe_list(cls, destination),
            )
        )

        return records
