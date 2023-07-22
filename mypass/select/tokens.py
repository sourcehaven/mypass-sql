from mypass.identifier_list.tokens import *
from mypass.where.tokens import *
from mypass.tokens import (
    SELECT, FROM, ORDER_BY, ASCENDING, DESCENDING,
    t_SELECT, t_FROM, t_ORDER_BY, t_ASCENDING, t_DESCENDING,
    t_ignore, t_error, t_newline
)

select_tokens = tuple(
    set(
        (
            SELECT,
            FROM,
            ORDER_BY,
            ASCENDING,
            DESCENDING,
        )
        + identifier_tokens
        + where_tokens
    )
)

tokens = select_tokens

x = 4