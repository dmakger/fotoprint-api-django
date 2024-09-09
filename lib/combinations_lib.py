from django.db.models import QuerySet
from mptt.querysets import TreeQuerySet

from characteristic.models import Combination
from product.models import Product, ProductCharacteristicCombination


def get_parents_combination_by_product(product: Product):
    combinations: TreeQuerySet[Combination] = Combination.objects.filter(
        productcharacteristiccombination__product=product
    ).distinct()
    parents = set()
    for parent in combinations:
        x = parent
        while x.parent:
            x = x.parent
        parents.add(x)
    return parents


def get_combinations_as_dict_id(product: Product):
    combinations: QuerySet[ProductCharacteristicCombination] = ProductCharacteristicCombination.objects.filter(
        product=product
    )
    d = dict()
    for c in combinations:
        x: Combination = c.combination
        ids = [x.characteristic.id]
        while x.parent:
            x = x.parent
            # ids.append(x.id)
            ids.append(x.characteristic.id)
        d[c.id] = ids
    return d


def get_product_combination_id(base: dict[int, list[int]], current_ids: list[int]):
    closest_key = None
    max_matches = -1  # Счетчик для отслеживания наибольшего количества совпадений

    # Итерируем по словарю в обратном порядке
    # for key, values in reversed(base.items()):
    for key, values in base.items():
        matches = len(set(values) & set(current_ids))  # Подсчитываем количество совпадений между списками
        if matches > max_matches:
            max_matches = matches
            closest_key = key
    return closest_key
