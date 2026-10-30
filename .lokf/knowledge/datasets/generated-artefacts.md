---
type: Dataset
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What the LinkML generators and `lokf adapt` write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel and Java), the Python dataclasses and Pydantic models in `src/nist_csf_v2/datamodel/`, `docs/schema/` and `docs/elements/`, and `.lokf/nist-csf-v2.yaml`. None is edited by hand."
resource: project
isPartOf:
  - https://w3id.org/lmodel/nist-csf-v2/knowledge/datasets/nist-csf-v2-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project, gen-doc and test recipes
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the generators' settings
  - id: project
    resource: project
    title: the generated folders
  - resource: src/nist_csf_v2/datamodel
    title: the Python models
  - resource: docs/schema
    title: the YAML gen-doc writes
  - id: pre-commit-config.yaml
    resource: .pre-commit-config.yaml
    title: the exclude pattern
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:42:52Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:07:28Z"
---

# Generated artefacts

Every file here is generated from `src/nist_csf_v2/schema/nist_csf_v2.yaml`, so a change starts in the schema and the recipes rewrite the rest.

`just gen-project` runs `gen-project` with `.linkml/generators.yaml` into `project/`, moves the Python dataclasses into `src/nist_csf_v2/datamodel/`, and writes the Pydantic models beside them. It then runs `gen-java`, `gen-typescript` and `gen-owl` separately, because some generators ignore the configuration or cannot create their folders, as its comment says.[^justfile] `.linkml/generators.yaml` leaves out the Markdown generator and merges imports for the others.[^generators.yaml] `project/` holds a folder each for Excel, GraphQL, Java, JSON-LD, JSON Schema, OWL, the prefix map, protobuf, SHACL, ShEx, SQL and TypeScript.[^project] The Java folder holds one class per schema class, five in all.

`just gen-doc` writes `docs/schema/nist_csf_v2.yaml` and the element pages under `docs/elements/`, which git ignores and the website builds. `just lokf-adapt` writes `.lokf/nist-csf-v2.yaml`. `just test` regenerates the dataclasses too, and under LinkML 1.12.1 it leaves no change, because the generated files carry no generation date.

The pre-commit hooks leave these folders alone, with NIST's catalog copy, the neighbours' copies and the sidecar's scripts, because no hook may rewrite a file the repository does not write by hand.[^pre-commit-config.yaml]

[^justfile]: justfile, the gen-project and gen-doc recipes
[^generators.yaml]: .linkml/generators.yaml, excludes and generator_args
[^project]: project, its folders
[^pre-commit-config.yaml]: .pre-commit-config.yaml, the exclude pattern and its comment
