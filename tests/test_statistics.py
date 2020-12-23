import pytest

from app.statistics import get_percentile


@pytest.mark.parametrize("arr, percentile, result", [
    ([3, 2, 1, 2], 100, 3),
    ([3, 2, 1, 2], 99, 3),
    ([3, 2, 1, 2], 99.9, 3),
    ([3, 2, 1, 2], 75.1, 3),
    ([3, 2, 1, 2], 74.9, 2),
    ([3, 2, 1, 2], 50, 2),
    ([3, 2, 1, 2], 25.1, 2),
    ([3, 2, 1, 2], 25, 1),
    ([3, 2, 1, 2], 0.1, 1),

    ([1, 7, 2, 6], 25, 1),
    ([1, 7, 2, 6], 26, 2),
    ([1, 7, 2, 6], 49, 2),
    ([1, 7, 2, 6], 50, 2),
    ([1, 7, 2, 6], 99, 7),
    ([1, 7, 2, 6], 75, 6),
    ([1, 7, 2, 6], 75.1, 7),

    ([3, 2, 1, 4, 5], 25, 2),
    ([3, 2, 1, 4, 5], 50, 3),
    ([3, 2, 1, 4, 5], 99, 5),
    ([3, 2, 1, 4, 5], 100, 5),

    ([3, 2, 1], 100, 3),
    ([3, 2, 1], 50, 2),
    ([3, 2, 1], 0.1, 1),

    ([1.4], 0.1, 1.4),
    ([1.4], 3.456, 1.4),
    ([1.4], 25, 1.4),
    ([1.4], 50, 1.4),
    ([1.4], 99.999, 1.4),
    ([1.4], 100, 1.4),
])
def test_quantile(arr, percentile, result):
    assert get_percentile(arr, percentile) == result


@pytest.mark.parametrize("arr, percentile, error", [
    ([3, 2, 1, 2], 0, ValueError),
    ([3, 2, 1, 2], -1, ValueError),
    ([], 10, ValueError),
    ([3, 2, 1, 2], 101, ValueError),
])
def test_invalid_quantile(arr, percentile, error):
    with pytest.raises(error):
        get_percentile(arr, percentile)
