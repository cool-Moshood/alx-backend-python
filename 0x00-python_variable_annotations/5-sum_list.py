#!/usr/bin/env python3
"""a type-annotated function sum_list which takes
a list input_list of floats"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """function sum_list which takes a list input_list of
floats as argument and returns their sum as a float"""

    return float(sum(input_list))
