from database import create_connection
from models import Blog, Base

if __name__ == "__main__":
    engine = create_connection()

    Base.metadata.create_all(engine)

    blog = Blog(name="Test")
    session.add(blog)
    session.comit()
