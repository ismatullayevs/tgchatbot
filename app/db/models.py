from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship
from config.settings import settings


Base = declarative_base()
engine = create_engine(settings.DATABASE_URL, echo=True)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='messages')

    reply_to_id = Column(Integer, ForeignKey('messages.id'))
    reply_to = relationship('Message', remote_side=[id], back_populates='replies')

    replies = relationship('Message', back_populates='reply_to', lazy='dynamic')


# Assuming you have an SQLAlchemy engine called `engine`
Base.metadata.create_all(engine)
