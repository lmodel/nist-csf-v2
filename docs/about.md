# About nist-csf-v2

This page is for anyone reading the [LinkML](https://linkml.io) schema's
elements: it says how they are named and what the model leaves out.

The Cybersecurity Framework (CSF) 2.0 sorts its outcomes into three levels.
A function is the highest grouping, named by two letters. A category is a
group of related outcomes within a function. A subcategory is one outcome,
stated in a sentence. NIST publishes implementation examples beside the Core,
each a step that could help achieve a subcategory's outcome. The schema gives
each a class, and holds them in one framework document.

Element names are the schema's own. Classes carry the `Csf` prefix
(`CsfCategory`, `CsfSubcategory`) so they can be imported beside other
vocabularies. Slots are snake_case. The keys that hold the functions and the
identifiers carry a `csf_` prefix (`csf_functions`, `csf_category_id`),
because other NIST frameworks also have functions, categories and
subcategories. The identifiers keep the form that the
National Institute of Standards and Technology (NIST) gives them, such as
`GV.OC-01`, and the example identifiers the form of NIST's reference data,
such as `GV.OC-01.001`. The one enum, `CsfElementStatus`, has the one value
NIST's catalog uses, `withdrawn`. Every element is in the `nist_csf_v2:`
namespace (`https://w3id.org/lmodel/nist-csf-v2/`).

The descriptions are this project's own words. NIST's own text of each
function, category, subcategory and example stays in NIST's catalog, which
the repository keeps beside the schema.

## What is left out

The schema models the Core and the implementation examples, the first-party
and third-party risk marking NIST's catalog gives most subcategories, and the
CSF 1.1 categories and subcategories that NIST's catalog keeps as withdrawn.
The examples and the marking are not in CSWP 29: NIST publishes them beside
the Core, in its catalog and its reference tool. The schema holds none of
the publication's prose outside the Core: the Organizational Profiles of
Section 3, the CSF Tiers of Appendix B and the glossary of Appendix C. It
holds no Informative Reference, which NIST publishes apart from the catalog,
and no community profile.

## Reference

- [CSWP 29 on NIST's site](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)
- [The CSF site](https://www.nist.gov/cyberframework)
- [NIST's CSF 2.0 catalog in the Open Security Controls Assessment Language](https://github.com/usnistgov/oscal-content/tree/v1.6.0/nist.gov/CSF/v2.0)
