"""Compatibility imports for creator tools; mechanics now live inside Core."""
from core_world import GENRE_OPS

def operate(core,s,at,op,p):
    return core._operate_domain(s,at,op,p)
