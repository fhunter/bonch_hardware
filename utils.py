""" Module for html formatting json hardware data """

from bottle import template

def html_capabilities(data):
    """ Implements capabilities formatting, expects dictionary """
    return template('capabilities_template', data = data)

def html_configuration(entity_id,data):
    """ Implements configuration table, expects dictionary """
    return template('configuration_template', data = data, entity_id = entity_id)

def json2tree(data, depth= 1, diff= None, lr= None):
    """ Forms html representation of configuration json data. Recursively
        $insert -> right, green
        $delete -> left, red
        $update -> ????
    """
    exclude = ["id", "configuration", "capabilities", "children"]
    outdata = template("items_template", data = data, exclude = exclude, depth = depth)
    if "capabilities" in data:
        # fill with dfn's - separate function
        outdata += html_capabilities(data["capabilities"])
    if "configuration" in data:
        # fill with configuration table - separate function
        outdata += html_configuration(data["id"], data["configuration"])

    outdata += "</table>"
    outdata += str(diff) + "<br/>"

    if "children" in data:
        new_diff = {}
        if diff is not None:
            if "$update" in diff:
                if "children" in diff["$update"]:
                    new_diff = diff["$update"]["children"]
        outdata += '\n'.join([json2tree(data["children"][i], depth + 1, new_diff.get(i), lr) for i in range(0,len(data["children"]))])
    outdata += """\n</div>"""
    return outdata
