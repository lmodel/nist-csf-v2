-- # Class: CSFDocument Description: Root wrapper for CSF catalog content
--     * Slot: id
--     * Slot: catalog_id Description: Root catalog payload
-- # Class: CSFCatalogBody Description: Main CSF catalog object
--     * Slot: id
--     * Slot: uuid Description: UUID for catalog or resource element
--     * Slot: metadata_id Description: Catalog metadata
--     * Slot: back_matter_id Description: Back-matter references and resources
-- # Class: CSFMetadata Description: OSCAL metadata section for the CSF catalog
--     * Slot: id
--     * Slot: title Description: Human-readable title
--     * Slot: published Description: Publication timestamp
--     * Slot: last_modified Description: Last modification timestamp
--     * Slot: version Description: Version identifier
--     * Slot: oscal_version Description: OSCAL version identifier
-- # Abstract Class: CSFElement Description: Abstract base class for CSF catalog elements
--     * Slot: uid
--     * Slot: id Description: Unique identifier for a catalog element
--     * Slot: class Description: Classification of a CSF catalog element (function, category, subcategory)
--     * Slot: title Description: Human-readable title
-- # Class: CSFFunction Description: A CSF function - top-level grouping (e.g. GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER)
--     * Slot: uid
--     * Slot: id Description: Unique identifier for a catalog element
--     * Slot: class Description: Classification of a CSF catalog element (function, category, subcategory)
--     * Slot: title Description: Human-readable title
--     * Slot: CSFCatalogBody_id Description: Autocreated FK slot
-- # Class: CSFCategory Description: A CSF category - second-level grouping within a function (e.g. GV.OC Organizational Context, ID.AM Asset Management)
--     * Slot: uid
--     * Slot: id Description: Unique identifier for a catalog element
--     * Slot: class Description: Classification of a CSF catalog element (function, category, subcategory)
--     * Slot: title Description: Human-readable title
--     * Slot: CSFFunction_uid Description: Autocreated FK slot
-- # Class: CSFSubcategory Description: A CSF subcategory - specific cybersecurity outcome (e.g. GV.OC-01, ID.AM-01)
--     * Slot: uid
--     * Slot: id Description: Unique identifier for a catalog element
--     * Slot: class Description: Classification of a CSF catalog element (function, category, subcategory)
--     * Slot: title Description: Human-readable title
--     * Slot: CSFCategory_uid Description: Autocreated FK slot
-- # Class: CSFPart Description: Structured narrative part (statement, overview, or example)
--     * Slot: uid
--     * Slot: id Description: Unique identifier for a catalog element
--     * Slot: name Description: Name of a property or part
--     * Slot: ns Description: Namespace URI for a property or part
--     * Slot: prose Description: Free-text prose content
--     * Slot: CSFElement_uid Description: Autocreated FK slot
--     * Slot: CSFFunction_uid Description: Autocreated FK slot
--     * Slot: CSFCategory_uid Description: Autocreated FK slot
--     * Slot: CSFSubcategory_uid Description: Autocreated FK slot
-- # Class: CSFProperty Description: A name-value property with optional namespace and supplemental remarks
--     * Slot: id
--     * Slot: name Description: Name of a property or part
--     * Slot: value Description: Property value
--     * Slot: ns Description: Namespace URI for a property or part
--     * Slot: remarks Description: Supplemental remarks on a property
--     * Slot: CSFMetadata_id Description: Autocreated FK slot
--     * Slot: CSFElement_uid Description: Autocreated FK slot
--     * Slot: CSFFunction_uid Description: Autocreated FK slot
--     * Slot: CSFCategory_uid Description: Autocreated FK slot
--     * Slot: CSFSubcategory_uid Description: Autocreated FK slot
-- # Class: Link Description: Relationship link with href and optional rel attribute
--     * Slot: id
--     * Slot: href Description: Link or resource reference
--     * Slot: rel Description: Relationship type for a link
--     * Slot: CSFMetadata_id Description: Autocreated FK slot
-- # Class: Role Description: Role definition used in metadata
--     * Slot: uid
--     * Slot: id Description: Unique identifier for a catalog element
--     * Slot: title Description: Human-readable title
--     * Slot: CSFMetadata_id Description: Autocreated FK slot
-- # Class: Party Description: Party definition (person or organization)
--     * Slot: id
--     * Slot: uuid Description: UUID for catalog or resource element
--     * Slot: type Description: Party type (e.g., organization, person)
--     * Slot: name Description: Name of a property or part
--     * Slot: short_name Description: Short display name for a party
--     * Slot: CSFMetadata_id Description: Autocreated FK slot
-- # Class: Address Description: Postal address
--     * Slot: id
--     * Slot: city Description: City name
--     * Slot: state Description: State or region
--     * Slot: postal_code Description: Postal code
--     * Slot: Party_id Description: Autocreated FK slot
-- # Class: ResponsibleParty Description: Assignment of parties to a role
--     * Slot: id
--     * Slot: role_id Description: Assigned role identifier
--     * Slot: CSFMetadata_id Description: Autocreated FK slot
-- # Class: BackMatter Description: OSCAL back-matter section containing resource references
--     * Slot: id
-- # Class: Resource Description: Referenced resource in back-matter
--     * Slot: id
--     * Slot: uuid Description: UUID for catalog or resource element
--     * Slot: title Description: Human-readable title
--     * Slot: BackMatter_id Description: Autocreated FK slot
-- # Class: ResourceLink Description: Reference link for a back-matter resource
--     * Slot: id
--     * Slot: href Description: Link or resource reference
--     * Slot: media_type Description: Media type for a resource link
--     * Slot: Resource_id Description: Autocreated FK slot
-- # Class: Party_email_addresses
--     * Slot: Party_id Description: Autocreated FK slot
--     * Slot: email_addresses Description: Party email addresses
-- # Class: Address_addr_lines
--     * Slot: Address_id Description: Autocreated FK slot
--     * Slot: addr_lines Description: Address lines
-- # Class: ResponsibleParty_party_uuids
--     * Slot: ResponsibleParty_id Description: Autocreated FK slot
--     * Slot: party_uuids Description: Referenced party UUIDs

CREATE TABLE "CSFMetadata" (
	id INTEGER NOT NULL,
	title TEXT,
	published TEXT,
	last_modified TEXT,
	version TEXT,
	oscal_version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CSFMetadata_id" ON "CSFMetadata" (id);

CREATE TABLE "CSFElement" (
	uid INTEGER NOT NULL,
	id TEXT,
	class VARCHAR(11),
	title TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_CSFElement_uid" ON "CSFElement" (uid);

CREATE TABLE "BackMatter" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BackMatter_id" ON "BackMatter" (id);

CREATE TABLE "CSFCatalogBody" (
	id INTEGER NOT NULL,
	uuid TEXT,
	metadata_id INTEGER,
	back_matter_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(metadata_id) REFERENCES "CSFMetadata" (id),
	FOREIGN KEY(back_matter_id) REFERENCES "BackMatter" (id)
);
CREATE INDEX "ix_CSFCatalogBody_id" ON "CSFCatalogBody" (id);

CREATE TABLE "Link" (
	id INTEGER NOT NULL,
	href TEXT,
	rel TEXT,
	"CSFMetadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CSFMetadata_id") REFERENCES "CSFMetadata" (id)
);
CREATE INDEX "ix_Link_id" ON "Link" (id);

CREATE TABLE "Role" (
	uid INTEGER NOT NULL,
	id TEXT,
	title TEXT,
	"CSFMetadata_id" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("CSFMetadata_id") REFERENCES "CSFMetadata" (id)
);
CREATE INDEX "ix_Role_uid" ON "Role" (uid);

CREATE TABLE "Party" (
	id INTEGER NOT NULL,
	uuid TEXT,
	type TEXT,
	name TEXT,
	short_name TEXT,
	"CSFMetadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CSFMetadata_id") REFERENCES "CSFMetadata" (id)
);
CREATE INDEX "ix_Party_id" ON "Party" (id);

CREATE TABLE "ResponsibleParty" (
	id INTEGER NOT NULL,
	role_id TEXT,
	"CSFMetadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CSFMetadata_id") REFERENCES "CSFMetadata" (id)
);
CREATE INDEX "ix_ResponsibleParty_id" ON "ResponsibleParty" (id);

CREATE TABLE "Resource" (
	id INTEGER NOT NULL,
	uuid TEXT,
	title TEXT,
	"BackMatter_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BackMatter_id") REFERENCES "BackMatter" (id)
);
CREATE INDEX "ix_Resource_id" ON "Resource" (id);

CREATE TABLE "CSFDocument" (
	id INTEGER NOT NULL,
	catalog_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(catalog_id) REFERENCES "CSFCatalogBody" (id)
);
CREATE INDEX "ix_CSFDocument_id" ON "CSFDocument" (id);

CREATE TABLE "CSFFunction" (
	uid INTEGER NOT NULL,
	id TEXT,
	class VARCHAR(11),
	title TEXT,
	"CSFCatalogBody_id" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("CSFCatalogBody_id") REFERENCES "CSFCatalogBody" (id)
);
CREATE INDEX "ix_CSFFunction_uid" ON "CSFFunction" (uid);

CREATE TABLE "Address" (
	id INTEGER NOT NULL,
	city TEXT,
	state TEXT,
	postal_code TEXT,
	"Party_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id)
);
CREATE INDEX "ix_Address_id" ON "Address" (id);

CREATE TABLE "ResourceLink" (
	id INTEGER NOT NULL,
	href TEXT,
	media_type TEXT,
	"Resource_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Resource_id") REFERENCES "Resource" (id)
);
CREATE INDEX "ix_ResourceLink_id" ON "ResourceLink" (id);

CREATE TABLE "Party_email_addresses" (
	"Party_id" INTEGER,
	email_addresses TEXT,
	PRIMARY KEY ("Party_id", email_addresses),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id)
);
CREATE INDEX "ix_Party_email_addresses_Party_id" ON "Party_email_addresses" ("Party_id");
CREATE INDEX "ix_Party_email_addresses_email_addresses" ON "Party_email_addresses" (email_addresses);

CREATE TABLE "ResponsibleParty_party_uuids" (
	"ResponsibleParty_id" INTEGER,
	party_uuids TEXT,
	PRIMARY KEY ("ResponsibleParty_id", party_uuids),
	FOREIGN KEY("ResponsibleParty_id") REFERENCES "ResponsibleParty" (id)
);
CREATE INDEX "ix_ResponsibleParty_party_uuids_ResponsibleParty_id" ON "ResponsibleParty_party_uuids" ("ResponsibleParty_id");
CREATE INDEX "ix_ResponsibleParty_party_uuids_party_uuids" ON "ResponsibleParty_party_uuids" (party_uuids);

CREATE TABLE "CSFCategory" (
	uid INTEGER NOT NULL,
	id TEXT,
	class VARCHAR(11),
	title TEXT,
	"CSFFunction_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("CSFFunction_uid") REFERENCES "CSFFunction" (uid)
);
CREATE INDEX "ix_CSFCategory_uid" ON "CSFCategory" (uid);

CREATE TABLE "Address_addr_lines" (
	"Address_id" INTEGER,
	addr_lines TEXT,
	PRIMARY KEY ("Address_id", addr_lines),
	FOREIGN KEY("Address_id") REFERENCES "Address" (id)
);
CREATE INDEX "ix_Address_addr_lines_Address_id" ON "Address_addr_lines" ("Address_id");
CREATE INDEX "ix_Address_addr_lines_addr_lines" ON "Address_addr_lines" (addr_lines);

CREATE TABLE "CSFSubcategory" (
	uid INTEGER NOT NULL,
	id TEXT,
	class VARCHAR(11),
	title TEXT,
	"CSFCategory_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("CSFCategory_uid") REFERENCES "CSFCategory" (uid)
);
CREATE INDEX "ix_CSFSubcategory_uid" ON "CSFSubcategory" (uid);

CREATE TABLE "CSFPart" (
	uid INTEGER NOT NULL,
	id TEXT,
	name TEXT,
	ns TEXT,
	prose TEXT,
	"CSFElement_uid" INTEGER,
	"CSFFunction_uid" INTEGER,
	"CSFCategory_uid" INTEGER,
	"CSFSubcategory_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("CSFElement_uid") REFERENCES "CSFElement" (uid),
	FOREIGN KEY("CSFFunction_uid") REFERENCES "CSFFunction" (uid),
	FOREIGN KEY("CSFCategory_uid") REFERENCES "CSFCategory" (uid),
	FOREIGN KEY("CSFSubcategory_uid") REFERENCES "CSFSubcategory" (uid)
);
CREATE INDEX "ix_CSFPart_uid" ON "CSFPart" (uid);

CREATE TABLE "CSFProperty" (
	id INTEGER NOT NULL,
	name TEXT,
	value TEXT,
	ns TEXT,
	remarks TEXT,
	"CSFMetadata_id" INTEGER,
	"CSFElement_uid" INTEGER,
	"CSFFunction_uid" INTEGER,
	"CSFCategory_uid" INTEGER,
	"CSFSubcategory_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CSFMetadata_id") REFERENCES "CSFMetadata" (id),
	FOREIGN KEY("CSFElement_uid") REFERENCES "CSFElement" (uid),
	FOREIGN KEY("CSFFunction_uid") REFERENCES "CSFFunction" (uid),
	FOREIGN KEY("CSFCategory_uid") REFERENCES "CSFCategory" (uid),
	FOREIGN KEY("CSFSubcategory_uid") REFERENCES "CSFSubcategory" (uid)
);
CREATE INDEX "ix_CSFProperty_id" ON "CSFProperty" (id);
