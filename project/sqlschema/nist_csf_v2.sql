-- # Class: CsfFramework Description: One edition of the CSF as a whole: its functions, each holding its categories and their subcategories.
--     * Slot: id
--     * Slot: csf_version Description: The CSF edition, as NIST numbers it in the publication's title, such as 2.0.
-- # Class: CsfFunction Description: One of the six functions that sort the CSF's outcomes at the highest level: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND and RECOVER. Each is named by two letters and described in a sentence.
--     * Slot: id
--     * Slot: title Description: The name CSWP 29 gives the function or category.
--     * Slot: description Description: What the function, category, subcategory or example says, in the words of whoever records it.
--     * Slot: csf_function_id Description: The function's two letters, such as GV for GOVERN.
--     * Slot: CsfFramework_id Description: Autocreated FK slot
-- # Class: CsfCategory Description: A group of related cybersecurity outcomes within a function, such as Organizational Context (GV.OC), or a CSF 1.1 category that CSF 2.0 withdrew, which the catalog keeps with its status and, where NIST recorded it, where it moved or what incorporated it.
--     * Slot: id
--     * Slot: title Description: The name CSWP 29 gives the function or category.
--     * Slot: description Description: What the function, category, subcategory or example says, in the words of whoever records it.
--     * Slot: csf_category_id Description: The category's identifier, such as GV.OC.
--     * Slot: category_status Description: withdrawn for a CSF 1.1 category that CSF 2.0 withdrew. A category of CSF 2.0 has no status.
--     * Slot: CsfFunction_id Description: Autocreated FK slot
-- # Class: CsfSubcategory Description: A cybersecurity outcome: one statement of a result within a category, such as GV.OC-01, or a CSF 1.1 subcategory that CSF 2.0 withdrew, which the catalog keeps with its statement, its status and where it moved or what incorporated it.
--     * Slot: id
--     * Slot: description Description: What the function, category, subcategory or example says, in the words of whoever records it.
--     * Slot: csf_subcategory_id Description: The subcategory's identifier, such as GV.OC-01.
--     * Slot: subcategory_status Description: withdrawn for a CSF 1.1 subcategory that CSF 2.0 withdrew. A subcategory of CSF 2.0 has no status.
--     * Slot: CsfCategory_id Description: Autocreated FK slot
-- # Class: CsfImplementationExample Description: An implementation example: one concise, action-oriented step that could help achieve a subcategory's outcome. NIST publishes the examples beside the Core, in its reference tool and its catalog, not in CSWP 29 itself.
--     * Slot: id
--     * Slot: description Description: What the function, category, subcategory or example says, in the words of whoever records it.
--     * Slot: csf_implementation_example_id Description: The example's identifier in NIST's reference data, such as GV.OC-01.001 for the first example of subcategory GV.OC-01.
--     * Slot: CsfSubcategory_id Description: Autocreated FK slot
-- # Class: CsfCategory_category_moved_to
--     * Slot: CsfCategory_id Description: Autocreated FK slot
--     * Slot: category_moved_to Description: The CSF 2.0 category a withdrawn category moved to, as the catalog states it, such as PR.AA for PR.AC.
-- # Class: CsfCategory_category_incorporated_into
--     * Slot: CsfCategory_id Description: Autocreated FK slot
--     * Slot: category_incorporated_into Description: The function, category or subcategory of CSF 2.0 that took in a withdrawn category's outcomes, as the catalog states it, such as GV.OC for ID.BE. The catalog names none for some withdrawn categories.
-- # Class: CsfSubcategory_subcategory_moved_to
--     * Slot: CsfSubcategory_id Description: Autocreated FK slot
--     * Slot: subcategory_moved_to Description: The CSF 2.0 subcategory a withdrawn subcategory moved to, as the catalog states it, such as GV.OC-03 for ID.GV-03. The catalog names two for a few.
-- # Class: CsfSubcategory_subcategory_incorporated_into
--     * Slot: CsfSubcategory_id Description: Autocreated FK slot
--     * Slot: subcategory_incorporated_into Description: The CSF 2.0 category or subcategory that took in a withdrawn subcategory's outcome, as the catalog states it, such as GV.OC-01 for ID.BE-02.

CREATE TABLE "CsfFramework" (
	id INTEGER NOT NULL,
	csf_version TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CsfFramework_id" ON "CsfFramework" (id);

CREATE TABLE "CsfFunction" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	csf_function_id TEXT NOT NULL,
	"CsfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CsfFramework_id") REFERENCES "CsfFramework" (id)
);
CREATE INDEX "ix_CsfFunction_id" ON "CsfFunction" (id);

CREATE TABLE "CsfCategory" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	csf_category_id TEXT NOT NULL,
	category_status VARCHAR(9),
	"CsfFunction_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CsfFunction_id") REFERENCES "CsfFunction" (id)
);
CREATE INDEX "ix_CsfCategory_id" ON "CsfCategory" (id);

CREATE TABLE "CsfSubcategory" (
	id INTEGER NOT NULL,
	description TEXT NOT NULL,
	csf_subcategory_id TEXT NOT NULL,
	subcategory_status VARCHAR(9),
	"CsfCategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CsfCategory_id") REFERENCES "CsfCategory" (id)
);
CREATE INDEX "ix_CsfSubcategory_id" ON "CsfSubcategory" (id);

CREATE TABLE "CsfCategory_category_moved_to" (
	"CsfCategory_id" INTEGER,
	category_moved_to TEXT,
	PRIMARY KEY ("CsfCategory_id", category_moved_to),
	FOREIGN KEY("CsfCategory_id") REFERENCES "CsfCategory" (id)
);
CREATE INDEX "ix_CsfCategory_category_moved_to_category_moved_to" ON "CsfCategory_category_moved_to" (category_moved_to);
CREATE INDEX "ix_CsfCategory_category_moved_to_CsfCategory_id" ON "CsfCategory_category_moved_to" ("CsfCategory_id");

CREATE TABLE "CsfCategory_category_incorporated_into" (
	"CsfCategory_id" INTEGER,
	category_incorporated_into TEXT,
	PRIMARY KEY ("CsfCategory_id", category_incorporated_into),
	FOREIGN KEY("CsfCategory_id") REFERENCES "CsfCategory" (id)
);
CREATE INDEX "ix_CsfCategory_category_incorporated_into_category_incorporated_into" ON "CsfCategory_category_incorporated_into" (category_incorporated_into);
CREATE INDEX "ix_CsfCategory_category_incorporated_into_CsfCategory_id" ON "CsfCategory_category_incorporated_into" ("CsfCategory_id");

CREATE TABLE "CsfImplementationExample" (
	id INTEGER NOT NULL,
	description TEXT NOT NULL,
	csf_implementation_example_id TEXT NOT NULL,
	"CsfSubcategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CsfSubcategory_id") REFERENCES "CsfSubcategory" (id)
);
CREATE INDEX "ix_CsfImplementationExample_id" ON "CsfImplementationExample" (id);

CREATE TABLE "CsfSubcategory_subcategory_moved_to" (
	"CsfSubcategory_id" INTEGER,
	subcategory_moved_to TEXT,
	PRIMARY KEY ("CsfSubcategory_id", subcategory_moved_to),
	FOREIGN KEY("CsfSubcategory_id") REFERENCES "CsfSubcategory" (id)
);
CREATE INDEX "ix_CsfSubcategory_subcategory_moved_to_subcategory_moved_to" ON "CsfSubcategory_subcategory_moved_to" (subcategory_moved_to);
CREATE INDEX "ix_CsfSubcategory_subcategory_moved_to_CsfSubcategory_id" ON "CsfSubcategory_subcategory_moved_to" ("CsfSubcategory_id");

CREATE TABLE "CsfSubcategory_subcategory_incorporated_into" (
	"CsfSubcategory_id" INTEGER,
	subcategory_incorporated_into TEXT,
	PRIMARY KEY ("CsfSubcategory_id", subcategory_incorporated_into),
	FOREIGN KEY("CsfSubcategory_id") REFERENCES "CsfSubcategory" (id)
);
CREATE INDEX "ix_CsfSubcategory_subcategory_incorporated_into_subcategory_incorporated_into" ON "CsfSubcategory_subcategory_incorporated_into" (subcategory_incorporated_into);
CREATE INDEX "ix_CsfSubcategory_subcategory_incorporated_into_CsfSubcategory_id" ON "CsfSubcategory_subcategory_incorporated_into" ("CsfSubcategory_id");
