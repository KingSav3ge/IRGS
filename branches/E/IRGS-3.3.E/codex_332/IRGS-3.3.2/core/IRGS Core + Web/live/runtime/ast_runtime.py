"""Compatibility names for the AST campaign library on the common Core kernel."""
from core_world import CoreWorld, ALIASES
ASTWorld=CoreWorld
AST_OPS=set(ALIASES)
def initial_ast():
    from campaign_library import initial_campaign
    return initial_campaign('ast')
