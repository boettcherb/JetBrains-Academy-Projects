from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

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
        option = input("1) Today's tasks\n2) Week's tasks\n3) All tasks\n"
                       "4) Add task\n0) Exit\n")
        if option == "0":
            break
        elif option == "1":
            today = datetime.today()
            condition = Table.deadline == today.date()
            rows = session.query(Table).filter(condition).all()
            print(f"\nToday {datetime.today().strftime('%d %b')}:")
            if not rows:
                print("Nothing to do!")
            else:
                for i, row in enumerate(rows):
                    print(f"{i + 1}) {row}")
        elif option == "2":
            cur_day = datetime.today().date()
            for _ in range(7):
                print(f"\n{cur_day.strftime('%A %d %b').replace(' 0', ' ')}")
                condition = Table.deadline == cur_day
                rows = session.query(Table).filter(condition).all()
                if not rows:
                    print("Nothing to do!")
                else:
                    for i, row in enumerate(rows):
                        print(f"{i + 1}) {row}")
                cur_day = cur_day + timedelta(days=1)
        elif option == "3":
            rows = session.query(Table).order_by(Table.deadline).all()
            print("\nAll tasks:")
            if not rows:
                print("Nothing to do!")
            else:
                for i, row in enumerate(rows):
                    deadline = row.deadline.strftime('%d %b').lstrip("0")
                    print(f"{i + 1}) {row}. {deadline}")
        elif option == "4":
            task = input("\nEnter task\n")
            deadline = datetime.strptime(input("Enter deadline\n"), "%Y-%m-%d")
            new_row = Table(id=task_id, task=task, deadline=deadline)
            session.add(new_row)
            session.commit()
            task_id += 1
            print("The task has been added!")
        print()
    print("\nBye!")


if __name__ == "__main__":
    main()
