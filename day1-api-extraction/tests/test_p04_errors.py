from katas.p04_errors import FetchError
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("7", None, 7),
        ("3.5", None, None),
        (None, 0, 0),
        ("abc", -1, -1),
    ]
)



def test_error_handling(a, b, expected):
    value = FetchError
    assert value.to_int(a, b) == expected
    