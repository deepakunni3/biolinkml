
# id: http://example.org/tests/timepoint
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import XSDTime
from includes.types import String, Time

metamodel_version = "1.3.6"


# Types
class TimeType(Time):
    """ A time object represents a (local) time of day, independent of any particular day """
    pass


# Class references
class GeographicLocationK(str):
    pass


class GeographicLocationAtTimeK(GeographicLocationK):
    pass


@dataclass
class GeographicLocation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://example.org/tests/timepoint/GeographicLocation"
    type_curie: ClassVar[str] = ":GeographicLocation"
    type_name: ClassVar[str] = "geographic location"

    k: Union[str, GeographicLocationK]

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.k, GeographicLocationK):
            self.k = GeographicLocationK(self.k)


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://example.org/tests/timepoint/GeographicLocationAtTime"
    type_curie: ClassVar[str] = ":GeographicLocationAtTime"
    type_name: ClassVar[str] = "geographic location at time"

    k: Union[str, GeographicLocationAtTimeK] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.k is not None and not isinstance(self.k, GeographicLocationAtTimeK):
            self.k = GeographicLocationAtTimeK(self.k)
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)
