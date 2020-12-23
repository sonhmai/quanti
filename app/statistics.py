from math import ceil

from logging import getLogger

_logger = getLogger(__file__)


def get_percentile(arr, percentile):
    """
    Get percentile of an array/list

    :param arr: list of numbers
    :type arr: list

    :param percentile: percentile number between
    :type percentile: number

    :rtype: Union[int, float]
    """
    if not arr or not isinstance(arr, list):
        raise ValueError('Arr must not be empty')
    if percentile <= 0 or percentile > 100:
        raise ValueError('Invalid percentile %s' % percentile)

    arr = sorted(arr)
    if percentile == 100:
        return arr[-1]
    length = len(arr)
    idx = ceil(percentile * length / 100) - 1
    res = arr[idx]
    _logger.info('%s at index %d is %s percentile of %s.'
                 % (res, idx, percentile, arr))
    return res



