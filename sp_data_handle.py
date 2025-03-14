from jsonpath_ng import parse


def get_data_from_json(json_data, json_path):
    jsonpath_expr = parse(json_path)
    return [match.value for match in jsonpath_expr.find(json_data)]

