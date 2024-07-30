from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

student_assignments_resources = Blueprint('principal_teacher_resources', __name__)