from data import DataBan, DataIngredient

class TestIngredient:

    def test_get_name_sauce_success(self, mock_sauce):
        assert mock_sauce.get_name() == DataIngredient.sauce_name

    def test_get_name_filling_success(self, mock_filling):
        assert mock_filling.get_name() == DataIngredient.filling_name

    def test_get_type_sauce_success(self, mock_sauce):
        assert mock_sauce.get_type() == DataIngredient.sauce_type

    def test_get_type_filling_success(self, mock_filling):
        assert mock_filling.get_type() == DataIngredient.filling_type

    def test_get_price_sauce_success(self, mock_sauce):
        assert mock_sauce.get_price() == DataIngredient.sauce_price

    def test_get_price_filling_success(self, mock_filling):
        assert mock_filling.get_price() == DataIngredient.filling_price