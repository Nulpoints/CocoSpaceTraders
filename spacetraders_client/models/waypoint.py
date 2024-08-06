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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from spacetraders_client.models.chart import Chart
from spacetraders_client.models.waypoint_faction import WaypointFaction
from spacetraders_client.models.waypoint_modifier import WaypointModifier
from spacetraders_client.models.waypoint_orbital import WaypointOrbital
from spacetraders_client.models.waypoint_trait import WaypointTrait
from spacetraders_client.models.waypoint_type import WaypointType
from typing import Optional, Set
from typing_extensions import Self

class Waypoint(BaseModel):
    """
    A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station.
    """ # noqa: E501
    symbol: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The symbol of the waypoint.")
    type: WaypointType
    system_symbol: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The symbol of the system.", alias="systemSymbol")
    x: StrictInt = Field(description="Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe.")
    y: StrictInt = Field(description="Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe.")
    orbitals: List[WaypointOrbital] = Field(description="Waypoints that orbit this waypoint.")
    orbits: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined.")
    faction: Optional[WaypointFaction] = None
    traits: List[WaypointTrait] = Field(description="The traits of the waypoint.")
    modifiers: Optional[List[WaypointModifier]] = Field(default=None, description="The modifiers of the waypoint.")
    chart: Optional[Chart] = None
    is_under_construction: StrictBool = Field(description="True if the waypoint is under construction.", alias="isUnderConstruction")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["symbol", "type", "systemSymbol", "x", "y", "orbitals", "orbits", "faction", "traits", "modifiers", "chart", "isUnderConstruction"]

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
        """Create an instance of Waypoint from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in orbitals (list)
        _items = []
        if self.orbitals:
            for _item in self.orbitals:
                if _item:
                    _items.append(_item.to_dict())
            _dict['orbitals'] = _items
        # override the default output from pydantic by calling `to_dict()` of faction
        if self.faction:
            _dict['faction'] = self.faction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in traits (list)
        _items = []
        if self.traits:
            for _item in self.traits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['traits'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in modifiers (list)
        _items = []
        if self.modifiers:
            for _item in self.modifiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['modifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of chart
        if self.chart:
            _dict['chart'] = self.chart.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Waypoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "type": obj.get("type"),
            "systemSymbol": obj.get("systemSymbol"),
            "x": obj.get("x"),
            "y": obj.get("y"),
            "orbitals": [WaypointOrbital.from_dict(_item) for _item in obj["orbitals"]] if obj.get("orbitals") is not None else None,
            "orbits": obj.get("orbits"),
            "faction": WaypointFaction.from_dict(obj["faction"]) if obj.get("faction") is not None else None,
            "traits": [WaypointTrait.from_dict(_item) for _item in obj["traits"]] if obj.get("traits") is not None else None,
            "modifiers": [WaypointModifier.from_dict(_item) for _item in obj["modifiers"]] if obj.get("modifiers") is not None else None,
            "chart": Chart.from_dict(obj["chart"]) if obj.get("chart") is not None else None,
            "isUnderConstruction": obj.get("isUnderConstruction")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


