import nextcord
from nextcord.ext import application_checks
from tools.db.methods import get_manager_roles

def manager_check():
    def predicate(interaction: nextcord.Interaction):
        if interaction.guild is None:
            return False
        if interaction.user.guild_permissions.manage_guild or any(role.id in get_manager_roles(guild_id=interaction.guild_id) for role in interaction.user.roles): # or in manager table
            return True
        return False
        
    return application_checks.check(predicate)