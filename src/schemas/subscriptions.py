"""Subscription schemas to assist with sub serialization"""
from marshmallow import fields, Schema, validate

from src.schemas.service_codes import PlanSchema


class SubscriptionSchema(Schema):
    """Schema class to handle serialization of subscription data"""
    id = fields.Integer()
    phone_number = fields.String()

    status = fields.String()
    status_effective_date = fields.DateTime()

    plan_id = fields.String()
    plan = fields.Nested(PlanSchema, dump_only=True)
    service_codes = fields.Method("get_service_codes")

    def get_service_codes(self, obj):
        """field get method to return service code names"""
        return [code.name for code in obj.service_codes]
