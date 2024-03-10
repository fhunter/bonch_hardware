""" Module for html formatting json hardware data """

from bottle import template

def html_capabilities(data):
    """ Implements capabilities formatting, expects dictionary """
    return template('capabilities_template', data = data)

def html_configuration(entity_id,data):
    """ Implements configuration table, expects dictionary """
    return template('configuration_template', data = data, entity_id = entity_id)

def json2tree(data, depth= 1):
    """ Forms html representation of configuration json data. Recursively """
    exclude = ["id", "configuration", "capabilities", "children"]
    outdata = template("items_template", data = data, exclude = exclude, depth = depth)
    if "capabilities" in data:
        # fill with dfn's - separate function
        outdata += html_capabilities(data["capabilities"])
    if "configuration" in data:
        # fill with configuration table - separate function
        outdata += html_configuration(data["id"], data["configuration"])

    outdata += "</table>"

    if "children" in data:
        outdata += '\n'.join([json2tree(i, depth + 1) for i in data["children"]])
    outdata += """\n</div>"""
    return outdata
