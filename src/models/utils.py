"""Utilities for models to inherit or use"""
from sqlalchemy.exc import SQLAlchemyError
from flask import abort
from http import HTTPStatus

from src.models.service_codes import Plan


def get_object_or_404(model, mid):
    """Get an object by id or return a 404 not found response

    Args:
        model (object): object's model class
        mid (int): object's id

    Returns:
        object: returned from query

    Raises:
        404: if one object is returned from query

    """
    try:
        return model.query.get(mid)
    except SQLAlchemyError:
        abort(404)


def get_available_data(model, sid):

    """ Get data available for a plan from subscription

    Args: 
        model: Subscription, Plan
        sid = subscription id

    Return:
        float: data available from query
    
    """
    try:
        plan_id = model.query.get(sid).plan_id
        data_available = Plan.query.get(plan_id).mb_available
        return data_available
    except SQLAlchemyError:
        abort(404)
