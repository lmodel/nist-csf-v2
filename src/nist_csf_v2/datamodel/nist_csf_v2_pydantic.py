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


linkml_meta = LinkMLMeta({'annotations': {'cprt_framework_version': {'tag': 'cprt_framework_version',
                                                'value': 'CSF_2_0_0'},
                     'oscal_content_commit': {'tag': 'oscal_content_commit',
                                              'value': 'f0de6d8d8c059d374f15e0ae07508d82e370fc1d'},
                     'oscal_content_tag': {'tag': 'oscal_content_tag',
                                           'value': 'v1.6.0'},
                     'publication_date': {'tag': 'publication_date',
                                          'value': '2024-02'}},
     'comments': ['The version is the CSF edition that CSWP 29 defines, and source '
                  "is the publication's digital object identifier. NIST's "
                  'Cybersecurity and Privacy Reference Tool names the same edition '
                  'CSF_2_0_0, and the catalog NIST publishes for it in '
                  'usnistgov/oscal-content is copied to '
                  'src/nist_csf_v2/schema/oscal-content/ at the tag and commit in '
                  'the annotations. That catalog carries a version number of its '
                  'own, 1.2.1, which numbers the catalog and not the framework. '
                  "The release tags are the schema's own versions, and "
                  'scripts/check_upstream_release.py reads the same pins and '
                  'reports when NIST publishes another edition or changes the '
                  'catalog.',
                  'CSWP 29 is a work of the United States Government and is not '
                  'subject to copyright in the United States. The descriptions '
                  "here are this project's own words; NIST's text of each "
                  'function, category, subcategory and example stays in the '
                  'catalog copy.',
                  "NIST's catalog renders each function as an OSCAL group, each "
                  'category and subcategory as an OSCAL control and each '
                  'implementation example as a part. The broad_mappings name those '
                  'lmodel/oscal classes. A withdrawn category or subcategory is a '
                  'control with a status property and links to where it moved or '
                  "what incorporated it; the schema carries those as the element's "
                  'status and identifiers.',
                  'The catalog also marks most CSF 2.0 subcategories as '
                  'first-party risk, third-party risk or both, in a marking '
                  'property of class risk-party. CSWP 29 carries no such marking, '
                  "so it is the reference tool's and the schema leaves it out."],
     'default_prefix': 'nist_csf_v2',
     'default_range': 'string',
     'description': 'A LinkML model of the Cybersecurity Framework (CSF) 2.0, '
                    'which NIST publishes as Cybersecurity White Paper (CSWP) 29: '
                    'its six functions, their categories and subcategories, the '
                    'implementation examples NIST publishes with the '
                    'subcategories, and the CSF 1.1 categories and subcategories '
                    'that CSF 2.0 withdrew, each with its status and, where NIST '
                    'recorded it, where it moved or what incorporated it.',
     'id': 'https://w3id.org/lmodel/nist-csf-v2',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'nist_csf_v2',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_csf_v2': {'prefix_prefix': 'nist_csf_v2',
                                  'prefix_reference': 'https://w3id.org/lmodel/nist-csf-v2/'},
                  'oscal': {'prefix_prefix': 'oscal',
                            'prefix_reference': 'https://w3id.org/lmodel/oscal/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/nist-csf-v2',
                  'https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final',
                  'https://www.nist.gov/cyberframework',
                  'https://github.com/usnistgov/oscal-content/tree/v1.6.0/nist.gov/CSF/v2.0'],
     'source': 'https://doi.org/10.6028/NIST.CSWP.29',
     'source_file': 'src/nist_csf_v2/schema/nist_csf_v2.yaml',
     'title': 'The NIST Cybersecurity Framework (CSF) 2.0',
     'types': {'csf_category_identifier': {'base': 'str',
                                           'description': "A category's "
                                                          'identifier: its '
                                                          "function's letters, a "
                                                          'dot and two letters for '
                                                          'the category, such as '
                                                          'GV.OC for '
                                                          'Organizational Context.',
                                           'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
                                           'name': 'csf_category_identifier',
                                           'pattern': '^(GV|ID|PR|DE|RS|RC)\\.[A-Z]{2}$',
                                           'typeof': 'string',
                                           'uri': 'xsd:string'},
               'csf_element_identifier': {'base': 'str',
                                          'description': 'The identifier of a '
                                                         'function, a category or '
                                                         'a subcategory, whichever '
                                                         'of the three a withdrawn '
                                                         'element names as what '
                                                         'incorporated it.',
                                          'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
                                          'name': 'csf_element_identifier',
                                          'pattern': '^(GV|ID|PR|DE|RS|RC)(\\.[A-Z]{2}(-[0-9]{2})?)?$',
                                          'typeof': 'string',
                                          'uri': 'xsd:string'},
               'csf_function_identifier': {'base': 'str',
                                           'description': 'The two letters that '
                                                          'name one of the six '
                                                          'functions, such as GV '
                                                          'for GOVERN.',
                                           'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
                                           'name': 'csf_function_identifier',
                                           'pattern': '^(GV|ID|PR|DE|RS|RC)$',
                                           'typeof': 'string',
                                           'uri': 'xsd:string'},
               'csf_implementation_example_identifier': {'base': 'str',
                                                         'description': 'The '
                                                                        'identifier '
                                                                        "NIST's "
                                                                        'reference '
                                                                        'data '
                                                                        'gives an '
                                                                        'implementation '
                                                                        'example: '
                                                                        'its '
                                                                        "subcategory's "
                                                                        'identifier, '
                                                                        'a dot and '
                                                                        'a '
                                                                        'three-digit '
                                                                        'number, '
                                                                        'such as '
                                                                        'GV.OC-01.001. '
                                                                        'The '
                                                                        'numbers '
                                                                        'run once '
                                                                        'through '
                                                                        'the whole '
                                                                        'Core, so '
                                                                        'no two '
                                                                        'examples '
                                                                        'share '
                                                                        'one.',
                                                         'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
                                                         'name': 'csf_implementation_example_identifier',
                                                         'pattern': '^(GV|ID|PR|DE|RS|RC)\\.[A-Z]{2}-[0-9]{2}\\.[0-9]{3}$',
                                                         'typeof': 'string',
                                                         'uri': 'xsd:string'},
               'csf_subcategory_identifier': {'base': 'str',
                                              'description': "A subcategory's "
                                                             'identifier: its '
                                                             "category's "
                                                             'identifier, a hyphen '
                                                             'and a two-digit '
                                                             'number, such as '
                                                             'GV.OC-01. CSWP 29 '
                                                             'says the numbers are '
                                                             'not sequential on '
                                                             'purpose: a gap marks '
                                                             'a CSF 1.1 '
                                                             'subcategory that CSF '
                                                             '2.0 moved elsewhere.',
                                              'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
                                              'name': 'csf_subcategory_identifier',
                                              'pattern': '^(GV|ID|PR|DE|RS|RC)\\.[A-Z]{2}-[0-9]{2}$',
                                              'typeof': 'string',
                                              'uri': 'xsd:string'}}} )

class CsfElementStatus(str, Enum):
    """
    The state the catalog gives a category or subcategory that CSF 2.0 no longer carries. A category or subcategory of CSF 2.0 has no status.
    """
    withdrawn = "withdrawn"
    """
    The element was in CSF 1.1 and CSF 2.0 withdrew it. The catalog keeps it, and names where it moved or what incorporated it where NIST recorded that.
    """



class CsfFramework(ConfiguredBaseModel):
    """
    One edition of the CSF as a whole: its functions, each holding its categories and their subcategories.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Catalog'],
         'class_uri': 'nist_csf_v2:Framework',
         'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'see_also': ['https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final'],
         'tree_root': True})

    csf_version: str = Field(default=..., description="""The CSF edition, as NIST numbers it in the publication's title, such as 2.0.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfFramework']} })
    csf_functions: list[CsfFunction] = Field(default=..., description="""The six functions, in the order CSWP 29 gives them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfFramework']} })

    @field_validator('csf_version')
    def pattern_csf_version(cls, v):
        pattern=re.compile(r"^[0-9]+\.[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid csf_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid csf_version format: {v}"
            raise ValueError(err_msg)
        return v


class CsfFunction(ConfiguredBaseModel):
    """
    One of the six functions that sort the CSF's outcomes at the highest level: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND and RECOVER. Each is named by two letters and described in a sentence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Group'],
         'class_uri': 'nist_csf_v2:Function',
         'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'see_also': ['https://www.nist.gov/cyberframework']})

    title: Optional[str] = Field(default=None, description="""The name CSWP 29 gives the function or category.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['CsfFunction', 'CsfCategory'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the function, category, subcategory or example says, in the words of whoever records it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['CsfFunction',
                       'CsfCategory',
                       'CsfSubcategory',
                       'CsfImplementationExample'],
         'slot_uri': 'schema:description'} })
    csf_function_id: str = Field(default=..., description="""The function's two letters, such as GV for GOVERN.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfFunction']} })
    function_categories: Optional[list[CsfCategory]] = Field(default=None, description="""The categories of the function. A knowledge bundle relates a category to its function with isPartOf instead.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfFunction']} })


class CsfCategory(ConfiguredBaseModel):
    """
    A group of related cybersecurity outcomes within a function, such as Organizational Context (GV.OC), or a CSF 1.1 category that CSF 2.0 withdrew, which the catalog keeps with its status and, where NIST recorded it, where it moved or what incorporated it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Control'],
         'class_uri': 'nist_csf_v2:Category',
         'comments': ['A withdrawn category keeps its CSF 1.1 subcategories, each '
                      'withdrawn too, and the catalog gives it no statement, so it has '
                      'no description.'],
         'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'see_also': ['https://www.nist.gov/cyberframework']})

    title: Optional[str] = Field(default=None, description="""The name CSWP 29 gives the function or category.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['CsfFunction', 'CsfCategory'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the function, category, subcategory or example says, in the words of whoever records it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['CsfFunction',
                       'CsfCategory',
                       'CsfSubcategory',
                       'CsfImplementationExample'],
         'slot_uri': 'schema:description'} })
    csf_category_id: str = Field(default=..., description="""The category's identifier, such as GV.OC.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfCategory']} })
    category_subcategories: Optional[list[CsfSubcategory]] = Field(default=None, description="""The subcategories of the category. A knowledge bundle relates a subcategory to its category with isPartOf instead.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfCategory']} })
    category_status: Optional[CsfElementStatus] = Field(default=None, description="""withdrawn for a CSF 1.1 category that CSF 2.0 withdrew. A category of CSF 2.0 has no status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfCategory']} })
    category_moved_to: Optional[list[str]] = Field(default=None, description="""The CSF 2.0 category a withdrawn category moved to, as the catalog states it, such as PR.AA for PR.AC.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfCategory']} })
    category_incorporated_into: Optional[list[str]] = Field(default=None, description="""The function, category or subcategory of CSF 2.0 that took in a withdrawn category's outcomes, as the catalog states it, such as GV.OC for ID.BE. The catalog names none for some withdrawn categories.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfCategory']} })


class CsfSubcategory(ConfiguredBaseModel):
    """
    A cybersecurity outcome: one statement of a result within a category, such as GV.OC-01, or a CSF 1.1 subcategory that CSF 2.0 withdrew, which the catalog keeps with its statement, its status and where it moved or what incorporated it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Control'],
         'class_uri': 'nist_csf_v2:Subcategory',
         'comments': ['A subcategory has no title of its own: its identifier names it '
                      'and its statement is its description, which is why the '
                      'description is required here.'],
         'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'see_also': ['https://www.nist.gov/cyberframework'],
         'slot_usage': {'description': {'name': 'description', 'required': True}}})

    description: str = Field(default=..., description="""What the function, category, subcategory or example says, in the words of whoever records it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['CsfFunction',
                       'CsfCategory',
                       'CsfSubcategory',
                       'CsfImplementationExample'],
         'slot_uri': 'schema:description'} })
    csf_subcategory_id: str = Field(default=..., description="""The subcategory's identifier, such as GV.OC-01.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfSubcategory']} })
    subcategory_examples: Optional[list[CsfImplementationExample]] = Field(default=None, description="""The implementation examples NIST publishes for the subcategory. CSWP 29 says they are notional, that none is required, and that they are not a complete list of what could be done.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfSubcategory']} })
    subcategory_status: Optional[CsfElementStatus] = Field(default=None, description="""withdrawn for a CSF 1.1 subcategory that CSF 2.0 withdrew. A subcategory of CSF 2.0 has no status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfSubcategory']} })
    subcategory_moved_to: Optional[list[str]] = Field(default=None, description="""The CSF 2.0 subcategory a withdrawn subcategory moved to, as the catalog states it, such as GV.OC-03 for ID.GV-03. The catalog names two for a few.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfSubcategory']} })
    subcategory_incorporated_into: Optional[list[str]] = Field(default=None, description="""The CSF 2.0 category or subcategory that took in a withdrawn subcategory's outcome, as the catalog states it, such as GV.OC-01 for ID.BE-02.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfSubcategory']} })


class CsfImplementationExample(ConfiguredBaseModel):
    """
    An implementation example: one concise, action-oriented step that could help achieve a subcategory's outcome. NIST publishes the examples beside the Core, in its reference tool and its catalog, not in CSWP 29 itself.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_csf_v2:ImplementationExample',
         'from_schema': 'https://w3id.org/lmodel/nist-csf-v2',
         'see_also': ['https://www.nist.gov/cyberframework'],
         'slot_usage': {'description': {'name': 'description', 'required': True}}})

    description: str = Field(default=..., description="""What the function, category, subcategory or example says, in the words of whoever records it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['CsfFunction',
                       'CsfCategory',
                       'CsfSubcategory',
                       'CsfImplementationExample'],
         'slot_uri': 'schema:description'} })
    csf_implementation_example_id: str = Field(default=..., description="""The example's identifier in NIST's reference data, such as GV.OC-01.001 for the first example of subcategory GV.OC-01.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CsfImplementationExample']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CsfFramework.model_rebuild()
CsfFunction.model_rebuild()
CsfCategory.model_rebuild()
CsfSubcategory.model_rebuild()
CsfImplementationExample.model_rebuild()
