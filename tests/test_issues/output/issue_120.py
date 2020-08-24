
# id: http://example.org/sample/example1
# description:
# license:

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace


metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
SAMP = CurieNamespace('samp', 'http://example.org/model/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SAMP


# Types
class String(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = SAMP.String


# Class references



@dataclass
class Student(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMP.Student
    class_class_curie: ClassVar[str] = "samp:Student"
    class_name: ClassVar[str] = "student"
    class_model_uri: ClassVar[URIRef] = SAMP.Student

    name: Optional[str] = None
    courses: Optional[Union[dict, "Course"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.courses is not None and not isinstance(self.courses, Course):
            self.courses = Course(**self.courses)
        super().__post_init__(**kwargs)


@dataclass
class Course(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMP.Course
    class_class_curie: ClassVar[str] = "samp:Course"
    class_name: ClassVar[str] = "course"
    class_model_uri: ClassVar[URIRef] = SAMP.Course

    name: Optional[str] = None


# Slots
class slots:
    pass

slots.name = Slot(uri=SAMP.name, name="name", curie=SAMP.curie('name'),
                      model_uri=SAMP.name, domain=None, range=Optional[str])

slots.courses = Slot(uri=SAMP.courses, name="courses", curie=SAMP.curie('courses'),
                      model_uri=SAMP.courses, domain=None, range=Optional[Union[dict, Course]])