from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


def get_option(prompt, min_option, max_option):
    while True:
        print(prompt)
        option = input()
        try:
            if min_option <= int(option) <= max_option:
                return int(option)
        except ValueError:
            pass
        print(f"{option} is not an option")


def get_id(session):
    cards = session.query(Flashcard).all()
    if not cards:
        return 0
    return max(f.id for f in session.query(Flashcard).all()) + 1


def get_flashcard(session):
    question, answer = "", ""
    while not question:
        question = input("Question:\n").strip()
    while not answer:
        answer = input("Answer:\n").strip()
    session.add(Flashcard(id=get_id(session), question=question, answer=answer))
    session.commit()


def add_flashcards(session):
    prompt = "1. Add a new flashcard\n2. Exit"
    while True:
        option = get_option(prompt, 1, 2)
        if option == 1:
            print()
            get_flashcard(session)
        elif option == 2:
            break
        print()


def update_card(session, card):
    print('press "d" to delete the flashcard:')
    print('press "e" to edit the flashcard:')
    choice = input()
    if choice == "d":
        session.delete(card)
        session.commit()
    elif choice == "e":
        print(f"current question: {card.question}")
        new_question = input("please write a new question: ").strip()
        if new_question != "":
            card.question = new_question
        print(f"current answer: {card.answer}")
        new_answer = input("please write a new answer: ").strip()
        if new_answer != "":
            card.answer = new_answer
        session.commit()


def practice_flashcards(session):
    flashcards = session.query(Flashcard).all()
    if not flashcards:
        print("\nThere is no flashcard to practice!")
        return
    for card in flashcards:
        print(f"\nQuestion: {card.question}")
        print('press "y" to see the answer:')
        print('press "n" to skip:')
        print('press "u" to update:')
        choice = input()
        if choice == "y":
            print(f"\nAnswer: {card.answer}")
        elif choice == "n":
            print()
        elif choice == "u":
            update_card(session, card)


def main():
    engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    prompt = "1. Add flashcards\n2. Practice flashcards\n3. Exit"
    while True:
        option = get_option(prompt, 1, 3)
        if option == 1:
            print()
            add_flashcards(session)
        elif option == 2:
            practice_flashcards(session)
        elif option == 3:
            break
        print()
    print("\nBye!")


if __name__ == "__main__":
    main()
