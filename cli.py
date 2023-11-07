import click
from database import Session
from models import Student, Course, Enrollment
from validators import validate_name, validate_integer

@click.group()
def main():
    pass

@main.command()
def create_student():
    name = input("Student name: ")
    try:
        validate_name(name)
        session = Session()
        student = Student(name=name)
        session.add(student)
        session.commit()
        session.close()
        click.echo("Student created successfully.")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

@main.command()
def create_course():
    name = input("Course Name: ")
    try:
        validate_name(name)
        session = Session()
        course = Course(name=name)
        session.add(course)
        session.commit()
        session.close()
        click.echo("Course created successfully.")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

@main.command()
def enroll_student():
    student_id = input("Student ID: ")
    course_id = input("Course ID: ")

    try:
        validate_integer(student_id)
        validate_integer(course_id)
        session = Session()
        student = session.query(Student).get(int(student_id))
        course = session.query(Course).get(int(course_id))

        if student and course:
            enrollment = Enrollment(student=student, course=course)
            session.add(enrollment)
            session.commit()
            click.echo("Student enrolled successfully.")
        else:
            click.echo("Error: Student or course not found.")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
