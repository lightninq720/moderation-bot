from sqlalchemy import Column, Integer, String, DateTime, Text, BigInteger, Boolean, VARCHAR, ForeignKey
from tools.db.handler import Base
from datetime import datetime


class Guild_Main(Base):
    __tablename__ = "guild_main"

    guild_id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    prefix = Column(VARCHAR, default="!", nullable=False)
    log_id = Column(BigInteger, nullable=True)
    mute_role_id = Column(BigInteger, nullable=True)

class Mod_Roles(Base):
    __tablename__ = "mod_roles"

    guild_id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    role_id = Column(BigInteger, primary_key=True, unique=True, nullable=False)

class Manager_Roles(Base):
    __tablename__ = "manager_roles"

    guild_id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    role_id = Column(BigInteger, primary_key=True, unique=True, nullable=False)

class Modlog(Base):
    __tablename__ = "modlog"

    case_no = Column(Integer, primary_key=True, nullable=False)
    guild_id = Column(BigInteger, primary_key=True, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    action = Column(VARCHAR, nullable=False)
    expires = Column(DateTime, nullable=True)
    reason = Column(Text, nullable=False)
    given = Column(DateTime, nullable=False)
    mod_id = Column(BigInteger, nullable=False)

