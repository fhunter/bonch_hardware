""" Module for html formatting json hardware data """

def html_capabilities(data):
    """ Implements capabilities formatting, expects dictionary """
#    result = ""
#    for key, value in data.items():
#        result += f"""<dfn title="{value}">{key}</dfn> """
    result = ' '.join(
        [f"<dfn title='{value}'>{key}</dfn>" for key, value in data.items()]
    )
    result += "\n"
    return result

def html_configuration(data):
    """ Implements configuration table, expects dictionary """
    begin = "<tr><td class='sub-first'>"
    middle = "</td><td>=</td><td>"
    end = "</td></tr>"
    result = '\n'.join(
        [f"{begin}{key}{middle}{value}{end}" for key, value in data.items()]
    )
    return result

def json2tree(data, depth= 1):
    """ Forms html representation of configuration json data. Recursively """
    outdata = """<div class='indented'>\n"""

    # start table
    width = "width=100% " if depth== 1 else ""
    outdata += f"""<table {width} class='node' summary='attributes of {data["id"]}'>"""
    # end table

    # add ID
    outdata += """<thead><tr><td class="first">id:</td>"""
    outdata += f"<td class='second'><div class='id'>{data['id']}</div></td></tr></thead>"
    # end of ID
    for i in data:
        if i in ["id", "configuration", "capabilities", "children"]:
            # already filled in, skip
            continue
        outdata += f"""<tr><td class="first">{i}: </td><td class="second">{data[i]}</td></tr>\n"""
    if "capabilities" in data:
        # fill with dfn's - separate function
        outdata += """<tr><td class="first">capabilities: </td><td class="second">"""
        outdata += html_capabilities(data["capabilities"])
        outdata += "</td></tr>"
    if "configuration" in data:
        # fill with configuration table - separate function
        outdata += """<tr><td class="first">configuration:</td><td class="second">"""
        outdata += """<table summary="configuration of %s">""" % data["id"]
        outdata += html_configuration(data["configuration"])
        outdata += """</table></td></tr>"""

    outdata += "</table>"

    if "children" in data:
        outdata += '\n'.join([json2tree(i, depth + 1) for i in data["children"]])
    outdata += """\n</div>"""
    return outdata
