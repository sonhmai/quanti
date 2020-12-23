from flask import Flask
from webargs import fields, validate

from .statistics import get_percentile
from .utils import use_args, IntOrFloat

app = Flask(__name__)

PERCENTILE_LIST_MAX_ELEMENT = 100_000


@app.route('/', methods=['POST'])
@use_args({
    'pool': fields.List(
        IntOrFloat, required=True,
        validate=validate.Length(max=PERCENTILE_LIST_MAX_ELEMENT)),
    'percentile': fields.Number(
        required=True,
        validate=validate.Range(min=0, max=100, min_inclusive=False))
})
def quantile(args):
    pool, percentile = args['pool'], args['percentile']
    result = get_percentile(pool, percentile)
    return {"data": result}
