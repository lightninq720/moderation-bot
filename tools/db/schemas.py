from typing import List, Dict, Optional, Union
from pydantic import BaseModel
import datetime

class Table(BaseModel):
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False
        equal = True

        for i in self.__class__.model_fields:
            if (self.model_dump()[i] or getattr(other, i, None)) and self.model_dump()[i] != getattr(other, i, None):
                return False
        
        return equal

class GuildMainBase(Table):
    guild_id: int
    prefix: str
    log_id: Optional[int] = None
    mute_role_id: Optional[int] = None

    class Config:
        from_attributes = True

class ModRolesBase(Table):
    guild_id: int
    role_id: int

    class Config:
        from_attributes = True

class ManagerRolesBase(Table):
    guild_id: int
    role_id: int

    class Config:
        from_attributes = True

class ModlogBase(Table):
    case_no: int
    guild_id: int
    user_id: int
    action: str
    expires: datetime
    reason: str
    given: datetime
    mod_id: int

    class Config:
        from_attributes = True