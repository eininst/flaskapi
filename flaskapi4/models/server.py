# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/4/28 11:26
from typing import Dict, Optional

from pydantic import BaseModel

from .server_variable import ServerVariable


class Server(BaseModel):
    """
    https://spec.Flaskapis.org/oas/v3.1.0#server-object
    """

    url: str
    description: Optional[str] = None
    variables: Optional[Dict[str, ServerVariable]] = None

    model_config = {
        "extra": "allow"
    }
