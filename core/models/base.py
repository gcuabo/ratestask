from typing import Union

from core.db import fetch_many

# __all__ = ("BaseModel", "ParentChildModel")


class BaseModel(object):
    def _list_to_query_safe_list(self, list_or_string: Union[list, str]) -> str:
        """
        Convert list or string to comma separated query friendly string
        e.g.
            k           => ('k')
            [a, b, c]   => ('a', 'b', 'c')

        ---
        :param list_or_string:
        :return:
        """

        is_list = isinstance(list_or_string, list) or isinstance(list_or_string, tuple)

        if is_list:
            query_safe_list = ",".join([f"'{s}'" for s in list_or_string])
        else:
            query_safe_list = f"'{list_or_string}'"
        return f"({query_safe_list})"


class ParentChildModel(BaseModel):
    """
    For models with 'parent_slug' column
    """

    @classmethod
    def get_children(cls, slug: Union[str, list]) -> list[str]:
        """
        Get children of object based on 'parent_slug' column.
        return list Includes children of children

        :param slug:
        :return:
        """
        children_complete_list = []
        code_or_slug_in_string = cls._list_to_query_safe_list(cls, slug)
        query_results = fetch_many(
            cls.GET_CHILDREN_QUERY.format(parents=code_or_slug_in_string)
        )
        children = [s[0] for s in query_results]
        children_complete_list.extend(children)

        while children:
            children = cls.get_children(children)
            if children:
                children_complete_list.extend(children)
        return children_complete_list
