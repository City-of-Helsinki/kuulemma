from factory import Factory

from kuulemma.extensions import db


class SQLAlchemyModelFactory(Factory):
    ABSTRACT_FACTORY = True

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        """Create an instance of the model, and save it to the database."""

        obj = target_class(*args, **kwargs)
        db.session.add(obj)
        db.session.flush()
        return obj
