""" Module for html formatting json hardware data """

from bottle import template
from copy import deepcopy

def html_capabilities(data):
    """ Implements capabilities formatting, expects dictionary """
    # FIXME - implement diff
    return template('capabilities_template', data = data)

def html_configuration(entity_id,data):
    """ Implements configuration table, expects dictionary """
    # FIXME - implement diff
    return template('configuration_template', data = data, entity_id = entity_id)

def json2tree(data, depth= 1, diff= None, lr= None, added=False, deleted=False):
    """ Forms html representation of configuration json data. Recursively
        $insert -> right, green
        $delete -> left, red
        $update -> ????
    """
    exclude = ["id", "configuration", "capabilities", "children"]
    outdata = template("items_template", data = data, exclude = exclude, depth = depth, diff=diff, lr= lr, added=added, deleted=deleted)
    if "capabilities" in data:
        # fill with dfn's - separate function
        outdata += html_capabilities(data["capabilities"])
    if "configuration" in data:
        # fill with configuration table - separate function
        outdata += html_configuration(data["id"], data["configuration"])

    outdata += "</table>"

    # FIXME: this is debug (begin)
    if diff:
        tmp_diff = deepcopy(diff)
        for i in ["update","insert","delete"]:
            if "$" + i in tmp_diff:
                outdata += "<b>" + i.capitalize() + ":</b> " + str(tmp_diff["$" + i]) + "<br/>"
    # FIXME: this is debug (end)

    if "children" in data:
        new_diff = {}
        new_added = False
        new_deleted = False
        if diff is not None:
            if "$update" in diff:
                if "children" in diff["$update"]:
                    new_diff = diff["$update"]["children"]
        temp_list = []
        for i in range(0,len(data["children"])):
            if (diff is not None) and ("$delete" in diff):
                new_deleted = True
                print("deleted", diff["$delete"])
            if (diff is not None) and ("$insert" in diff):
                new_added = True
                print("added", diff["$insert"])
            temp_list.append(json2tree(data["children"][i], depth +1, new_diff.get(i), lr, new_added, new_deleted))
        outdata += '\n'.join(temp_list)
#        outdata += '\n'.join([json2tree(
#                                data["children"][i],
#                                depth + 1,
#                                new_diff.get(i),
#                                lr, added, deleted) for i in range(0,len(data["children"]))])
    outdata += """\n</div>"""
    return outdata
