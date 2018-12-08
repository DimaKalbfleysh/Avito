#!/usr/bin/env python
import public


def _lists(matrix):
    widths = [max(map(len, map(str, col))) for col in zip(*matrix)]
    for row in matrix:
        yield "  ".join((str(val).ljust(width) for val, width in zip(row, widths)))


@public.add
def lists(matrix):
    """columnate lists"""
    return "\n".join(list(_lists(matrix)))
