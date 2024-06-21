from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class CommentModel(Base):
    __tablename__ = 'comentarios'

    columna1 = Column(String, primary_key=True)
    columna2 = Column(String)
    columna3 = Column(String)
    columna4 = Column(String)
    columna5 = Column(String)
    columna6 = Column(String)
    columna7 = Column(String)
    columna8 = Column(String)
    columna9 = Column(String)


class EventModel(Base):
    __tablename__ = 'eventos'
    columna1 = Column(String, primary_key=True)
    columna2 = Column(String)
    columna3 = Column(String)
    columna4 = Column(String)
    columna5 = Column(String)
    columna6 = Column(String)
    columna7 = Column(String)
    columna8 = Column(String)
    columna9 = Column(String)
    columna10 = Column(String)
    columna11 = Column(String)
    columna12 = Column(String)
    columna13 = Column(String)
    columna14 = Column(String)
    columna15 = Column(String)
    columna16 = Column(String)
    columna17 = Column(String)
    columna18 = Column(String)
    columna19 = Column(String)
    columna20 = Column(String)
    columna21 = Column(String)
    columna22 = Column(String)
    columna23 = Column(String)
    columna24 = Column(String)
    columna25 = Column(String)
    columna26 = Column(String)
    columna27 = Column(String)
