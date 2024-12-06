import database as _dt
import models as _mds

def _add_table():
    return _dt.Base.metadata.create_all(bind=_dt.engine)

