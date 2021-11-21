from flask import request
from flask_restful import Resource

from core.api.schema.rates import RatesGetInputSchema, RatesGetOutputSchema
from core.models.price import Price


class RatesResource(Resource):
    schema = RatesGetInputSchema()

    def get(self):
        params = self.schema.load(request.args)
        records = Price().get_rates(**params)
        return RatesGetOutputSchema().load(
            [
                {"day": str(day), "average_price": ave if ave else None}
                for day, ave in records
            ],
            many=True,
        )
