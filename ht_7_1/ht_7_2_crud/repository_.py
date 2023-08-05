import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.models_ import Group, Student, Lector, Subject, Mark, Base


def get_table(model: str) -> Base:
    match model:
        case "Group":
            return Group
        case "Student":
            return Student
        case "Lector":
            return Lector
        case "Subject":
            return Subject
        case "Mark":
            return Mark
