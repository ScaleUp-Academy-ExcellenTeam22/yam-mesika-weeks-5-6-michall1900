from functools import reduce


def get_recipe_price(prices: dict, optionals: list = None, **gram_ingredients: float) -> float:
    """
    Receives dictionary when key its ingredient's names and item is their price for 100 g,
    list of optional ingredients that someone don't want to buy at all and dictionary with same keys as the first
    but it's items is how many grams do we need to buy.
    If there is key in prices dictionary that has no quantity at gram_ingredients, the function add its price as
    it is.
    Anyway, the function calculate and return the final shopping price for the recipe.
    :param prices: Keys are ingredients names, items are their price for 100 gram.
    :param optionals: List of items (as keys) that we don't want to buy.
    :param gram_ingredients: Keys as prices dictionary and items as grams we need to buy.
    :return: Total price.
    """
    return reduce(lambda total_price, key: total_price + prices.get(key) * (gram_ingredients.get(key) or 100) / 100
                  if not optionals or key not in optionals else total_price, prices, 0)


def main_piece_of_cake() -> None:
    """
    Send prices for 100 g of ingredient, wanted quantity for recipe and ingredient we don't want to buy
    and print the total shopping price.
    :return: None.
    """
    (lambda prices, grams:
     [print(get_recipe_price(prices, **grams)),
      print(get_recipe_price(prices=prices, optionals=['milk'], **grams))])({'chocolate': 18, 'milk': 8},
                                                                            dict({('chocolate', 200), ('milk', 100)}))
    print(get_recipe_price({'rice': 5, 'chicken': 30, 'wine': 20}, rice=400, chicken=1000))
    print(get_recipe_price({}))


if __name__ == "__main__":
    main_piece_of_cake()
