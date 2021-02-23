from sqlalchemy import Column, ForeignKey, SmallInteger, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Clas(Base):
    __tablename__ = 'class'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(15), nullable=False)


class Subject(Base):
    __tablename__ = 'subject'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False)


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(SmallInteger, primary_key=True)
    fullname = Column(VARCHAR(20), nullable=False)
    qualification = Column(VARCHAR(20), nullable=False)


class Learningactivity(Base):
    __tablename__ = 'learningactivities'

    idclass = Column(ForeignKey('class.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    idteacher = Column(ForeignKey('teacher.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    idsubject = Column(ForeignKey('subject.id', ondelete='CASCADE'), primary_key=True, nullable=False)

    clas = relationship('Clas')
    subject = relationship('Subject')
    teacher = relationship('Teacher')