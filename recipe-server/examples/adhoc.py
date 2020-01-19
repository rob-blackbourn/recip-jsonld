"""Adhoc example"""

import asyncio
import sqlite3

import aiosqlite
from recipe_server.recipe_repository import RecipeRepository


async def main():
    conn = await aiosqlite.connect(
        'recipes.db',
        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
    )

    repo = RecipeRepository(conn)
    all_recipes = await repo.read_many_like(['thai', 'meat'], 100)
    one_recipe = await repo.read_by_identifier('830f2163-ccfd-4088-9fe3-b471e7c82b7a')
    print("Done")


if __name__ == "__main__":
    asyncio.run(main())
