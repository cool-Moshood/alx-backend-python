#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float"""

    return float(sum(mxd_lst))
