from sqlalchemy import Column, Integer, Float, String, Date, Boolean, ForeignKey, Enum, func, distinct
from sqlalchemy.orm import relationship
from StudentManage import db
from datetime import datetime
from flask_login import UserMixin
import hashlib


# class Ministry(db.Model):
#     __tablename__='Giáo Vụ'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
# class Student(db.Model):
#     __tablename__='Học Sinh'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
#     male = Column(Enum('Male', 'Female'))
#     birthday = Column(Date)
#     address = Column(String(100))
#     phoneNumber = Column(String(10))
#     email = Column(String(100))
# class Class(db.Model):
#     __tablename__ = 'Lớp Học'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
#     numbers=Column(Integer)
# class Account(db.Model):
#     __tablename__ = 'Tài Khoản'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(String(100), nullable=False, unique=True)
#     password = Column(String(100), nullable=False)
#     role = Column(String(50), nullable=False)
# class Teacher (db.Model):
#     __tablename__ = 'Giáo Viên'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
# class Scores(db.Model):
#     __tablename__ = 'Điểm Số'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     score_15= Column(Float,nullable=False)
#     score_45=Column(Float,nullable=False)
#     semester = Column(Enum('1', '2'))
# class Subjects(db.Model):
#     __tablename__ = 'Môn Học'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
# class Regulation(db.Model):
#     __tablename__ = 'Quy đinh'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     course = Column(Integer, nullable=False)
#     name = Column(String(50), nullable=False)
#     value = Column(Integer, nullable=False)
# class Manager(db.Model):
#     id =
# class Subject(db.Model):
#     __tablename__ = 'Subject'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
#     Account = relationship('Account', backref='subject', lazy=True)
#     scores = relationship('Scores', backref='subject', lazy=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Account(db.Model, UserMixin):
#     __tablename__ = 'Account'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(String(100), nullable=False, unique=True)
#     password = Column(String(100), nullable=False)
#     firstname = Column(String(100), nullable=False)
#     lastname = Column(String(100), nullable=False)
#     admin = Column(Boolean, default=False)
#     active = Column(Boolean, default=True)
#     subject_id = Column(Integer, ForeignKey(Subject.id))
#
#     def __str__(self):
#         return self.firstname + ' ' + self.lastname
#
#
# class Test(db.Model):
#     __tablename__ = 'Test'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False, unique=True)
#     scores = relationship('Scores', backref='test', lazy=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Class(db.Model):
#     __tablename__ = 'Class'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     course = Column(Integer, nullable=False)
#     grade = Column(Enum('10', '11', '12'))
#     name = Column(String(10), nullable=False)
#     students = relationship('Student', backref='class', lazy=True)
#
#     def __str__(self):
#         return self.grade + 'A' + self.name
#
#
# class Teach(db.Model):
#     teacher_id = Column(Integer, ForeignKey(Account.id), primary_key=True)
#     class_id = Column(Integer, ForeignKey(Class.id), primary_key=True)
#
#
# class Student(db.Model):
#     __tablename__ = 'Student'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     firstname = Column(String(100), nullable=False)
#     lastname = Column(String(100), nullable=False)
#     fullname = Column(String(200), nullable=False)
#     male = Column(Enum('Male', 'Female'))
#     birthday = Column(Date)
#     address = Column(String(100))
#     email = Column(String(100))
#     class_id = Column(Integer, ForeignKey(Class.id))
#     scores = relationship('Scores', backref='student', lazy=True)
#
#     def __str__(self):
#         return self.firstname + ' ' + self.lastname
#
#
# class Scores(db.Model):
#     __tablename__ = 'Scores'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
#     subject_id = Column(Integer, ForeignKey(Subject.id), nullable=False)
#     test_id = Column(Integer, ForeignKey(Test.id), nullable=False)
#     scores = Column(Float, nullable=False)
#     semester = Column(Enum('1', '2'))
#     date_create = Column(Date, default=datetime.now())
#
#
# class Rule(db.Model):
#     __tablename__ = 'regulation'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     course = Column(Integer, nullable=False)
#     name = Column(String(50), nullable=False)
#     value = Column(Integer, nullable=False)


class Subject(db.Model):
    __tablename__ = 'Subject'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    Account = relationship('Account', backref='subject', lazy=True)
    scores = relationship('Scores', backref='subject', lazy=True)

    def __str__(self):
        return self.name


class Account(db.Model, UserMixin):
    __tablename__ = 'Account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    admin = Column(Boolean, default=False)
    active = Column(Boolean, default=True)
    subject_id = Column(Integer, ForeignKey(Subject.id))

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Test(db.Model):
    __tablename__ = 'Test'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    scores = relationship('Scores', backref='test', lazy=True)

    def __str__(self):
        return self.name


class Class(db.Model):
    __tablename__ = 'Class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(Integer, nullable=False)
    grade = Column(Enum('10', '11', '12'))
    name = Column(String(10), nullable=False)
    students = relationship('Student', backref='class', lazy=True)

    def __str__(self):
        return self.grade + 'A' + self.name


class Teach(db.Model):
    teacher_id = Column(Integer, ForeignKey(Account.id), primary_key=True)
    class_id = Column(Integer, ForeignKey(Class.id), primary_key=True)


class Student(db.Model):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    fullname = Column(String(200), nullable=False)
    male = Column(Enum('Male', 'Female'))
    birthday = Column(Date)
    address = Column(String(100))
    email = Column(String(100))
    class_id = Column(Integer, ForeignKey(Class.id))
    scores = relationship('Scores', backref='student', lazy=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Scores(db.Model):
    __tablename__ = 'Scores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
    subject_id = Column(Integer, ForeignKey(Subject.id), nullable=False)
    test_id = Column(Integer, ForeignKey(Test.id), nullable=False)
    scores = Column(Float, nullable=False)
    semester = Column(Enum('1', '2'))
    date_create = Column(Date, default=datetime.now())


class Regulation(db.Model):
    __tablename__ = 'regulation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    value = Column(Integer, nullable=False)
if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # Tao subject
    subject1 = Subject(name='Math')
    subject2 = Subject(name='History')
    db.session.add_all([subject1, subject2])
    db.session.commit()

    # Tao account
    admin = Account(username='admin',
                    password=hashlib.md5('123'.strip().encode("utf-8")).hexdigest(),
                    firstname='admin',
                    lastname='admin',
                    admin=True)
    gv = Account(username='gv',
                 password=hashlib.md5('123'.strip().encode("utf-8")).hexdigest(),
                 firstname='gv',
                 lastname='gv')
    db.session.add_all([admin, gv])
    db.session.commit()

    # Tao class

    class10 = Class(course=2, grade='10', name='Lop 10')
    class1 = Class(course=1, grade='11', name='Lop 11')
    class2 = Class(course=2, grade='12', name='Lop 12')
    db.session.add_all([class10, class1, class2])
    db.session.commit()

    # Tao teach
    teach1 = Teach(teacher_id=gv.id, class_id=class1.id)
    teach2 = Teach(teacher_id=gv.id, class_id=class2.id)
    teach3 = Teach(teacher_id=gv.id, class_id=class10.id)
    db.session.add_all([teach1, teach2, teach3])
    db.session.commit()

    # Tao Student them vao Class
    student1 = Student(firstname='Thanh', lastname='Dat',
                       fullname='Thanh Dat', male='Male',
                       class_id=class1.id)
    student2 = Student(firstname='Sieu', lastname='Nhan',
                       fullname='Sieu Nhan', male='Male',
                       class_id=class1.id)
    student3 = Student(firstname='Phu', lastname='Nu',
                       fullname='Phu Nu', male='Female',
                       class_id=class1.id)
    student4 = Student(firstname='Nguyen', lastname='A',
                       fullname='Nguyen A', male='Female',
                       class_id=class2.id)
    student5 = Student(firstname='Nguyen', lastname='B',
                       fullname='Nguyen B', male='Female',
                       class_id=class2.id)
    student6 = Student(firstname='Nguyen', lastname='C',
                       fullname='Phu Nu', male='Female',
                       class_id=class10.id)

    db.session.add_all([student1, student2, student3, student4, student5, student6])
    db.session.commit()

    # Tao test
    test1 = Test(name='Kiem tra 1')
    db.session.add_all([test1, ])
    db.session.commit()

    # Tao score
    score1 = Scores(student_id=student1.id,
                    subject_id=subject1.id,
                    test_id=test1.id,
                    scores=8.2,
                    semester='1')
    score2 = Scores(student_id=student1.id,
                    subject_id=subject1.id,
                    test_id=test1.id,
                    scores=5,
                    semester='1')
    score3 = Scores(student_id=student1.id,
                    subject_id=subject1.id,
                    test_id=test1.id,
                    scores=7,
                    semester='2')

    score4 = Scores(student_id=student2.id,
                    subject_id=subject1.id,
                    test_id=test1.id,
                    scores=1,
                    semester='1')
    score5 = Scores(student_id=student2.id,
                    subject_id=subject1.id,
                    test_id=test1.id,
                    scores=2,
                    semester='1')
    db.session.add_all([score1, score2, score3, score4, score5])
    db.session.commit()

    # Them rule
    rule1 = Regulation(course=1, name='MinAge', value='17')
    rule2 = Regulation(course=1, name='MaxAge', value='20')
    rule3 = Regulation(course=1, name='MaxPopulation', value='40')
    db.session.add_all([rule1, rule2, rule3])
    db.session.commit()

    # db.drop_all()
    # db.create_all()
#
#     # Tao subject
#     subject1 = Subjects(name='Math')
#     subject2 = Subjects(name='History')
#     subject3 = Subjects(name='English')
#     db.session.add_all([subject1, subject2,subject3])
#     db.session.commit()
#
#     # Tao account
#     admin = Account(username='admin',
#                     password=hashlib.md5('123'.strip().encode("utf-8")).hexdigest(),
#                     admin=True,is_active=True)
#
#     gv = Account(username='gv',
#                     password=hashlib.md5('123'.strip().encode("utf-8")).hexdigest(),
#                     admin = False,is_active=True)
#     minister= Account(username='mini',
#                     password=hashlib.md5('123'.strip().encode("utf-8")).hexdigest(),
#                     admin=False,is_active=True)
#     db.session.add_all([admin, gv, minister])
#     db.session.commit()
# #
#
#
#     # Tao class
#
#     class10 = Class(name='Lop10A1', grade='10', numbers=40)
#     class11 = Class(name='Lop11A1', grade='11', numbers=40)
#     class12 = Class(name='Lop12A1', grade='12', numbers=40)
#     db.session.add_all([class10, class11, class12])
#     db.session.commit()
#
#     # Tao teacher
#     teacher1 = Teacher(name='Ho Huong Thien10', account_id=gv.id)
#     teacher2 = Teacher(name='Ho Huong Thien11', account_id=gv.id)
#     teacher3 = Teacher(name='Ho Huong Thien12', account_id=gv.id)
#     db.session.add_all([teacher1, teacher2, teacher3])
#     db.session.commit()
# #
# #     Tao Student them vao Class
#     student1 = Student(name='Son Duy1', birthday='2003/2/22',address='Sai Gon', phoneNumber='0222331131', email='sonduy123@gmail.com', male='Male', class_id=class10.id)
#     student2 = Student(name='Son Duy1', birthday='2003/2/22',address='Sai Gon', phoneNumber='0222331131', email='sonduy123@gmail.com', male='Male', class_id=class11.id)
#     student3 = Student(name='Son Duy1', birthday='2003/2/22',address='Sai Gon', phoneNumber='0222331131', email='sonduy123@gmail.com', male='Male', class_id=class12.id)
#
#
#     db.session.add_all([student1, student2, student3])
#     db.session.commit()
# #
# #     # Tao test
# #     test1 = Test(name='Kiem tra 1')
# #     db.session.add_all([test1, ])
# #     db.session.commit()
# #
# #     # Tao score
#     score1 = Scores(score_15=8.2,
#                     score_45 = 8.3,
#                     score_final = 9,
#                     semester='1',
#                     student_id=student1.id,
#                     subject_id=subject1.id,
#                     )
#     score2 = Scores(score_15=8.2,
#                     score_45 = 8.3,
#                     score_final=9,
#                     semester='1',
#                     student_id=student2.id,
#                     subject_id=subject1.id,
#                     )
#     score3 = Scores(score_15=8.2,
#                     score_45 = 8.3,
#                     score_final=9.2,
#                     semester='1',
#                     student_id=student3.id,
#                     subject_id=subject3.id,
#                     )
#
#     db.session.add_all([score1, score2, score3])
#     db.session.commit()
#         #Tạo subject
#     # Them rule
#     rule1 = Regulation(course=1, name='MinAge', value='17')
#     rule2 = Regulation(course=2, name='MaxAge', value='20')
#     rule3 = Regulation(course=3, name='MaxPopulation', value='40')
#     db.session.add_all([rule1, rule2, rule3])
#     db.session.commit()