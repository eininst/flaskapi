from flaskapi.doc import redoc, rapidoc, scalar
from flaskapi.doc.rapidoc.plugins import RegisterPlugin
from flaskapi.doc.redoc.plugins import RegisterPlugin
from flaskapi.doc.scalar.plugins import RegisterPlugin

REDOC = "redoc"
RAPIDOC = "rapidoc"
SCALAR = "scalar"

plugin_map = {
    REDOC: redoc.plugins.RegisterPlugin,
    RAPIDOC: rapidoc.plugins.RegisterPlugin,
    SCALAR: scalar.plugins.RegisterPlugin
}

def plugins() -> list[str]:
    return [REDOC, RAPIDOC, SCALAR]
