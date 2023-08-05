from sqlalchemy import Integer, String, Column, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(10), nullable=False)
    students_ = relationship('Student', back_populates='group_')


class Lector(Base):
    __tablename__ = 'lectors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(40), nullable=False)
    phone = Column(String(25), nullable=False)
    address = Column(String(100), nullable=False)
    start_work = Column(Date, nullable=False)
    subjects_ = relationship('Subject', back_populates='lector_')
    
    @hybrid_property
    def get_full_name(self):
        return self.first_name+' '+self.last_name


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(40), nullable=False)
    phone = Column(String(25), nullable=False)
    address = Column(String(100), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE'))
    group_ = relationship('Group', back_populates='students_')
    
    @hybrid_property
    def get_full_name(self):
        return self.first_name+' '+self.last_name

    @hybrid_property
    def get_contacts(self):
        return 'Phone: '+self.phone+', email: '+self.email+', address: '+self.address


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(50), nullable=False)
    lector_id = Column(Integer, ForeignKey('lectors.id', ondelete='CASCADE'))
    lector_ = relationship('Lector', back_populates='subjects_')


class Mark(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    grade = Column(Integer, nullable=False)
    lesson_date = Column(Date, nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'))
    student_ = relationship('Student', backref='grade')
    subject_ = relationship('Subject', backref='grade')
