from typing import TYPE_CHECKING, List
import fastapi as _api
import sqlalchemy.orm as _orm
import schemas as _sch
import services as _ser


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _api.FastAPI()

# --- Endpoint que cria um novo contato no banco de dados ---

@app.post("/api/contacts/", response_model=_sch.Contact)
async def create_contact(
    contact: _sch.CreateContact,
    db: _orm.Session = _api.Depends(_ser.get_db),
):
    return await _ser.create_contact(contact=contact, db=db)


# --- Endpoint que retorna os contatos existentes no banco de dados ---

@app.get("/api/contacts/", response_model=List[_sch.Contact])
async def get_contacts(db: _orm.Session = _api.Depends(_ser.get_db)):
    return await _ser.get_all_contacts(db=db)


# --- Endpoint que trás um contato específico pelo seu ID ---

@app.get("/api/contacts/{contact_id}/", response_model=_sch.Contact)
async def get_contact(
    contact_id: int, db: _orm.Session = _api.Depends(_ser.get_db)
):
    contact = await _ser.get_contact(db=db, contact_id=contact_id)
    if contact is None:
        raise _api.HTTPException(status_code=404, detail="Contact does not exist")

    return contact


# --- Endpoint que deleta um contato específico atravéz do seu ID ---

@app.delete("/api/contacts/{contact_id}/")
async def delete_contact(
    contact_id: int, db: _orm.Session = _api.Depends(_ser.get_db)
):
    contact = await _ser.get_contact(db=db, contact_id=contact_id)
    if contact is None:
        raise _api.HTTPException(status_code=404, detail="Contact does not exist")

    await _ser.delete_contact(contact, db=db)

    return "successfully deleted the user"


# --- Endpoint que atualiza/modifica informações de um contato atravéz do seu ID ---

@app.put("/api/contacts/{contact_id}/", response_model=_sch.Contact)
async def update_contact(
    contact_id: int,
    contact_data: _sch.CreateContact,
    db: _orm.Session = _api.Depends(_ser.get_db),
):
    contact = await _ser.get_contact(db=db, contact_id=contact_id)
    if contact is None:
        raise _api.HTTPException(status_code=404, detail="Contact does not exist")

    return await _ser.update_contact(
        contact_data=contact_data, contact=contact, db=db
    )