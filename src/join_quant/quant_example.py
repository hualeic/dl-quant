from jqdatasdk import get_query_count, get_account_info
from jqdatasdk import auth
auth('15986639830','Khwj240812!')

infos = get_query_count()
print(infos)
infos = get_account_info()
print(infos)