from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DB_FILE_NAME = "todo.db"
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


def get_id(session):
    rows = session.query(Table).all()
    task_id = 0
    for row in rows:
        task_id = max(task_id, row.id)
    return task_id


def main():
    engine = create_engine(f"sqlite:///{DB_FILE_NAME}?check_same_thread=False")
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    task_id = get_id(session) + 1
    while True:
        option = input("1) Today's tasks\n2) Add task\n0) Exit\n")
        if option == "0":
            break
        elif option == "1":
            rows = session.query(Table).all()
            print("\nToday:")
            if not rows:
                print("Nothing to do!")
            else:
                for i, row in enumerate(rows):
                    print(f"{i + 1}) {row}")
        elif option == "2":
            task = input("\nEnter task\n")
            new_row = Table(id=task_id, task=task)
            session.add(new_row)
            session.commit()
            task_id += 1
            print("The task has been added!")
        print()


if __name__ == "__main__":
    main()
