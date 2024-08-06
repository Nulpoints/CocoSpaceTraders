# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.   

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from spacetraders_client.models.ship_requirements import ShipRequirements
from typing import Optional, Set
from typing_extensions import Self

class ShipFrame(BaseModel):
    """
    The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.
    """ # noqa: E501
    symbol: StrictStr = Field(description="Symbol of the frame.")
    name: StrictStr = Field(description="Name of the frame.")
    description: StrictStr = Field(description="Description of the frame.")
    condition: Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.")
    integrity: Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.")
    module_slots: Annotated[int, Field(strict=True, ge=0)] = Field(description="The amount of slots that can be dedicated to modules installed in the ship. Each installed module take up a number of slots, and once there are no more slots, no new modules can be installed.", alias="moduleSlots")
    mounting_points: Annotated[int, Field(strict=True, ge=0)] = Field(description="The amount of slots that can be dedicated to mounts installed in the ship. Each installed mount takes up a number of points, and once there are no more points remaining, no new mounts can be installed.", alias="mountingPoints")
    fuel_capacity: Annotated[int, Field(strict=True, ge=0)] = Field(description="The maximum amount of fuel that can be stored in this ship. When refueling, the ship will be refueled to this amount.", alias="fuelCapacity")
    requirements: ShipRequirements
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["symbol", "name", "description", "condition", "integrity", "moduleSlots", "mountingPoints", "fuelCapacity", "requirements"]

    @field_validator('symbol')
    def symbol_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['FRAME_PROBE', 'FRAME_DRONE', 'FRAME_INTERCEPTOR', 'FRAME_RACER', 'FRAME_FIGHTER', 'FRAME_FRIGATE', 'FRAME_SHUTTLE', 'FRAME_EXPLORER', 'FRAME_MINER', 'FRAME_LIGHT_FREIGHTER', 'FRAME_HEAVY_FREIGHTER', 'FRAME_TRANSPORT', 'FRAME_DESTROYER', 'FRAME_CRUISER', 'FRAME_CARRIER']):
            raise ValueError("must be one of enum values ('FRAME_PROBE', 'FRAME_DRONE', 'FRAME_INTERCEPTOR', 'FRAME_RACER', 'FRAME_FIGHTER', 'FRAME_FRIGATE', 'FRAME_SHUTTLE', 'FRAME_EXPLORER', 'FRAME_MINER', 'FRAME_LIGHT_FREIGHTER', 'FRAME_HEAVY_FREIGHTER', 'FRAME_TRANSPORT', 'FRAME_DESTROYER', 'FRAME_CRUISER', 'FRAME_CARRIER')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ShipFrame from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of requirements
        if self.requirements:
            _dict['requirements'] = self.requirements.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShipFrame from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "condition": obj.get("condition"),
            "integrity": obj.get("integrity"),
            "moduleSlots": obj.get("moduleSlots"),
            "mountingPoints": obj.get("mountingPoints"),
            "fuelCapacity": obj.get("fuelCapacity"),
            "requirements": ShipRequirements.from_dict(obj["requirements"]) if obj.get("requirements") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


