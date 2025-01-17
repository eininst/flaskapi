# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:47
from typing import Dict, Optional

from pydantic import BaseModel


class OAuthFlow(BaseModel):
    """
    https://spec.Flaskapis.org/oas/v3.1.0#oauth-flow-object
    """

    authorizationUrl: Optional[str] = None
    tokenUrl: Optional[str] = None
    refreshUrl: Optional[str] = None
    scopes: Dict[str, str]

    model_config = {
        "extra": "allow"
    }
