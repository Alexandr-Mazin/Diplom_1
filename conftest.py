import pytest
from unittest.mock import Mock
from data import DataBan, DataIngredient
from praktikum.database import Database
from praktikum.burger import Burger


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = DataBan.bun_name
    mock_bun.get_price.return_value = DataBan.bun_price
    return mock_bun

@pytest.fixture
def mock_sauce():
    mock_for_sauce = Mock()
    mock_for_sauce.get_name.return_value = DataIngredient.sauce_name
    mock_for_sauce.get_price.return_value = DataIngredient.sauce_price
    mock_for_sauce.get_type.return_value = DataIngredient.sauce_type
    return mock_for_sauce

@pytest.fixture
def mock_filling():
    mock_for_filling = Mock()
    mock_for_filling.get_name.return_value = DataIngredient.filling_name
    mock_for_filling.get_price.return_value = DataIngredient.filling_price
    mock_for_filling.get_type.return_value = DataIngredient.filling_type
    return mock_for_filling

@pytest.fixture
def burger(mock_bun, mock_sauce, mock_filling):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    return burger


@pytest.fixture
def setup():
    database = Database()
    return database