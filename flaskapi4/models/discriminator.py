# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:41
from typing import Dict, Optional

from pydantic import BaseModel


class Discriminator(BaseModel):
    """
    https://spec.Flaskapis.org/oas/v3.1.0#discriminator-object
    """

    propertyName: str
    mapping: Optional[Dict[str, str]] = None

    model_config = {
        "extra": "allow"
    }
