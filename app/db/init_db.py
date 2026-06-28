from app.db.base import Base
from app.db.session import engine

# IMPORTANT: import models so SQLAlchemy registers them
from app.db.models import Exam, Subject, Topic, PYQ, User


def init_db():
    print("Creating ExamVerseOS tables...")

    Base.metadata.create_all(bind=engine)

    print("All tables created successfully.")


if __name__ == "__main__":
    init_db()