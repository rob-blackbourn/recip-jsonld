"""Types"""

from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union
try:
    from typing import TypedDict  # type:ignore
except:  # pylint: disable=bare-except
    from typing_extensions import TypedDict

from bareasgi.basic_router.path_definition import PathDefinition

PropertyValue = TypedDict(
    'PropertyValue',
    {
        '@type': str,
        'max_value': Optional[Union[int, float]],
        'measurement_technique': Optional[str],
        'min_value': Optional[Union[int, float]],
        'property_id': Optional[str],
        'unit_code': Optional[str],
        'unit_text': Optional[str],
        'value': Optional[Union[bool, int, float, str]],
    },
    total=False
)

Thing = TypedDict(
    'Thing',
    {
        '@type': str,
        'additional_type': Optional[str],
        'alternate_name': Optional[str],
        'description': Optional[str],
        'disambiguating_description': Optional[str]
    },
    total=False
)
Author = TypedDict(
    'Author',
    {
        '@type': str,
        'name': str
    },
    total=False
)

HowToTool = TypedDict(
    'HowToTool',
    {
        '@type': str,
        'name': str
    },
    total=False
)

Recipe = TypedDict(
    'Recipe',
    {
        '@context': str,
        '@type': str,
        'name': str,
        'author': Optional[Author],
        'description': Optional[str],
        'date_published': Optional[datetime],
        'image': str,
        'prep_time': Optional[timedelta],
        'cook_time': Optional[timedelta],
        'recipe_ingredient': List[str],
        'recipe_instructions': List[str],
        'recipe_category': Optional[str],
        'recipe_cuisine': Optional[str],
        'keywords': Optional[List[str]],
        'tool': Optional[List[HowToTool]],  # type: ignore
        'foo': Optional[Union[str, int]]
    },
    total=False
)
