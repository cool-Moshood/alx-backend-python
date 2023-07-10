#!/usr/bin/env python3
"""A type-annotated module"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[
        typing.Tuple[typing.Sequence, int]]:
    """Function to calculate the length of elements in a list"""

    return [(i, len(i)) for i in lst]
