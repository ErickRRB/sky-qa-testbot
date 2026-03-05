"""
Estado global compartido entre módulos.
Se popula en test_sky.py (antes de run()) mediante CFG.update(aplicar_args(...)).
Todos los módulos acceden a este objeto via: import core.state as state
"""

CFG: dict = {}
EXPLORACION_RUN_ID: str = ""
EXPLORACION_DIR: str = ""
