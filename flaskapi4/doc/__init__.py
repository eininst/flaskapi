from flaskapi4.doc import redoc, rapidoc, scalar
from flaskapi4.doc.rapidoc.plugins import RegisterPlugin
from flaskapi4.doc.redoc.plugins import RegisterPlugin
from flaskapi4.doc.scalar.plugins import RegisterPlugin

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
