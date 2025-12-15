
from enum import Enum as em
from datetime import datetime, timezone
from sqlalchemy import (
    String,
    Numeric,
    DateTime,
    Enum,
    Index,
    Integer
)


from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column
)

class Base(DeclarativeBase):
    pass


class Side(em):
    BUY = "BUY"
    SELL = "SELL"


class Trade(Base):
    __tablename__ = "trades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    instrument: Mapped[str] = mapped_column(String(32), nullable=False)
    broker: Mapped[str] = mapped_column(String(64), nullable=False)

    side: Mapped[Side] = mapped_column(Enum(Side, name="side_enum"), nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    price: Mapped[float] = mapped_column(Numeric(18, 6), nullable=False)

    executed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))


Index("ix_trades_instrument", Trade.instrument)
Index("ix_trades_executed_at", Trade.executed_at)
Index("ix_broker", Trade.broker)


