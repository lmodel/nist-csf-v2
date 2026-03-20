from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "2.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'nist_csf_v2',
     'default_range': 'string',
     'description': 'NIST Cybersecurity Framework 2.0',
     'id': 'https://w3id.org/lmodel/nist-csf-v2',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'nist-csf-v2',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_csf_v2': {'prefix_prefix': 'nist_csf_v2',
                                  'prefix_reference': 'https://w3id.org/lmodel/nist-csf-v2/'}},
     'see_also': ['https://lmodel.github.io/nist-csf-v2'],
     'source': 'https://doi.org/10.6028/NIST.CSWP.29',
     'source_file': 'src/nist_csf_v2/schema/nist_csf_v2.yaml',
     'subsets': {'nist_csf_v2_catalog': {'description': 'NIST CSF 2.0 Catalog '
                                                        'subset for functions, '
                                                        'categories, and '
                                                        'subcategories',
                                         'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
                                         'name': 'nist_csf_v2_catalog'}},
     'title': 'nist-csf-v2'} )

class CSFElementClassValue(str, Enum):
    """
    Allowed class values for CSF catalog elements
    """
    function = "function"
    category = "category"
    subcategory = "subcategory"



class CSFElement(ConfiguredBaseModel):
    """
    Abstract base class for CSF catalog elements
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'in_subset': ['nist_csf_v2_catalog'],
         'slot_usage': {'_class': {'name': '_class', 'range': 'CSFElementClassValue'}}})

    id: Optional[str] = Field(default=None, description="""Unique identifier for a catalog element""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement', 'CSFPart', 'Role'],
         'in_subset': ['nist_csf_v2_catalog']} })
    class_: Optional[CSFElementClassValue] = Field(default=None, alias="class", description="""Classification of a CSF catalog element (function, category, subcategory)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement'], 'in_subset': ['nist_csf_v2_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFMetadata', 'CSFElement', 'Role', 'Resource'],
         'in_subset': ['nist_csf_v2_catalog']} })
    props: Optional[list[CSFProperty]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFMetadata', 'CSFElement'],
         'in_subset': ['nist_csf_v2_catalog']} })
    parts: Optional[list[Any]] = Field(default=None, description="""Structured narrative parts (e.g., statement, overview, example)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement'], 'in_subset': ['nist_csf_v2_catalog']} })


class CSFFunction(CSFElement):
    """
    A CSF function - top-level grouping (e.g. GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'in_subset': ['nist_csf_v2_catalog']})

    controls: Optional[list[CSFCategory]] = Field(default=None, description="""List of categories or subcategories within a function or category""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFFunction', 'CSFCategory'],
         'in_subset': ['nist_csf_v2_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for a catalog element""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement', 'CSFPart', 'Role'],
         'in_subset': ['nist_csf_v2_catalog']} })
    class_: Optional[CSFElementClassValue] = Field(default=None, alias="class", description="""Classification of a CSF catalog element (function, category, subcategory)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement'], 'in_subset': ['nist_csf_v2_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFMetadata', 'CSFElement', 'Role', 'Resource'],
         'in_subset': ['nist_csf_v2_catalog']} })
    props: Optional[list[CSFProperty]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFMetadata', 'CSFElement'],
         'in_subset': ['nist_csf_v2_catalog']} })
    parts: Optional[list[Any]] = Field(default=None, description="""Structured narrative parts (e.g., statement, overview, example)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement'], 'in_subset': ['nist_csf_v2_catalog']} })


class CSFCategory(CSFElement):
    """
    A CSF category - second-level grouping within a function (e.g. GV.OC Organizational Context, ID.AM Asset Management)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'in_subset': ['nist_csf_v2_catalog'],
         'slot_usage': {'controls': {'name': 'controls', 'range': 'CSFSubcategory'}}})

    controls: Optional[list[CSFSubcategory]] = Field(default=None, description="""List of categories or subcategories within a function or category""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFFunction', 'CSFCategory'],
         'in_subset': ['nist_csf_v2_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for a catalog element""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement', 'CSFPart', 'Role'],
         'in_subset': ['nist_csf_v2_catalog']} })
    class_: Optional[CSFElementClassValue] = Field(default=None, alias="class", description="""Classification of a CSF catalog element (function, category, subcategory)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement'], 'in_subset': ['nist_csf_v2_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFMetadata', 'CSFElement', 'Role', 'Resource'],
         'in_subset': ['nist_csf_v2_catalog']} })
    props: Optional[list[CSFProperty]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFMetadata', 'CSFElement'],
         'in_subset': ['nist_csf_v2_catalog']} })
    parts: Optional[list[Any]] = Field(default=None, description="""Structured narrative parts (e.g., statement, overview, example)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement'], 'in_subset': ['nist_csf_v2_catalog']} })


class CSFSubcategory(CSFElement):
    """
    A CSF subcategory - specific cybersecurity outcome (e.g. GV.OC-01, ID.AM-01)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'in_subset': ['nist_csf_v2_catalog']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for a catalog element""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement', 'CSFPart', 'Role'],
         'in_subset': ['nist_csf_v2_catalog']} })
    class_: Optional[CSFElementClassValue] = Field(default=None, alias="class", description="""Classification of a CSF catalog element (function, category, subcategory)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement'], 'in_subset': ['nist_csf_v2_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFMetadata', 'CSFElement', 'Role', 'Resource'],
         'in_subset': ['nist_csf_v2_catalog']} })
    props: Optional[list[CSFProperty]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFMetadata', 'CSFElement'],
         'in_subset': ['nist_csf_v2_catalog']} })
    parts: Optional[list[Any]] = Field(default=None, description="""Structured narrative parts (e.g., statement, overview, example)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement'], 'in_subset': ['nist_csf_v2_catalog']} })


class CSFProperty(ConfiguredBaseModel):
    """
    A name-value property with optional namespace and supplemental remarks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'in_subset': ['nist_csf_v2_catalog']})

    name: Optional[str] = Field(default=None, description="""Name of a property or part""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFPart', 'CSFProperty', 'Party'],
         'in_subset': ['nist_csf_v2_catalog']} })
    value: Optional[str] = Field(default=None, description="""Property value""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFProperty'], 'in_subset': ['nist_csf_v2_catalog']} })
    ns: Optional[str] = Field(default=None, description="""Namespace URI for a property or part""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFPart', 'CSFProperty'], 'in_subset': ['nist_csf_v2_catalog']} })
    remarks: Optional[str] = Field(default=None, description="""Supplemental remarks on a property""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFProperty'], 'in_subset': ['nist_csf_v2_catalog']} })


class Link(ConfiguredBaseModel):
    """
    Relationship link with href and optional rel attribute
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'in_subset': ['nist_csf_v2_catalog']})

    href: Optional[str] = Field(default=None, description="""Link or resource reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link', 'ResourceLink'], 'in_subset': ['nist_csf_v2_catalog']} })
    rel: Optional[str] = Field(default=None, description="""Relationship type for a link""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link'], 'in_subset': ['nist_csf_v2_catalog']} })


class Role(ConfiguredBaseModel):
    """
    Role definition used in metadata
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'in_subset': ['nist_csf_v2_catalog']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for a catalog element""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFElement', 'CSFPart', 'Role'],
         'in_subset': ['nist_csf_v2_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['CSFMetadata', 'CSFElement', 'Role', 'Resource'],
         'in_subset': ['nist_csf_v2_catalog']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CSFElement.model_rebuild()
CSFFunction.model_rebuild()
CSFCategory.model_rebuild()
CSFSubcategory.model_rebuild()
CSFProperty.model_rebuild()
Link.model_rebuild()
Role.model_rebuild()
