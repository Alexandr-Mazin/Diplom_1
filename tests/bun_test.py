from data import DataBan
from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun(DataBan.bun_name, DataBan.bun_price)
        assert bun.get_name() == DataBan.bun_name

    def test_get_price(self):
        bun = Bun(DataBan.bun_name, DataBan.bun_price)
        assert bun.get_price() == DataBan.bun_price