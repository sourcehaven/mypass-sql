from mypass.identifier_equeals_literal_list.tokens import *
from mypass.tokens import WHERE, t_WHERE

where_tokens = (WHERE,) + identifier_equals_literal_tokens

tokens = where_tokens
