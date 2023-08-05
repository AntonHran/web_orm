from sqlalchemy import and_, func, desc

from src.db_connection_ import session
from src.models_ import Student, Lector, Group, Subject, Mark


def select_1(number: int):
    students = (
        (
            session.query(
                Student.first_name,
                Student.last_name,
                func.round(func.avg(Mark.grade), 2).label("avg_grade"),
            )
            .select_from(Mark)
            .join(Student)
            .group_by(Student.id)
        )
        .order_by(desc("avg_grade"))
        .limit(number)
        .all()
    )
    [print(student) for student in students]


def select_2(subj_id: int):
    student = (
        (
            session.query(
                Student.first_name,
                Student.last_name,
                func.round(func.avg(Mark.grade), 2).label("avg_grade"),
            )
            .select_from(Mark)
            .join(Student)
            .join(Subject)
            .where(Subject.id == subj_id)
            .group_by(Student.id)
        )
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )
    print(student)


def select_3(subj_id: int):
    average_grade = (
        (
            session.query(
                Group.group_name,
                Subject.subject_name,
                func.round(func.avg(Mark.grade), 2).label("avg_grade"),
            )
            .select_from(Mark)
            .join(Student)
            .join(Group)
            .join(Subject)
            .where(Subject.id == subj_id)
            .group_by(Group.group_name, Subject.subject_name)
        )
        .order_by(desc("avg_grade"))
        .all()
    )
    [print(res) for res in average_grade]


def select_4():
    avg_grade = session.query(
        func.round(func.avg(Mark.grade), 2).label("avg_grade")
    ).all()
    print(avg_grade)


def select_5(lector_id: int):
    lectors_subjects = (
        session.query(Lector.id, Subject.subject_name)
        .select_from(Subject)
        .join(Lector)
        .where(Lector.id == lector_id)
        .order_by(Subject.subject_name)
        .all()
    )
    [print(subject) for subject in lectors_subjects]


def select_6(group_id: int):
    students_group = (
        session.query(Student.id, Student.first_name, Student.last_name)
        .select_from(Student)
        .join(Group)
        .where(Group.id == group_id)
        .order_by(Student.id)
        .all()
    )
    [print(student) for student in students_group]


def select_7(group_id: int, subj_id: int):
    grade_by_sub_in_group = (
        session.query(
            Student.id,
            Student.first_name,
            Student.last_name,
            Subject.subject_name,
            Mark.grade,
            Mark.lesson_date,
            Group.group_name,
        )
        .select_from(Student)
        .join(Mark)
        .join(Subject)
        .join(Group)
        .filter(and_(Group.id == group_id, Subject.id == subj_id))
        .all()
    )
    [print(grade) for grade in grade_by_sub_in_group]


def select_8(lector_id: int):
    average_grade_for_sub = (
        session.query(
            Subject.subject_name,
            func.round(func.avg(Mark.grade), 2).label("avg_grade"),
        )
        .select_from(Mark)
        .join(Subject)
        .join(Lector)
        .filter(Lector.id == lector_id)
        .group_by(Subject.subject_name)
        .order_by(desc("avg_grade"))
        .all()
    )
    [print(grade) for grade in average_grade_for_sub]


def select_9(st_id: int):
    student_subjects = (
        session.query(
            Subject.subject_name,
        )
        .select_from(Subject)
        .join(Mark)
        .join(Student)
        .filter(Student.id == st_id)
        .group_by(Subject.subject_name)
        .order_by(Subject.subject_name)
        .all()
    )
    [print(subject) for subject in student_subjects]


def select_10(st_id: int, lector_id: int):
    student_subjects_of_lector = (
        session.query(
            Subject.subject_name,
            Lector.get_full_name,
        )
        .select_from(Subject)
        .join(Mark)
        .join(Student)
        .join(Lector)
        .filter(and_(Student.id == st_id, Lector.id == lector_id))
        .group_by(Subject.subject_name, Lector.get_full_name)
        .order_by(Subject.subject_name)
        .all()
    )
    [print(subject) for subject in student_subjects_of_lector]


def select_11(st_id: int, lector_id: int):
    student_avg_grade_from_lector = (
        session.query(
            func.round(func.avg(Mark.grade), 2).label("avg_grade"),
            Subject.subject_name,
            Student.get_full_name,
            Lector.get_full_name,
        )
        .select_from(Student)
        .join(Mark)
        .join(Subject)
        .join(Lector)
        .filter(and_(Student.id == st_id, Lector.id == lector_id))
        .group_by(Subject.subject_name, Student.get_full_name, Lector.get_full_name)
        .order_by(desc("avg_grade"))
        .all()
    )
    [print(avg_gr) for avg_gr in student_avg_grade_from_lector]


def select_12(group_id: int, subj_id: int):
    subquery = (session.query(func.max(Mark.lesson_date), Subject.subject_name)
                .select_from(Mark)
                .join(Subject)
                .filter(Subject.id == subj_id)
                .group_by(Subject.subject_name)
                .all())
    print(subquery)

    students_subject_grades_last_lesson = (
        session.query(
            Mark.grade,
            Student.get_full_name,
            Subject.subject_name,
            Group.group_name,
            Mark.lesson_date,
        ).select_from(Mark)
        .join(Student)
        .join(Group)
        .join(Subject)
        .filter(and_(Group.id == group_id, Subject.id == subj_id, Mark.lesson_date == subquery[0][0]))
        .group_by(Mark.grade, Subject.subject_name, Student.get_full_name, Group.group_name, Mark.lesson_date)
        .order_by(Mark.grade)
        .all()
    )
    [print(grade) for grade in students_subject_grades_last_lesson]


if __name__ == "__main__":
    select_1(5)
    select_2(1)
    select_3(2)
    select_4()
    select_5(1)
    select_6(1)
    select_7(1, 2)
    select_8(3)
    select_9(10)
    select_10(1, 2)
    select_11(1, 2)
    select_12(3, 2)
