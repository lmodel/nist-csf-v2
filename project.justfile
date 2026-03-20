## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Validate a representative catalog document with the catalog schema.
validate-catalog:
        uv run linkml validate \
                -s src/nist_csf_v2/schema/nist_csf_v2.yaml \
                tests/data/nist/NIST_CSF_v2.0_catalog.yaml

