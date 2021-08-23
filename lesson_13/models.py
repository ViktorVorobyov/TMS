from sqlalchemy import Integer, String, Column, ForeignKey, Text, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # One-To-One relation to User
    user = relationship("User", back_populates="blog", uselist=False)

    # One-To-Many relation to Articles
    articles = relationship("Article", back_populates="blog")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)

    blog_id = Column(Integer, ForeignKey("blog.id"), nullable=False)
    blog = relationship("Blog", back_populates="user", uselist=False)


article_tags = Table(
    "article_tags", Base.metadata,
    Column("article_id", ForeignKey("article.id")),
    Column("tag_id", ForeignKey('tag.id'))
)


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(Text)

    blog_id = Column(Integer, ForeignKey("blog.id"), nullable=False)
    blog = relationship("Blog", back_populates="articles")

    tags = relationship("Tag", secondary=article_tags)


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True)
    title = Column(String)