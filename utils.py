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

def html_capabilities(data):
    result = ""
    for i in data:
        result += f"""<dfn title="{data[i]}">{i}</dfn> """
    result += "\n"
    return result

def html_configuration(data):
    result = ""
    for i in data:
        result += f"""<tr><td class="sub-first"> {i}</td><td>=</td><td>{data[i]}</td></tr>\n"""
    return result

def json2tree(data, depth= 1):
    outdata = ""
#    for i in range(0,depth):
    outdata += """<div class='indented'>\n"""
    # start table
    outdata += """<table border=1 """
    if depth == 1:
        outdata += """width=100% """
    outdata += """class='node' summary='attributes of %s'>""" % data["id"]
    # end table
    # add ID
    outdata += """<thead><tr><td class="first">id:</td><td class="second"><div class="id">%s</div></td></tr></thead>""" % data["id"]
    # end of ID
    for i in data:
        if i in ["id", "configuration", "capabilities", "children"]:
            # already filled in, skip
            continue
        if i == "capabilities":
            # fill with dfn's - separate function
            outdata += """<tr><td class="first">capabilities: </td><td class="second">"""
            outdata += html_capabilities(data[i])
            outdata += "</td></tr>"
            continue
        if i == "configuration":
            # fill with configuration table - separate function
            outdata += """<tr><td class="first">configuration:</td><td class="second"><table border=1 summary="configuration of %s">""" % data["id"]
            outdata += html_configuration(data[i])
            outdata += """</table></td></tr>"""
            continue
        if i == "children":
            continue
        outdata += f"""<tr><td class="first">{i}: </td><td class="second">{data[i]}</td></tr>\n"""
    for i in ["capabilities", "configuration"]:
        if i in data:
            if i == "capabilities":
                # fill with dfn's - separate function
                outdata += """<tr><td class="first">capabilities: </td><td class="second">"""
                outdata += html_capabilities(data[i])
                outdata += "</td></tr>"
            if i == "configuration":
                # fill with configuration table - separate function
                outdata += """<tr><td class="first">configuration:</td><td class="second"><table border=1 summary="configuration of %s">""" % data["id"]
                outdata += html_configuration(data[i])
                outdata += """</table></td></tr>"""
    outdata += "</table>"
    if "children" in data:
        for i in data["children"]:
            outdata += json2tree(i, depth + 1)
            outdata += "\n"
#    for i in range(0,depth):
    outdata += """\n</div>"""
    return outdata
