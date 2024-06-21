from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()


class Event(Base):
    __tablename__ = 'event'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()

    def __init__(self,name):
        self.name = name
