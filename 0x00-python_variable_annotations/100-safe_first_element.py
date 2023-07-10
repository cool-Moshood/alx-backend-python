#!/usr/bin/env python3
# The types of the elements of the input are not know
from types import NoneType
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[
        typing.Any, NoneType]:
    """function that lst and return lst[0] or none"""

    if lst:
        return lst[0]
    else:
        return None
