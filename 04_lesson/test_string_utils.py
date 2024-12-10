from string_utils import StringUtils

import pytest

class TestStringUtils:
    def setup_method(self):
        self.utils = StringUtils()

    def test_capitilize(self):
        assert self.utils.capitilize("skypro") == "Skypro"
        assert self.utils.capitilize("SkyPro") == "Skypro"
        assert self.utils.capitilize("") == ""

    def test_trim(self):
        assert self.utils.trim("   skypro") == "skypro"
        assert self.utils.trim("skypro") == "skypro"
        assert self.utils.trim("   ") == ""

    def test_to_list(self):
        assert self.utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
        assert self.utils.to_list("1:2:3", ":") == ["1", "2", "3"]
        assert self.utils.to_list("") == []

    def test_contains(self):
        assert self.utils.contains("SkyPro", "S") is True
        assert self.utils.contains("SkyPro", "U") is False
        assert self.utils.contains("", "S") is False

    def test_delete_symbol(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_starts_with(self):
        assert self.utils.starts_with("SkyPro", "S") is True
        assert self.utils.starts_with("SkyPro", "P") is False
        assert self.utils.starts_with("", "S") is False

    def test_end_with(self):
        assert self.utils.end_with("SkyPro", "o") is True
        assert self.utils.end_with("SkyPro", "y") is False
        assert self.utils.end_with("", "o") is False

    def test_is_empty(self):
        assert self.utils.is_empty("") is True
        assert self.utils.is_empty(" ") is True
        assert self.utils.is_empty("SkyPro") is False

    def test_list_to_string(self):
        assert self.utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
        assert self.utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
        assert self.utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
        assert self.utils.list_to_string([]) == ""
