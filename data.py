""" Module for filtering data received from computers """

def filter_hardware_report(data_in):
    """ Filter incoming data for frequently changeable attributes
    not relevant to hardware configuration (like current cpu frequency) """
    if data_in.get("id") == "cpu":
        del data_in["size"]
    if data_in.get("class") == "volume":
        if "configuration" in data_in:
            if "modified" in data_in["configuration"]:
                del data_in["configuration"]["modified"]
            if "mounted" in data_in["configuration"]:
                del data_in["configuration"]["mounted"]
    if "children" in data_in:
        for i in data_in["children"]:
            filter_hardware_report(i)
    return data_in
