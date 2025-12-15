
from app.db import LocalSession, engine
from app.crud import TradeOrder, create_trade
from app.models import Base, Side
from decimal import Decimal


def init_db() -> None:
    Base.metadata.create_all(bind=engine)



def test() -> None:
    with LocalSession() as db_session:
        create_trade(db_session, TradeOrder("AAPL", "BBG", Side.BUY, 10, Decimal("192.3")))


if __name__ == "__main__":
    print("Creating table")
    init_db()
    print("Creation done")
    test()
    print("Added entries")