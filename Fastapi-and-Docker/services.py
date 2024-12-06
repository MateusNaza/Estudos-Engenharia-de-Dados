import database as _dt
import models as _mds

def _add_tables():
    return _dt.Base.metadata.create_all(bind=_dt.engine)

def _drop_tables():
    return _dt.Base.metadata.drop_all(bind=_dt.engine)
