# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2022/4/16 14:21
import json

from flask import current_app
from flask.cli import click
from flask.cli import with_appcontext


@click.command(name="Flaskapi")
@click.option("--output", "-o", type=click.Path(), help="The output file path.")
@click.option("--format", "-f", "_format", type=click.Choice(["json", "yaml"]), help="The output file format.")
@click.option("--indent", "-i", type=int, help="The indentation for JSON dumps.")
@with_appcontext
def Flaskapi_command(output, _format, indent):
    """Export the Flaskapi Specification to console or a file"""

    # Check if the current app has an api_doc attribute
    if hasattr(current_app, "api_doc"):
        obj = current_app.api_doc

        # Generate the Flaskapi Specification based on the specified format
        if _format == "yaml":
            try:
                import yaml  # type: ignore
            except ImportError:  # pragma: no cover
                raise ImportError("pyyaml must be installed.")
            Flaskapi = yaml.safe_dump(obj, allow_unicode=True)
        else:
            Flaskapi = json.dumps(obj, indent=indent, ensure_ascii=False)

        # Save the Flaskapi Specification to a file if the output path is provided
        if output:
            with open(output, "w", encoding="utf8") as f:
                f.write(Flaskapi)
            click.echo(f"Saved to {output}.")
        else:
            click.echo(Flaskapi)
