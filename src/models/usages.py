"""Usage related models and database functionality"""
from decimal import Decimal
from src.models.base import db
from src.models.cycles import BillingCycle


class DataUsage(db.Model):
    """Model class to represent data usage record

    Note:
        A daily usage record is created for a subscription each day
        it is active, beginning at midnight UTC timezone.

    """
    __tablename__ = "data_usages"

    id = db.Column(db.Integer, primary_key=True)
    mb_used = db.Column(db.Float, default=0.0)
    from_date = db.Column(db.TIMESTAMP(timezone=True))
    to_date = db.Column(db.TIMESTAMP(timezone=True))

    subscription_id = db.Column(
        db.Integer, db.ForeignKey("subscriptions.id"), nullable=False
    )
    subscription = db.relationship("Subscription", back_populates="data_usages")

    def __repr__(self):  # pragma: no cover
        return (
            f"<{self.__class__.__name__}: {self.id} ({self.subscription_id}) "
            f"{self.mb_used} MB {self.from_date} - {self.to_date}>"
        )
