#!/usr/bin/python
# -*- coding: utf-8 -*-


def compare_keys(
    dict1,
    dict2,
    dict1_keys,
    dict2_keys,
    depth,
    status,
    ):
    if dict1_keys == dict2_keys:
        status = True
    else:
        status = False

        # stop condition

    if depth == 0:
        return status
    else:
        for key in dict1_keys:
            if isinstance(dict1[key], dict):
                depth -= 1

                    # update the keys

                dict1_keys = dict1[key].keys()
                dict2_keys = dict2[key].keys()
                Helpers.compare_keys(
                    dict1,
                    dict2,
                    dict1_keys[key],
                    dict2_keys[key],
                    depth,
                    status,

                    )
    return status
