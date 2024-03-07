""" Module for filtering data received from computers """

def filter_hardware_report(data_in):
    """ Filter incoming data for frequently changeable attributes
    not relevant to hardware configuration (like current cpu frequency) """
    if "id" in data_in:
        if data_in["id"] == "cpu":
            del data_in["size"]
    if "children" in data_in:
        for i in data_in["children"]:
            filter_hardware_report(i)
    return data_in
