"""Application"""

from functools import partial
import sqlite3
from typing import Any, Dict

import aiosqlite
from bareasgi import (
    Application,
    Scope,
    Info,
    Message
)
from bareasgi_cors import CORSMiddleware
from bareasgi_rest import RestHttpRouter, add_swagger_ui

from .recipe_repository import RecipeRepository
from .recipe_controller import RecipeController


async def _on_startup(
        app: Application,
        _scope: Scope,
        info: Info,
        _request: Message
) -> None:
    conn = await aiosqlite.connect(
        info['config']['app']['db'],
        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
    )

    recipe_repository = RecipeRepository(conn)

    recipe_controller = RecipeController(recipe_repository)
    recipe_controller.add_routes(app.http_router)
    info['aiosqlite_conn'] = conn


async def _on_shutdown(
        _scope: Scope,
        info: Info,
        _request: Message
) -> None:
    conn: aiosqlite.Connection = info['aiosqlite_conn']
    await conn.close()


def create_application(config: Dict[str, Any]) -> Application:
    """Create the application"""
    cors_middleware = CORSMiddleware(
        # allow_methods=ALL_METHODS
    )
    rest_router = RestHttpRouter(
        None,
        title="Recipes",
        version="1",
        description="A recipe api",
        base_path='/api/1',
        tags=[
            {
                'name': 'Recipes',
                'description': 'The recipe API'
            }
        ]
    )

    app = Application(
        info=dict(config=config),
        middlewares=[cors_middleware],
        http_router=rest_router
    )

    app.startup_handlers.append(partial(_on_startup, app))
    app.shutdown_handlers.append(_on_shutdown)

    add_swagger_ui(app)

    return app
