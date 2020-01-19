"""Recipe Repository"""

from datetime import datetime
import json
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple
)
from uuid import uuid4

import aiosqlite


def _make_unpacker(cur: aiosqlite.Cursor) -> Callable[[Tuple], Dict[str, Any]]:
    columns = [name for name, *_ in cur.description]
    return lambda row: dict(zip(columns, row))


class RecipeRepository:
    """"A recipe repository"""

    def __init__(self, conn: aiosqlite.Connection) -> None:
        self._conn = conn

    async def create(self, recipe: Dict[str, Any]) -> str:
        """Create a recipe"""

        identifier = str(uuid4())
        stmt = f"""
INSERT INTO recipes(identifier, content)
VALUES (?, ?)
"""
        args = (identifier, json.dumps(recipe))

        async with self._conn.cursor() as cur:
            await cur.execute(stmt, args)
            await self._conn.commit()
            return identifier

    async def read(
            self,
            identifier: str
    ) -> Optional[Dict[str, Any]]:
        """Read a recipe by identifier"""

        stmt = f"""
SELECT content
FROM recipes
WHERE identifier = ?
"""
        args = (identifier,)

        async with self._conn.cursor() as cur:
            await cur.execute(stmt, args)
            row = await cur.fetchone()
            if row is None:
                return None
            recipe = json.loads(row[0])
            return recipe

    async def read_many(
            self,
            values: List[str],
            limit: int
    ) -> List[Dict[str, Any]]:
        """Read recipes like properties"""
        stmt = 'INTERSECT'.join("""
SELECT r.content
FROM recipes AS r
JOIN property_map AS pm
ON pm.identifier = r.identifier
WHERE pm.property_value like ?
""" for _ in values)
        stmt += "\nLIMIT ?"

        args: List[Any] = [f'%{value}%' for value in values]
        args.append(limit)

        async with self._conn.cursor() as cur:
            await cur.execute(stmt, args)
            recipes: List[Dict[str, Any]] = []
            async for row in cur:
                recipes.append(json.loads(row[0]))
            return recipes

    async def read_all(
            self,
            limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Read all recipes"""
        stmt = """
SELECT *
FROM recipes
LIMIT ?
"""
        args = (limit,)

        async with self._conn.cursor() as cur:
            await cur.execute(stmt, args)
            unpack = _make_unpacker(cur)
            values = [unpack(row) async for row in cur]
            recipes = [json.loads(value['content']) for value in values]
            return recipes

    async def update(self, recipe: Dict[str, Any]) -> bool:
        """Update a recipe"""
        stmt = """
UPDATE recipe
SET content=?
WHERE identifier=?
"""
        args = (json.dumps(recipe), recipe['identifier'])
        async with self._conn.cursor() as cur:
            await cur.execute(stmt, args)
            await self._conn.commit()
            return cur.rowcount == 1

    async def delete(self, identifier: str) -> bool:
        """Delete a recipe"""
        stmt = """
DELETE FROM recipes
WHERE identifier=?
"""
        args = (identifier,)
        async with self._conn.cursor() as cur:
            await cur.execute(stmt, args)
            await self._conn.commit()
            return cur.rowcount == 1
