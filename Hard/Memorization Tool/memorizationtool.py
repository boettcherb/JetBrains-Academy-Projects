from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    box = Column(Integer)


def get_option(prompt, options):
    while True:
        print(prompt)
        option = input()
        try:
            if option in options:
                return option
            if int(option) in options:
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
    session.add(Flashcard(id=get_id(session), question=question,
                          answer=answer, box=1))
    session.commit()


def add_flashcards(session):
    prompt = "1. Add a new flashcard\n2. Exit"
    while True:
        option = get_option(prompt, (1, 2))
        if option == 1:
            print()
            get_flashcard(session)
        elif option == 2:
            break
        print()


def update_card(session, card):
    prompt = 'press "d" to delete the flashcard:\n' \
             'press "e" to edit the flashcard: '
    option = get_option(prompt, ("d", "e"))
    if option == "d":
        session.delete(card)
        session.commit()
    else:
        print(f"current question: {card.question}")
        new_question = input("please write a new question: ").strip()
        if new_question != "":
            card.question = new_question
        print(f"current answer: {card.answer}")
        new_answer = input("please write a new answer: ").strip()
        if new_answer != "":
            card.answer = new_answer
        session.commit()


def ask_if_correct(session, card):
    prompt = 'press "y" if your answer is correct:\n' \
             'press "n" if your answer is wrong:'
    option = get_option(prompt, ("y", "n"))
    if option == "y":
        if card.box == 3:
            session.delete(card)
        else:
            card.box += 1
    else:
        card.box = 1
    session.commit()


def practice_flashcards(session):
    flashcards = session.query(Flashcard).all()
    if not flashcards:
        print("\nThere is no flashcard to practice!")
        return
    for card in flashcards:
        print(f"\nQuestion: {card.question}")
        prompt = 'press "y" to see the answer:\npress "n" to skip:\n' \
                 'press "u" to update:'
        option = get_option(prompt, ("y", "n", "u"))
        if option == "y":
            print(f"\nAnswer: {card.answer}")
            ask_if_correct(session, card)
        elif option == "n":
            ask_if_correct(session, card)
        else:
            update_card(session, card)


def main():
    engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    prompt = "1. Add flashcards\n2. Practice flashcards\n3. Exit"
    while True:
        option = get_option(prompt, (1, 2, 3))
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
