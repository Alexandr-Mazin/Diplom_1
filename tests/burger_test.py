import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from data import DataIngredient

class TestBurger:

    def test_set_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burger):
        removed_ingredient = burger.ingredients[0]
        burger.remove_ingredient(0)

        assert removed_ingredient not in burger.ingredients

    def test_move_ingredient(self, burger):
        moved_ingredient = burger.ingredients[1]
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == moved_ingredient

    def test_get_price_burger_success(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == DataIngredient.burger_final_cost

    def test_get_receipt_success(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_receipt = (
            '(==== Флюоресцентная булка R2-D3 ====)\n'
            '= sauce Соус Spicy-X =\n'
            '= filling Мясо бессмертных моллюсков Protostomia =\n'
            '(==== Флюоресцентная булка R2-D3 ====)\n'
            '\n'
            f'Price: {burger.get_price()}'
        )

        assert burger.get_receipt() == expected_receipt