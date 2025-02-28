import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    @pytest.mark.parametrize("expected_name, expected_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_available_buns(self, expected_name, expected_price, setup):
        available_buns = setup.available_buns()
        bun_names = [bun.get_name() for bun in available_buns]
        bun_prices = [bun.get_price() for bun in available_buns]

        assert expected_name in bun_names
        assert expected_price in bun_prices

    @pytest.mark.parametrize("expected_name, expected_price, expected_type", [
        ("hot sauce", 100, INGREDIENT_TYPE_SAUCE),
        ("sour cream", 200, INGREDIENT_TYPE_SAUCE),
        ("chili sauce", 300, INGREDIENT_TYPE_SAUCE),
        ("cutlet", 100, INGREDIENT_TYPE_FILLING),
        ("dinosaur", 200, INGREDIENT_TYPE_FILLING),
        ("sausage", 300, INGREDIENT_TYPE_FILLING)
    ])
    def test_available_ingredients(self, expected_name, expected_price, expected_type, setup):
        available_ingredients = setup.available_ingredients()
        ingredient_names = [ingredient.get_name() for ingredient in available_ingredients]
        ingredient_prices = [ingredient.get_price() for ingredient in available_ingredients]
        ingredient_types = [ingredient.get_type() for ingredient in available_ingredients]

        assert expected_name in ingredient_names
        assert expected_price in ingredient_prices
        assert expected_type in ingredient_types