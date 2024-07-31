from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from .schema import TeacherSchema

from .schema import 
principal_teacher_resources = Blueprint('principal_teacher_resources', __name__)


@principal_teacher_resources.route('/', method=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """list of all teachers"""
    all_teachers = Teacher.get_all_teachers(principal_id=p.principal_id, user_id=p.user_id)
    teachers_dump = TeacherSchema(data=teachers_dump)