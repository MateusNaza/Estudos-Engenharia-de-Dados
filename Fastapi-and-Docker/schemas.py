import datetime as _dt
import pydantic as _pyd


class _BaseContact(_pyd.BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str


class Contact(_BaseContact):
    id: int
    date_created: _dt.datetime

    model_config = _pyd.ConfigDict(from_attributes=True)


class CreateContact(_BaseContact):
    pass
