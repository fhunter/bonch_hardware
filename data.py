
def filter_hardware_report(data_in):
    if "id" in data_in:
        if data_in["id"] == "cpu":
            del data_in["size"]
    if "children" in data_in:
        for i in data_in["children"]:
            filter_hardware_report(i)
    return data_in
