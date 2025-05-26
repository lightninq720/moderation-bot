import nextcord
from nextcord.ext import application_checks
from tools.db.methods import get_mod_roles

def mod_check():
    def predicate(interaction: nextcord.Interaction) -> bool:
        if interaction.guild is None:
            return False
        return any(role.id in get_mod_roles(guild_id=interaction.guild_id) for role in interaction.user.roles)
        
    return application_checks.check(predicate)