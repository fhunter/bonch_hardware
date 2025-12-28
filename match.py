#!/usr/bin/env python3


def hardwarematches(hardware, match, path="/"):
    if type(match) == dict:
        return hardwarematches_d(hardware, match, path)
    elif type(match) == list:
        return all([hardwarematches_d(hardware, x) for x in match])
    else:
        return False


def hardwarematches_d(hardware, match, path="/"):
    result = False
    temp = True
    for i in match.keys():
        if not i in hardware:
            temp = False
            break
        else:
            value = hardware[i]
            if (value != match[i]) and not (value.startswith(match[i])):
                temp = False
                break
    result = result or temp
    if "children" in hardware:
        for i in hardware["children"]:
            result = result or hardwarematches_d(i, match, path + i["id"] + "/")
    return result
