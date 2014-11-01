import pytest
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError

from kuulemma.extensions import db


def assert_unique(factory, field):
    obj = factory()
    obj2 = factory()
    table = inspect(obj2.__class__).columns[field].table
    query = table.update().values(**{field: getattr(obj, field)})
    with pytest.raises(IntegrityError):
        db.session.execute(query)
