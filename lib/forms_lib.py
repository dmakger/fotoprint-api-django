def add_characteristics_in_form(node, characteristics, form_data):
    """ Рекурсивно добавляем характеристики и связываем их с формами """
    if not characteristics:
        return

    # Берем первую характеристику и проверяем, есть ли она в текущем узле
    current_char = characteristics[0]
    existing_child = next((child for child in node['children'] if child['id'] == current_char['id']), None)

    if existing_child is None:
        # Если текущей характеристики нет среди детей, добавляем её
        new_child = {
            'id': current_char['id'],
            'title': current_char['title'],
            'description': current_char['description'],
            'characteristicGroup': current_char['characteristicGroup'],
            'children': []
        }
        node['children'].append(new_child)
        existing_child = new_child

    # Если осталась одна характеристика, добавляем форму
    if len(characteristics) == 1:
        existing_child['form'] = form_data
    else:
        # Идем дальше вглубь характеристик
        add_characteristics(existing_child, characteristics[1:], form_data)