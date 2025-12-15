

from .models import Side, Trade
from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.orm import Session

@dataclass(frozen=True)
class TradeOrder:
    instrument: str
    broker: str
    side: Side
    quantity: int
    price: float 
    executed_at: datetime | None = None


def create_trade(db_session: Session, order: TradeOrder):
    trade = Trade(
        instrument=order.instrument,
        broker=order.broker,
        side=order.side,
        quantity=order.quantity,
        price=order.price,
        executed_at=order.executed_at if order.executed_at is not None else None,
    )

    db_session.add(trade)
    db_session.commit()
    db_session.refresh(trade)
    return trade

