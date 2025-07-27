from typing import Any

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src.application.order.commands.abstract.create_order_command_abstract import (
    CreateOrderCommandAbstract,
)
from src.application.order.queries.abstract.get_all_order_query_abstract import (
    GetAllOrderQueryAbstract,
)
from src.presentation.schemas.order_request_schema import OrderRequestSchema
from src.presentation.schemas.order_response_schema import OrderResponseSchema


class OrderResource(Resource):
    def __init__(self, container: Any) -> Any:
        self.get_all_order_query = container.resolve(GetAllOrderQueryAbstract)
        self.create_order_command = container.resolve(CreateOrderCommandAbstract)
        self.order_request_schema = OrderRequestSchema()
        self.order_response_schema = OrderResponseSchema()

    def get(self) -> Any:
        orders, error = self.get_all_order_query.handle()
        if error:
            return {"error": error}, 404
        return {"orders": orders}, 200

    def post(self) -> Any:
        data = request.json

        if not data:
            return {"error": "No data provided"}, 400

        try:
            data = self.order_request_schema.load(data)
        except ValidationError as err:
            return {"error": err.messages}, 400

        order, error = self.create_order_command.handle(data)

        if error:
            return {"error": error}, 400

        order = self.order_response_schema.dump(order)

        return {"order": order}, 201
