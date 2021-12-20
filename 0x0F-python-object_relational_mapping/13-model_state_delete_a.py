#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
Base = declarative_base()

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State):
        if 'a' in state.name:
            session.delete(state)
            session.commit()
    session.close()
