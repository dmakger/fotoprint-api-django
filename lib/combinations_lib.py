from mptt.querysets import TreeQuerySet

from characteristic.models import Combination
from product.models import Product


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
