"""Usage resource for handling any usage requests"""
from sqlalchemy.sql import func
from webargs import fields
from webargs.flaskparser import use_kwargs
from flask_restful import Resource

from src.models.subscriptions import Subscription
from src.models.usages import DataUsage
from src.models.utils import get_available_data


class SubscriptionDataUsageApi(Resource):
    
    def get(self, sid):
        """External facing subscription endpoint GET

        Gets an existing Subscription Status

        Args:
            sid (int): id of subscription object

        Returns:
            json: serialized data usage object

        """
        try:
            available_limit = get_available_data(Subscription, sid) / 1024
        except Exception as e:
            available_limit = 0.00

        try:
            data_used = DataUsage.query.with_entities(
                    func.sum(DataUsage.mb_used).label('data_used')
                    ).filter(DataUsage.subscription_id == sid).first()[0] / 1024
        except Exception as e:
            data_used = 0.00

        if data_used >= available_limit:
            status = 'Data Limit Exhausted'
            available_limit = 0.00
        else:
            status = 'Plan Active'
            available_limit = available_limit - data_used
        
        result = {   
            'subscription_id': sid,
            'available_limit': "{} GB".format(available_limit),
            'data_used': "{} GB".format(data_used),
            'status': status,
        }
        return result

