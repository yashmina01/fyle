from core import db
from core.libs import helpers

from core.libs import assertions
from core.models.principals import Principal

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, db.Sequence('teachers_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<Teacher %r>' % self.id

    @classmethod
    def get_teacher_by_id(cls, teacher_id,user_id):
        return cls.query.filter_by(id=teacher_id,user_id=user_id).first()

    @classmethod
    def get_all_teachers(cls, teacher_id, user_id):
        """List of teachers"""
        principal = Teacher.get_teacher_by_id(teacher_id, user_id)
        assertions.assert_auth(Teacher is not None, "Provided user is not a valid principal")
        return cls.query.all()