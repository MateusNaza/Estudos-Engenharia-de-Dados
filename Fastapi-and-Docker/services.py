from typing import TYPE_CHECKING
import database as _db
import models as _mds
import schemas as _sch


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _db.Base.metadata.create_all(bind=_db.engine)


def _drop_tables():
    return _db.Base.metadata.drop_all(bind=_db.engine)


def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_contact(
    contact: _sch.CreateContact, db: "Session"
) -> _sch.Contact:
    contact = _mds.Contact(**contact.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return _sch.Contact.from_orm(contact)


async def get_all_contacts(db: "Session") -> list[_sch.Contact]:
    contacts = db.query(_mds.Contact).all()
    return list(map(_sch.Contact.from_orm, contacts))


async def get_contact(contact_id: int, db: "Session"):
    contact = db.query(_mds.Contact).filter(_mds.Contact.id == contact_id).first()
    return contact


async def delete_contact(contact: _mds.Contact, db: "Session"):
    db.delete(contact)
    db.commit()


async def update_contact(
    contact_data: _sch.CreateContact, contact: _mds.Contact, db: "Session"
) -> _sch.Contact:
    contact.first_name = contact_data.first_name
    contact.last_name = contact_data.last_name
    contact.email = contact_data.email
    contact.phone_number = contact_data.phone_number

    db.commit()
    db.refresh(contact)

    return _sch.Contact.from_orm(contact)


