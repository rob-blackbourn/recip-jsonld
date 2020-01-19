"""Recipe REST Controller"""

from datetime import datetime, timedelta
import json
from typing import Any, Dict, List, Optional
try:
    from typing import TypedDict  # type:ignore
except:  # pylint: disable=bare-except
    from typing_extensions import TypedDict
from urllib.parse import parse_qsl
from urllib.error import HTTPError

from bareasgi import (
    Application,
    Scope,
    Info,
    RouteMatches,
    Content,
    HttpResponse
)
from bareutils import (
    text_reader,
    text_writer
)
import bareutils.header as header
from bareasgi_rest import RestHttpRouter, add_swagger_ui, Body

from .recipe_repository import RecipeRepository


class RecipeController:
    """The recipe controller"""

    def __init__(self, repository: RecipeRepository) -> None:
        """The recipe controller

        Args:
            repository (RecipeRepository): The recipe repository
        """
        self._repository = repository

    def add_routes(self, router: RestHttpRouter) -> None:
        """Add the routes

        Args:
            router (RestHttpRouter): The rest router
        """
        tags = ['Recipes']
        router.add_rest(
            {'POST', 'OPTIONS'},
            '/recipes',
            self._create,
            tags=tags,
            status_code=201
        )
        router.add_rest(
            {'GET'},
            '/recipes/{identifier:str}',
            self._read
        )
        router.add_rest(
            {'GET'},
            '/recipes',
            self._read_many,
            tags=tags
        )
        router.add_rest(
            {'PUT', 'OPTIONS'},
            '/recipes',
            self._update,
            tags=tags
        )
        router.add_rest(
            {'DELETE', 'OPTIONS'},
            '/recipes/{identifier:str}',
            self._delete,
            tags=tags
        )

    async def _create(
            self,
            recipe: Body[Dict[str, Any]]
    ) -> str:
        """Create a recipe

        Args:
            recipe (Recipe): The recipe

        Returns:
            str: The identifier
        """
        return await self._repository.create(recipe)

    async def _read(
            self,
            identifier: str
    ) -> Dict[str, Any]:
        """Read a recipe

        Args:
            identifier (str): The identifiers

        Returns:
            Optional[Recipe]: The recipe if found
        """
        recipe = await self._repository.read(identifier)
        if recipe is None:
            raise HTTPError(None, 404, None, None, None)

        return recipe

    async def _read_many(
            self,
            values: List[str],
            limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Read recipes matching values

        Args:
            values (List[str]): The values to match
            limit (int, optional): The maximum number of records to return. Defaults to 10.

        Returns:
            List[Recipe]: A list of matched recipes
        """
        if not values:
            return await self._repository.read_all(limit)
        else:
            return await self._repository.read_many(values, limit)

    async def _update(
            self,
            recipe: Body[Dict[str, Any]]
    ) -> bool:
        """Update a recipe

        Args:
            recipe (Recipe): The recipe

        Returns:
            bool: True if the recipe was updated
        """
        return await self._repository.update(recipe)

    async def _delete(
            self,
            identifier: str
    ) -> bool:
        """Delete a recipe

        Args:
            identifier (str): The identifier

        Returns:
            bool: True if the recipe was deleted
        """
        return await self._repository.delete(identifier)
