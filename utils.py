from copy import copy

def makesummary(data):
    result = ""
    if isinstance(data,dict):
        newdata = copy(data)
        if "children" in newdata:
            del newdata["children"]
        for key, value in newdata.items():
            result += f"{key} = {value}<br/>\n"
    else:
        result = str(data)
    return result

def json2tree(data):
    outdata = "<ul class='tree'>\n"
#    outdata = "<ul>"
    if isinstance(data, dict):
        summary = makesummary(data)
        lst = ""
        if "children" in data:
            lst = json2tree(data["children"])
        outdata += "<li><details open><summary>" + summary + "</summary>" + lst + "</details></li>"
    elif isinstance(data, list):
        for value in data:
            summary = makesummary(value)
            outdata += "<li><details open><summary>" + summary + "</summary>" + json2tree(value) + "</details></li>"
    else:
        return str(data)
    outdata += "</ul>"
    return outdata
