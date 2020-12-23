import random

import pytest

from app.api import app, PERCENTILE_LIST_MAX_ELEMENT
from app.statistics import get_percentile

ENDPOINT_PERCENTILE = '/'


def get_test_client():
    return app.test_client()


@pytest.mark.parametrize("arr, percentile", [
    ([1, 3, 2], 50),
    ([1, 3, 2], 100),
    ([1, 3, 2], 1.3),
    ([1, 3, 2], 75.7),
    (list(range(100000)), 66)
])
def test_percentile_valid(arr, percentile):
    response = get_test_client().post(
        ENDPOINT_PERCENTILE,
        json={'pool': arr, 'percentile': percentile}
    )
    js = response.get_json()
    assert response.status_code == 200
    assert js['data'] == get_percentile(arr, percentile)


@pytest.mark.parametrize("js", [
    None,
    {'pool': [1, 2, 3]},
    {'quantile': 33},
    {'pool': [1, 2, 3], 'quantile': 33},
    {'percentile': 34},
    {'pool': [1, 2, "hey"], 'percentile': 34},
    {'array': [1, 2], 'percentile': 50},
    {'pool': [1, 2], 'percentile': 101},
    {'pool': [1, 2], 'percentile': 0},
    {'pool': [1, 2], 'percentile': 'invalid'},
    {'pool': random.sample(
        range(PERCENTILE_LIST_MAX_ELEMENT + 1),
        PERCENTILE_LIST_MAX_ELEMENT + 1),
        'percentile': 20}
])
def test_percentile_invalid(js):
    response = get_test_client().post(
        ENDPOINT_PERCENTILE,
        json=js
    )
    assert response.status_code == 400
