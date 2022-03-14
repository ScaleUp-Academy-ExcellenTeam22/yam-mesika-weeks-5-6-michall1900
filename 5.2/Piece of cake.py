"""
Calculate price for recipe's ingredients
"""


def get_recipe_price(prices: dict, optionals: list = None, **gram_ingredients: dict) -> float or None:
    """Receives dictionary when key its ingredients name's and item is their price for 100 g,
    list of optional ingredients that someone don't want to buy at all and dictionary with same keys as the first
    but it's items is how many grams do we need to buy.
    If keys are not the same at both of dictionaries, return null. Otherwise, calculate and return the final price.
    :param prices: Keys are ingredients names, items are their price for 100 gram
    :param optionals: List of items (as keys) that we don't want to buy.
    :param gram_ingredients: Keys as prices dictionary and items as grams we need to buy.
    :return: none when there is error, else, total price when
    """
    if not prices.keys() == gram_ingredients.keys():
        print("There are missing key/s at one of the dicts")
        return None
    final_price = 0
    for key, item in prices.items():
        if optionals is not None and key in optionals:
            continue
        final_price += item * gram_ingredients.get(key) / 100

    return final_price


def main_piece_of_cake():
    # Just doing and printing some tests.
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, ['milk'], chocolate=200, milk=100))
    print(get_recipe_price({}))


if __name__ == "__main__":
    main_piece_of_cake()
