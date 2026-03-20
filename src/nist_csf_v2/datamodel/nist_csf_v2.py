# Auto generated from nist_csf_v2.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-20T17:44:57
# Schema: nist-csf-v2
#
# id: https://w3id.org/lmodel/nist-csf-v2
# description: NIST Cybersecurity Framework 2.0
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
DEFAULT_ = NIST_CSF_V2


# Types

# Class references



CSFDocument = Any

CSFCatalogBody = Any

CSFMetadata = Any

@dataclass(repr=False)
class CSFElement(YAMLRoot):
    """
    Abstract base class for CSF catalog elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["CSFElement"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:CSFElement"
    class_name: ClassVar[str] = "CSFElement"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.CSFElement

    id: Optional[str] = None
    _class: Optional[Union[str, "CSFElementClassValue"]] = None
    title: Optional[str] = None
    props: Optional[Union[Union[dict, "CSFProperty"], list[Union[dict, "CSFProperty"]]]] = empty_list()
    parts: Optional[Union[Union[dict, "CSFPart"], list[Union[dict, "CSFPart"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self._class is not None and not isinstance(self._class, CSFElementClassValue):
            self._class = CSFElementClassValue(self._class)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.props, list):
            self.props = [self.props] if self.props is not None else []
        self.props = [v if isinstance(v, CSFProperty) else CSFProperty(**as_dict(v)) for v in self.props]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CSFFunction(CSFElement):
    """
    A CSF function - top-level grouping (e.g. GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["CSFFunction"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:CSFFunction"
    class_name: ClassVar[str] = "CSFFunction"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.CSFFunction

    controls: Optional[Union[Union[dict, "CSFCategory"], list[Union[dict, "CSFCategory"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, CSFCategory) else CSFCategory(**as_dict(v)) for v in self.controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CSFCategory(CSFElement):
    """
    A CSF category - second-level grouping within a function (e.g. GV.OC Organizational Context, ID.AM Asset
    Management)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["CSFCategory"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:CSFCategory"
    class_name: ClassVar[str] = "CSFCategory"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.CSFCategory

    controls: Optional[Union[Union[dict, "CSFSubcategory"], list[Union[dict, "CSFSubcategory"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, CSFSubcategory) else CSFSubcategory(**as_dict(v)) for v in self.controls]

        super().__post_init__(**kwargs)


class CSFSubcategory(CSFElement):
    """
    A CSF subcategory - specific cybersecurity outcome (e.g. GV.OC-01, ID.AM-01)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["CSFSubcategory"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:CSFSubcategory"
    class_name: ClassVar[str] = "CSFSubcategory"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.CSFSubcategory


CSFPart = Any

@dataclass(repr=False)
class CSFProperty(YAMLRoot):
    """
    A name-value property with optional namespace and supplemental remarks
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["CSFProperty"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:CSFProperty"
    class_name: ClassVar[str] = "CSFProperty"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.CSFProperty

    name: Optional[str] = None
    value: Optional[str] = None
    ns: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Link(YAMLRoot):
    """
    Relationship link with href and optional rel attribute
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["Link"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:Link"
    class_name: ClassVar[str] = "Link"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.Link

    href: Optional[str] = None
    rel: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.href is not None and not isinstance(self.href, str):
            self.href = str(self.href)

        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Role(YAMLRoot):
    """
    Role definition used in metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_CSF_V2["Role"]
    class_class_curie: ClassVar[str] = "nist_csf_v2:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = NIST_CSF_V2.Role

    id: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


Party = Any

Address = Any

ResponsibleParty = Any

BackMatter = Any

Resource = Any

ResourceLink = Any

# Enumerations
class CSFElementClassValue(EnumDefinitionImpl):
    """
    Allowed class values for CSF catalog elements
    """
    function = PermissibleValue(text="function")
    category = PermissibleValue(text="category")
    subcategory = PermissibleValue(text="subcategory")

    _defn = EnumDefinition(
        name="CSFElementClassValue",
        description="Allowed class values for CSF catalog elements",
    )

# Slots
class slots:
    pass

slots.catalog = Slot(uri=NIST_CSF_V2.catalog, name="catalog", curie=NIST_CSF_V2.curie('catalog'),
                   model_uri=NIST_CSF_V2.catalog, domain=None, range=Optional[Union[dict, CSFCatalogBody]])

slots.metadata = Slot(uri=NIST_CSF_V2.metadata, name="metadata", curie=NIST_CSF_V2.curie('metadata'),
                   model_uri=NIST_CSF_V2.metadata, domain=None, range=Optional[Union[dict, CSFMetadata]])

slots.groups = Slot(uri=NIST_CSF_V2.groups, name="groups", curie=NIST_CSF_V2.curie('groups'),
                   model_uri=NIST_CSF_V2.groups, domain=None, range=Optional[Union[Union[dict, CSFFunction], list[Union[dict, CSFFunction]]]])

slots.controls = Slot(uri=NIST_CSF_V2.controls, name="controls", curie=NIST_CSF_V2.curie('controls'),
                   model_uri=NIST_CSF_V2.controls, domain=None, range=Optional[Union[Union[dict, CSFCategory], list[Union[dict, CSFCategory]]]])

slots.props = Slot(uri=NIST_CSF_V2.props, name="props", curie=NIST_CSF_V2.curie('props'),
                   model_uri=NIST_CSF_V2.props, domain=None, range=Optional[Union[Union[dict, CSFProperty], list[Union[dict, CSFProperty]]]])

slots.links = Slot(uri=NIST_CSF_V2.links, name="links", curie=NIST_CSF_V2.curie('links'),
                   model_uri=NIST_CSF_V2.links, domain=None, range=Optional[Union[Union[dict, Link], list[Union[dict, Link]]]])

slots.parts = Slot(uri=NIST_CSF_V2.parts, name="parts", curie=NIST_CSF_V2.curie('parts'),
                   model_uri=NIST_CSF_V2.parts, domain=None, range=Optional[Union[Union[dict, CSFPart], list[Union[dict, CSFPart]]]])

slots.roles = Slot(uri=NIST_CSF_V2.roles, name="roles", curie=NIST_CSF_V2.curie('roles'),
                   model_uri=NIST_CSF_V2.roles, domain=None, range=Optional[Union[Union[dict, Role], list[Union[dict, Role]]]])

slots.parties = Slot(uri=NIST_CSF_V2.parties, name="parties", curie=NIST_CSF_V2.curie('parties'),
                   model_uri=NIST_CSF_V2.parties, domain=None, range=Optional[Union[Union[dict, Party], list[Union[dict, Party]]]])

slots.responsible_parties = Slot(uri=NIST_CSF_V2.responsible_parties, name="responsible-parties", curie=NIST_CSF_V2.curie('responsible_parties'),
                   model_uri=NIST_CSF_V2.responsible_parties, domain=None, range=Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]])

slots.back_matter = Slot(uri=NIST_CSF_V2.back_matter, name="back-matter", curie=NIST_CSF_V2.curie('back_matter'),
                   model_uri=NIST_CSF_V2.back_matter, domain=None, range=Optional[Union[dict, BackMatter]])

slots.resources = Slot(uri=NIST_CSF_V2.resources, name="resources", curie=NIST_CSF_V2.curie('resources'),
                   model_uri=NIST_CSF_V2.resources, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.rlinks = Slot(uri=NIST_CSF_V2.rlinks, name="rlinks", curie=NIST_CSF_V2.curie('rlinks'),
                   model_uri=NIST_CSF_V2.rlinks, domain=None, range=Optional[Union[Union[dict, ResourceLink], list[Union[dict, ResourceLink]]]])

slots.addresses = Slot(uri=NIST_CSF_V2.addresses, name="addresses", curie=NIST_CSF_V2.curie('addresses'),
                   model_uri=NIST_CSF_V2.addresses, domain=None, range=Optional[Union[Union[dict, Address], list[Union[dict, Address]]]])

slots.id = Slot(uri=NIST_CSF_V2.id, name="id", curie=NIST_CSF_V2.curie('id'),
                   model_uri=NIST_CSF_V2.id, domain=None, range=Optional[str])

slots.uuid = Slot(uri=NIST_CSF_V2.uuid, name="uuid", curie=NIST_CSF_V2.curie('uuid'),
                   model_uri=NIST_CSF_V2.uuid, domain=None, range=Optional[str])

slots.title = Slot(uri=NIST_CSF_V2.title, name="title", curie=NIST_CSF_V2.curie('title'),
                   model_uri=NIST_CSF_V2.title, domain=None, range=Optional[str])

slots.published = Slot(uri=NIST_CSF_V2.published, name="published", curie=NIST_CSF_V2.curie('published'),
                   model_uri=NIST_CSF_V2.published, domain=None, range=Optional[str])

slots.last_modified = Slot(uri=NIST_CSF_V2.last_modified, name="last-modified", curie=NIST_CSF_V2.curie('last_modified'),
                   model_uri=NIST_CSF_V2.last_modified, domain=None, range=Optional[str])

slots.version = Slot(uri=NIST_CSF_V2.version, name="version", curie=NIST_CSF_V2.curie('version'),
                   model_uri=NIST_CSF_V2.version, domain=None, range=Optional[str])

slots.oscal_version = Slot(uri=NIST_CSF_V2.oscal_version, name="oscal-version", curie=NIST_CSF_V2.curie('oscal_version'),
                   model_uri=NIST_CSF_V2.oscal_version, domain=None, range=Optional[str])

slots._class = Slot(uri=NIST_CSF_V2._class, name="_class", curie=NIST_CSF_V2.curie('_class'),
                   model_uri=NIST_CSF_V2._class, domain=None, range=Optional[str])

slots.name = Slot(uri=NIST_CSF_V2.name, name="name", curie=NIST_CSF_V2.curie('name'),
                   model_uri=NIST_CSF_V2.name, domain=None, range=Optional[str])

slots.value = Slot(uri=NIST_CSF_V2.value, name="value", curie=NIST_CSF_V2.curie('value'),
                   model_uri=NIST_CSF_V2.value, domain=None, range=Optional[str])

slots.ns = Slot(uri=NIST_CSF_V2.ns, name="ns", curie=NIST_CSF_V2.curie('ns'),
                   model_uri=NIST_CSF_V2.ns, domain=None, range=Optional[str])

slots.prose = Slot(uri=NIST_CSF_V2.prose, name="prose", curie=NIST_CSF_V2.curie('prose'),
                   model_uri=NIST_CSF_V2.prose, domain=None, range=Optional[str])

slots.remarks = Slot(uri=NIST_CSF_V2.remarks, name="remarks", curie=NIST_CSF_V2.curie('remarks'),
                   model_uri=NIST_CSF_V2.remarks, domain=None, range=Optional[str])

slots.href = Slot(uri=NIST_CSF_V2.href, name="href", curie=NIST_CSF_V2.curie('href'),
                   model_uri=NIST_CSF_V2.href, domain=None, range=Optional[str])

slots.rel = Slot(uri=NIST_CSF_V2.rel, name="rel", curie=NIST_CSF_V2.curie('rel'),
                   model_uri=NIST_CSF_V2.rel, domain=None, range=Optional[str])

slots.type = Slot(uri=NIST_CSF_V2.type, name="type", curie=NIST_CSF_V2.curie('type'),
                   model_uri=NIST_CSF_V2.type, domain=None, range=Optional[str])

slots.short_name = Slot(uri=NIST_CSF_V2.short_name, name="short-name", curie=NIST_CSF_V2.curie('short_name'),
                   model_uri=NIST_CSF_V2.short_name, domain=None, range=Optional[str])

slots.email_addresses = Slot(uri=NIST_CSF_V2.email_addresses, name="email-addresses", curie=NIST_CSF_V2.curie('email_addresses'),
                   model_uri=NIST_CSF_V2.email_addresses, domain=None, range=Optional[Union[str, list[str]]])

slots.addr_lines = Slot(uri=NIST_CSF_V2.addr_lines, name="addr-lines", curie=NIST_CSF_V2.curie('addr_lines'),
                   model_uri=NIST_CSF_V2.addr_lines, domain=None, range=Optional[Union[str, list[str]]])

slots.city = Slot(uri=NIST_CSF_V2.city, name="city", curie=NIST_CSF_V2.curie('city'),
                   model_uri=NIST_CSF_V2.city, domain=None, range=Optional[str])

slots.state = Slot(uri=NIST_CSF_V2.state, name="state", curie=NIST_CSF_V2.curie('state'),
                   model_uri=NIST_CSF_V2.state, domain=None, range=Optional[str])

slots.postal_code = Slot(uri=NIST_CSF_V2.postal_code, name="postal-code", curie=NIST_CSF_V2.curie('postal_code'),
                   model_uri=NIST_CSF_V2.postal_code, domain=None, range=Optional[str])

slots.role_id = Slot(uri=NIST_CSF_V2.role_id, name="role-id", curie=NIST_CSF_V2.curie('role_id'),
                   model_uri=NIST_CSF_V2.role_id, domain=None, range=Optional[str])

slots.party_uuids = Slot(uri=NIST_CSF_V2.party_uuids, name="party-uuids", curie=NIST_CSF_V2.curie('party_uuids'),
                   model_uri=NIST_CSF_V2.party_uuids, domain=None, range=Optional[Union[str, list[str]]])

slots.media_type = Slot(uri=NIST_CSF_V2.media_type, name="media-type", curie=NIST_CSF_V2.curie('media_type'),
                   model_uri=NIST_CSF_V2.media_type, domain=None, range=Optional[str])

slots.CSFElement__class = Slot(uri=NIST_CSF_V2._class, name="CSFElement__class", curie=NIST_CSF_V2.curie('_class'),
                   model_uri=NIST_CSF_V2.CSFElement__class, domain=CSFElement, range=Optional[Union[str, "CSFElementClassValue"]])

slots.CSFCategory_controls = Slot(uri=NIST_CSF_V2.controls, name="CSFCategory_controls", curie=NIST_CSF_V2.curie('controls'),
                   model_uri=NIST_CSF_V2.CSFCategory_controls, domain=CSFCategory, range=Optional[Union[Union[dict, "CSFSubcategory"], list[Union[dict, "CSFSubcategory"]]]])

