from tools.db.handler import get_db
from tools.db.schemas import GuildMainBase, ModrolesBase, ManagerRolesBase, ModlogBase, ModRolesBase, ManagerRolesBase, ModlogBase
from tools.db.models import Guild_Main, Mod_Roles, Manager_Roles, Modlog
from typing import List
from sqlalchemy.orm import Session

# Getters, Creaters, Updaters and Deleters for Guild_Main, Mod_Roles, Manager_Roles, and Modlog

# Getters

def get_guild_main(query: dict) -> List[GuildMainBase]:
    db = get_db()

    result: List[GuildMainBase] = db.query(Guild_Main).filter_by(**query).all()
    return result if result else None

def get_mod_roles(query: dict) -> List[ModRolesBase]:
    db = get_db()

    result: List[ModRolesBase] = db.query(Mod_Roles).filter_by(**query).all()
    return result if result else None

def get_manager_roles(query: dict) -> List[ManagerRolesBase]:
    db = get_db()

    result: List[ManagerRolesBase] = db.query(Manager_Roles).filter_by(**query).all()
    return result if result else None

def get_modlog(query: dict) -> List[ModlogBase]:
    db = get_db()

    result: List[ModlogBase] = db.query(Modlog).filter_by(**query).all()
    return result if result else None
    





# Creaters
def create_guild_main(**data):
    guild_main = GuildMainBase(**data)
    db = get_db()

    # Check if the guild already exists
    existing_guild = db.query(Guild_Main).filter_by(guild_id=guild_main.guild_id).first()
    if existing_guild:
        yield existing_guild  # Yield the existing guild if it already exists
        raise ValueError("Guild already exists")

    db.add(guild_main)
    db.commit()
    db.refresh(guild_main)
    return guild_main

def create_mod_roles(**data) -> ModrolesBase:
    mod_roles = ModrolesBase(**data)
    db = get_db()

    # Check if the mod role already exists
    existing_role = db.query(Mod_Roles).filter_by(guild_id=mod_roles.guild_id, role_id=mod_roles.role_id).first()
    if existing_role:
        yield existing_role  # Yield the existing role if it already exists
        raise ValueError("Mod role already exists")

    db.add(mod_roles)
    db.commit()
    db.refresh(mod_roles)
    return mod_roles

def create_manager_roles(**data) -> ManagerRolesBase:
    manager_roles = ManagerRolesBase(**data)
    db = get_db()

    # Check if the manager role already exists
    existing_role = db.query(Manager_Roles).filter_by(guild_id=manager_roles.guild_id, role_id=manager_roles.role_id).first()
    if existing_role:
        yield existing_role  # Yield the existing role if it already exists
        raise ValueError("Manager role already exists")

    db.add(manager_roles)
    db.commit()
    db.refresh(manager_roles)
    return manager_roles

def create_modlog(**data) -> ModlogBase:
    modlog = ModlogBase(**data)
    db = get_db()

    # Check if the modlog already exists
    existing_log = db.query(Modlog).filter_by(guild_id=modlog.guild_id, log_id=modlog.case_no).first()
    if existing_log:
        yield existing_log  # Yield the existing log if it already exists
        raise ValueError("Modlog already exists")

    db.add(modlog)
    db.commit()
    db.refresh(modlog)
    return modlog







# Deleters

def delete_data(db: Session, item):
    db.delete(item)
    db.commit()

def delete_guild_main(guild: GuildMainBase):
    db = get_db()
    delete_data(db, guild)

def delete_mod_roles(mod_role: ModRolesBase):
    db = get_db()
    delete_data(db, mod_role)

def delete_manager_roles(manager_role: ManagerRolesBase):
    db = get_db()
    delete_data(db, manager_role)

def delete_modlog(modlog: ModlogBase):
    db = get_db()
    delete_data(db, modlog)