'''
This file has useful code snippets from the MYPY documentation.
'''

def greeting(name: str) -> str:
    return 'Hello ' + name

# greeting(3)
greeting(' Kuni') # If you did not put annotations mypy would not capture the error

from typing import List
def greet_all(names: List[str]) -> None:
    for name in names:
        print('Hello ' + name)

# no need to be exactly a string
from collections.abc import Iterable
def greet_all_two(names: Iterable[str]) -> None:
    for name in names:
        print('Hello ' + name)

# you want a function which can accept either an int or a string
from typing import Union
def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return 'user-{}'.format(100000 + user_id)
    else:
        return user_id

from typing import Optional
def greeting_two(name: Optional[str] = None) -> str:
    # Optional[str] means the same thing as Union[str, None]
    if name is None:
        name = 'stranger'
    return 'Hello, ' + name


# d = {}  Error: Need type annotation for "my_global_dict"
from typing import Dict
d: Dict[int, float] = {}

import pandas as pd # type: ignore

print(pd.to_datetime('2021-02-20'))