# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2024/4/22 16:13
import os

from flask import Blueprint, render_template_string, current_app

from flaskapi4.doc.redoc.templates import redoc_html_string
from flaskapi4.plugins import BasePlugin


class RegisterPlugin(BasePlugin):
    name = "redoc"
    display_name = "Redoc"

    @classmethod
    def register(cls, doc_url: str) -> Blueprint:
        _here = os.path.dirname(__file__)
        template_folder = os.path.join(_here, "templates")
        static_folder = os.path.join(template_folder, "redoc")
        blueprint = Blueprint(
            cls.name,
            __name__,
            template_folder=template_folder,
            static_folder=static_folder
        )

        blueprint.add_url_rule(
            rule=f"/{cls.name}",
            endpoint=f"{cls.name}",
            view_func=lambda: render_template_string(
                current_app.config.get("REDOC_HTML_STRING") or redoc_html_string,
                doc_url=doc_url,
                redoc_config=current_app.config.get("REDOC_CONFIG")
            )
        )

        return blueprint
