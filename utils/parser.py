def event_parse_to_json(result):
    columns = [f'columna{i}' for i in range(1, 28)]

    data = []
    for row in result:
        json = {col: getattr(row, col) for col in columns}
        data.append(json)
    return data
