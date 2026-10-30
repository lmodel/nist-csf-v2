# Auto generated from nist_csf_v2.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-10-30T08:17:22
# Schema: nist_csf_v2
#
# id: https://w3id.org/lmodel/nist-csf-v2
# description: A LinkML model of the Cybersecurity Framework (CSF) 2.0, which NIST publishes as Cybersecurity White Paper (CSWP) 29: its six functions, their categories and subcategories, the implementation examples NIST publishes with the subcategories, and the CSF 1.1 categories and subcategories that CSF 2.0 withdrew, each with its status and, where NIST recorded it, where it moved or what incorporated it.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = "2.0.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_CSF_V2 = CurieNamespace('nist_csf_v2', 'https://w3id.org/lmodel/nist-csf-v2/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NIST_CSF_V2


# Types
class CsfFunctionIdentifier(String):
    """ The two letters that name one of the six functions, such as GV for GOVERN. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "csf_function_identifier"
    type_model_uri = NIST_CSF_V2.CsfFunctionIdentifier


class CsfCategoryIdentifier(String):
    """ A category's identifier: its function's letters, a dot and two letters for the category, such as GV.OC for Organizational Context. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "csf_category_identifier"
    type_model_uri = NIST_CSF_V2.CsfCategoryIdentifier


class CsfSubcategoryIdentifier(String):
    """ A subcategory's identifier: its category's identifier, a hyphen and a two-digit number, such as GV.OC-01. CSWP 29 says the numbers are not sequential on purpose: a gap marks a CSF 1.1 subcategory that CSF 2.0 moved elsewhere. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "csf_subcategory_identifier"
    type_model_uri = NIST_CSF_V2.CsfSubcategoryIdentifier


class CsfImplementationExampleIdentifier(String):
    """ The identifier NIST's reference data gives an implementation example: its subcategory's identifier, a dot and a three-digit number, such as GV.OC-01.001. The numbers run once through the whole Core, so no two examples share one. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "csf_implementation_example_identifier"
    type_model_uri = NIST_CSF_V2.CsfImplementationExampleIdentifier


class CsfElementIdentifier(String):
    """ The identifier of a function, a category or a subcategory, whichever of the three a withdrawn element names as what incorporated it. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "csf_element_identifier"
    type_model_uri = NIST_CSF_V2.CsfElementIdentifier


# Class references



@dataclass(repr=False)
class CsfFramework(YAMLRoot):
    """
    One edition of the CSF as a whole: its functions, each holding its categories and their subcategories.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["Framework"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:Framework"
    class_name: ClassVar[str] = "CsfFramework"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.CsfFramework

    csf_version: str = None
    csf_functions: Union[Union[dict, "CsfFunction"], list[Union[dict, "CsfFunction"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.csf_version):
            self.MissingRequiredField("csf_version")
        if not isinstance(self.csf_version, str):
            self.csf_version = str(self.csf_version)

        if self._is_empty(self.csf_functions):
            self.MissingRequiredField("csf_functions")
        self._normalize_inlined_as_list(slot_name="csf_functions", slot_type=CsfFunction, key_name="csf_function_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CsfFunction(YAMLRoot):
    """
    One of the six functions that sort the CSF's outcomes at the highest level: GOVERN, IDENTIFY, PROTECT, DETECT,
    RESPOND and RECOVER. Each is named by two letters and described in a sentence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["Function"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:Function"
    class_name: ClassVar[str] = "CsfFunction"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.CsfFunction

    csf_function_id: Union[str, CsfFunctionIdentifier] = None
    title: Optional[str] = None
    description: Optional[str] = None
    function_categories: Optional[Union[Union[dict, "CsfCategory"], list[Union[dict, "CsfCategory"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.csf_function_id):
            self.MissingRequiredField("csf_function_id")
        if not isinstance(self.csf_function_id, CsfFunctionIdentifier):
            self.csf_function_id = CsfFunctionIdentifier(self.csf_function_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="function_categories", slot_type=CsfCategory, key_name="csf_category_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CsfCategory(YAMLRoot):
    """
    A group of related cybersecurity outcomes within a function, such as Organizational Context (GV.OC), or a CSF 1.1
    category that CSF 2.0 withdrew, which the catalog keeps with its status and, where NIST recorded it, where it
    moved or what incorporated it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["Category"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:Category"
    class_name: ClassVar[str] = "CsfCategory"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.CsfCategory

    csf_category_id: Union[str, CsfCategoryIdentifier] = None
    title: Optional[str] = None
    description: Optional[str] = None
    category_subcategories: Optional[Union[Union[dict, "CsfSubcategory"], list[Union[dict, "CsfSubcategory"]]]] = empty_list()
    category_status: Optional[Union[str, "CsfElementStatus"]] = None
    category_moved_to: Optional[Union[Union[str, CsfCategoryIdentifier], list[Union[str, CsfCategoryIdentifier]]]] = empty_list()
    category_incorporated_into: Optional[Union[Union[str, CsfElementIdentifier], list[Union[str, CsfElementIdentifier]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.csf_category_id):
            self.MissingRequiredField("csf_category_id")
        if not isinstance(self.csf_category_id, CsfCategoryIdentifier):
            self.csf_category_id = CsfCategoryIdentifier(self.csf_category_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="category_subcategories", slot_type=CsfSubcategory, key_name="description", keyed=False)

        if self.category_status is not None and not isinstance(self.category_status, CsfElementStatus):
            self.category_status = CsfElementStatus(self.category_status)

        if not isinstance(self.category_moved_to, list):
            self.category_moved_to = [self.category_moved_to] if self.category_moved_to is not None else []
        self.category_moved_to = [v if isinstance(v, CsfCategoryIdentifier) else CsfCategoryIdentifier(v) for v in self.category_moved_to]

        if not isinstance(self.category_incorporated_into, list):
            self.category_incorporated_into = [self.category_incorporated_into] if self.category_incorporated_into is not None else []
        self.category_incorporated_into = [v if isinstance(v, CsfElementIdentifier) else CsfElementIdentifier(v) for v in self.category_incorporated_into]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CsfSubcategory(YAMLRoot):
    """
    A cybersecurity outcome: one statement of a result within a category, such as GV.OC-01, or a CSF 1.1 subcategory
    that CSF 2.0 withdrew, which the catalog keeps with its statement, its status and where it moved or what
    incorporated it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["Subcategory"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:Subcategory"
    class_name: ClassVar[str] = "CsfSubcategory"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.CsfSubcategory

    description: str = None
    csf_subcategory_id: Union[str, CsfSubcategoryIdentifier] = None
    subcategory_examples: Optional[Union[Union[dict, "CsfImplementationExample"], list[Union[dict, "CsfImplementationExample"]]]] = empty_list()
    subcategory_status: Optional[Union[str, "CsfElementStatus"]] = None
    subcategory_moved_to: Optional[Union[Union[str, CsfSubcategoryIdentifier], list[Union[str, CsfSubcategoryIdentifier]]]] = empty_list()
    subcategory_incorporated_into: Optional[Union[Union[str, CsfElementIdentifier], list[Union[str, CsfElementIdentifier]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.csf_subcategory_id):
            self.MissingRequiredField("csf_subcategory_id")
        if not isinstance(self.csf_subcategory_id, CsfSubcategoryIdentifier):
            self.csf_subcategory_id = CsfSubcategoryIdentifier(self.csf_subcategory_id)

        self._normalize_inlined_as_list(slot_name="subcategory_examples", slot_type=CsfImplementationExample, key_name="description", keyed=False)

        if self.subcategory_status is not None and not isinstance(self.subcategory_status, CsfElementStatus):
            self.subcategory_status = CsfElementStatus(self.subcategory_status)

        if not isinstance(self.subcategory_moved_to, list):
            self.subcategory_moved_to = [self.subcategory_moved_to] if self.subcategory_moved_to is not None else []
        self.subcategory_moved_to = [v if isinstance(v, CsfSubcategoryIdentifier) else CsfSubcategoryIdentifier(v) for v in self.subcategory_moved_to]

        if not isinstance(self.subcategory_incorporated_into, list):
            self.subcategory_incorporated_into = [self.subcategory_incorporated_into] if self.subcategory_incorporated_into is not None else []
        self.subcategory_incorporated_into = [v if isinstance(v, CsfElementIdentifier) else CsfElementIdentifier(v) for v in self.subcategory_incorporated_into]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CsfImplementationExample(YAMLRoot):
    """
    An implementation example: one concise, action-oriented step that could help achieve a subcategory's outcome. NIST
    publishes the examples beside the Core, in its reference tool and its catalog, not in CSWP 29 itself.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["ImplementationExample"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:ImplementationExample"
    class_name: ClassVar[str] = "CsfImplementationExample"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.CsfImplementationExample

    description: str = None
    csf_implementation_example_id: Union[str, CsfImplementationExampleIdentifier] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.csf_implementation_example_id):
            self.MissingRequiredField("csf_implementation_example_id")
        if not isinstance(self.csf_implementation_example_id, CsfImplementationExampleIdentifier):
            self.csf_implementation_example_id = CsfImplementationExampleIdentifier(self.csf_implementation_example_id)

        super().__post_init__(**kwargs)


# Enumerations
class CsfElementStatus(EnumDefinitionImpl):
    """
    The state the catalog gives a category or subcategory that CSF 2.0 no longer carries. A category or subcategory of
    CSF 2.0 has no status.
    """
    withdrawn = PermissibleValue(
        text="withdrawn",
        description="""The element was in CSF 1.1 and CSF 2.0 withdrew it. The catalog keeps it, and names where it moved or what incorporated it where NIST recorded that.""")

    _defn = EnumDefinition(
        name="CsfElementStatus",
        description="""The state the catalog gives a category or subcategory that CSF 2.0 no longer carries. A category or subcategory of CSF 2.0 has no status.""",
    )

# Slots
class slots:
    pass

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_CSF_V2.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_CSF_V2.description, domain=None, range=Optional[str])

slots.csfFramework__csf_version = Slot(uri=NIST_CSF_V2.csf_version, name="csfFramework__csf_version", curie=NIST_CSF_V2.curie('csf_version'),
                   model_uri=NIST_CSF_V2.csfFramework__csf_version, domain=None, range=str,
                   pattern=re.compile(r'^[0-9]+\.[0-9]+$'))

slots.csfFramework__csf_functions = Slot(uri=NIST_CSF_V2.csf_functions, name="csfFramework__csf_functions", curie=NIST_CSF_V2.curie('csf_functions'),
                   model_uri=NIST_CSF_V2.csfFramework__csf_functions, domain=None, range=Union[Union[dict, CsfFunction], list[Union[dict, CsfFunction]]])

slots.csfFunction__csf_function_id = Slot(uri=NIST_CSF_V2.csf_function_id, name="csfFunction__csf_function_id", curie=NIST_CSF_V2.curie('csf_function_id'),
                   model_uri=NIST_CSF_V2.csfFunction__csf_function_id, domain=None, range=Union[str, CsfFunctionIdentifier])

slots.csfFunction__function_categories = Slot(uri=NIST_CSF_V2.function_categories, name="csfFunction__function_categories", curie=NIST_CSF_V2.curie('function_categories'),
                   model_uri=NIST_CSF_V2.csfFunction__function_categories, domain=None, range=Optional[Union[Union[dict, CsfCategory], list[Union[dict, CsfCategory]]]])

slots.csfCategory__csf_category_id = Slot(uri=NIST_CSF_V2.csf_category_id, name="csfCategory__csf_category_id", curie=NIST_CSF_V2.curie('csf_category_id'),
                   model_uri=NIST_CSF_V2.csfCategory__csf_category_id, domain=None, range=Union[str, CsfCategoryIdentifier])

slots.csfCategory__category_subcategories = Slot(uri=NIST_CSF_V2.category_subcategories, name="csfCategory__category_subcategories", curie=NIST_CSF_V2.curie('category_subcategories'),
                   model_uri=NIST_CSF_V2.csfCategory__category_subcategories, domain=None, range=Optional[Union[Union[dict, CsfSubcategory], list[Union[dict, CsfSubcategory]]]])

slots.csfCategory__category_status = Slot(uri=NIST_CSF_V2.category_status, name="csfCategory__category_status", curie=NIST_CSF_V2.curie('category_status'),
                   model_uri=NIST_CSF_V2.csfCategory__category_status, domain=None, range=Optional[Union[str, "CsfElementStatus"]])

slots.csfCategory__category_moved_to = Slot(uri=NIST_CSF_V2.category_moved_to, name="csfCategory__category_moved_to", curie=NIST_CSF_V2.curie('category_moved_to'),
                   model_uri=NIST_CSF_V2.csfCategory__category_moved_to, domain=None, range=Optional[Union[Union[str, CsfCategoryIdentifier], list[Union[str, CsfCategoryIdentifier]]]])

slots.csfCategory__category_incorporated_into = Slot(uri=NIST_CSF_V2.category_incorporated_into, name="csfCategory__category_incorporated_into", curie=NIST_CSF_V2.curie('category_incorporated_into'),
                   model_uri=NIST_CSF_V2.csfCategory__category_incorporated_into, domain=None, range=Optional[Union[Union[str, CsfElementIdentifier], list[Union[str, CsfElementIdentifier]]]])

slots.csfSubcategory__csf_subcategory_id = Slot(uri=NIST_CSF_V2.csf_subcategory_id, name="csfSubcategory__csf_subcategory_id", curie=NIST_CSF_V2.curie('csf_subcategory_id'),
                   model_uri=NIST_CSF_V2.csfSubcategory__csf_subcategory_id, domain=None, range=Union[str, CsfSubcategoryIdentifier])

slots.csfSubcategory__subcategory_examples = Slot(uri=NIST_CSF_V2.subcategory_examples, name="csfSubcategory__subcategory_examples", curie=NIST_CSF_V2.curie('subcategory_examples'),
                   model_uri=NIST_CSF_V2.csfSubcategory__subcategory_examples, domain=None, range=Optional[Union[Union[dict, CsfImplementationExample], list[Union[dict, CsfImplementationExample]]]])

slots.csfSubcategory__subcategory_status = Slot(uri=NIST_CSF_V2.subcategory_status, name="csfSubcategory__subcategory_status", curie=NIST_CSF_V2.curie('subcategory_status'),
                   model_uri=NIST_CSF_V2.csfSubcategory__subcategory_status, domain=None, range=Optional[Union[str, "CsfElementStatus"]])

slots.csfSubcategory__subcategory_moved_to = Slot(uri=NIST_CSF_V2.subcategory_moved_to, name="csfSubcategory__subcategory_moved_to", curie=NIST_CSF_V2.curie('subcategory_moved_to'),
                   model_uri=NIST_CSF_V2.csfSubcategory__subcategory_moved_to, domain=None, range=Optional[Union[Union[str, CsfSubcategoryIdentifier], list[Union[str, CsfSubcategoryIdentifier]]]])

slots.csfSubcategory__subcategory_incorporated_into = Slot(uri=NIST_CSF_V2.subcategory_incorporated_into, name="csfSubcategory__subcategory_incorporated_into", curie=NIST_CSF_V2.curie('subcategory_incorporated_into'),
                   model_uri=NIST_CSF_V2.csfSubcategory__subcategory_incorporated_into, domain=None, range=Optional[Union[Union[str, CsfElementIdentifier], list[Union[str, CsfElementIdentifier]]]])

slots.csfImplementationExample__csf_implementation_example_id = Slot(uri=NIST_CSF_V2.csf_implementation_example_id, name="csfImplementationExample__csf_implementation_example_id", curie=NIST_CSF_V2.curie('csf_implementation_example_id'),
                   model_uri=NIST_CSF_V2.csfImplementationExample__csf_implementation_example_id, domain=None, range=Union[str, CsfImplementationExampleIdentifier])

slots.CsfSubcategory_description = Slot(uri=SCHEMA.description, name="CsfSubcategory_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_CSF_V2.CsfSubcategory_description, domain=CsfSubcategory, range=str)

slots.CsfImplementationExample_description = Slot(uri=SCHEMA.description, name="CsfImplementationExample_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_CSF_V2.CsfImplementationExample_description, domain=CsfImplementationExample, range=str)
