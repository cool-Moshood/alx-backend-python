#!/usr/bin/env python3
"""typing protocols"""
from typing import TypeVar


T = TypeVar('T')


def safely_get_value(dct: dict, key: str, default: T = None) -> T:
    """typing module"""

    if key in dct:
        return dct[key]
    else:
        return default
