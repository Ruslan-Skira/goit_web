from sqlalchemy import create_engine, Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

note_m2m_tag = Table("note_m2m_tag",
                     Base.metadata,
                     Column("id", Integer, primary_key=True),
                     Column("note_id", Integer, ForeignKey("notes.id", ondelete="CASCADE")),
                     Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"))
)

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(250))
    done = Column(Boolean, default=False)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), nullable=False, unique=True)