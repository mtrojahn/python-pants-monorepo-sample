from libs.converters import convert_to_string


def test_convert_to_string():
    assert "1" == convert_to_string(1)
