/**
* Allowed class values for CSF catalog elements
*/
export enum CSFElementClassValue {
    
    function = "function",
    category = "category",
    subcategory = "subcategory",
};


/**
 * Root wrapper for CSF catalog content
 */
export interface CSFDocument {
    /** Root catalog payload */
    catalog?: CSFCatalogBody,
}


/**
 * Main CSF catalog object
 */
export interface CSFCatalogBody {
    /** UUID for catalog or resource element */
    uuid?: string,
    /** Catalog metadata */
    metadata?: CSFMetadata,
    /** List of CSF functions (top-level groupings) in the catalog */
    groups?: CSFFunction[],
    /** Back-matter references and resources */
    back_matter?: BackMatter,
}


/**
 * OSCAL metadata section for the CSF catalog
 */
export interface CSFMetadata {
    /** Human-readable title */
    title?: string,
    /** Publication timestamp */
    published?: string,
    /** Last modification timestamp */
    last_modified?: string,
    /** Version identifier */
    version?: string,
    /** OSCAL version identifier */
    oscal_version?: string,
    /** List of properties */
    props?: CSFProperty[],
    /** List of links and relationships */
    links?: Link[],
    /** Roles used in metadata */
    roles?: Role[],
    /** Parties used in metadata */
    parties?: Party[],
    /** Responsible party assignments */
    responsible_parties?: ResponsibleParty[],
}


/**
 * Abstract base class for CSF catalog elements
 */
export interface CSFElement {
    /** Unique identifier for a catalog element */
    id?: string,
    /** Classification of a CSF catalog element (function, category, subcategory) */
    class?: string,
    /** Human-readable title */
    title?: string,
    /** List of properties */
    props?: CSFProperty[],
    /** Structured narrative parts (e.g., statement, overview, example) */
    parts?: CSFPart[],
}


/**
 * A CSF function - top-level grouping (e.g. GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER)
 */
export interface CSFFunction extends CSFElement {
    /** List of categories or subcategories within a function or category */
    controls?: CSFCategory[],
}


/**
 * A CSF category - second-level grouping within a function (e.g. GV.OC Organizational Context, ID.AM Asset Management)
 */
export interface CSFCategory extends CSFElement {
    /** List of categories or subcategories within a function or category */
    controls?: CSFSubcategory[],
}


/**
 * A CSF subcategory - specific cybersecurity outcome (e.g. GV.OC-01, ID.AM-01)
 */
export interface CSFSubcategory extends CSFElement {
}


/**
 * Structured narrative part (statement, overview, or example)
 */
export interface CSFPart {
    /** Unique identifier for a catalog element */
    id?: string,
    /** Name of a property or part */
    name?: string,
    /** Namespace URI for a property or part */
    ns?: string,
    /** Free-text prose content */
    prose?: string,
}


/**
 * A name-value property with optional namespace and supplemental remarks
 */
export interface CSFProperty {
    /** Name of a property or part */
    name?: string,
    /** Property value */
    value?: string,
    /** Namespace URI for a property or part */
    ns?: string,
    /** Supplemental remarks on a property */
    remarks?: string,
}


/**
 * Relationship link with href and optional rel attribute
 */
export interface Link {
    /** Link or resource reference */
    href?: string,
    /** Relationship type for a link */
    rel?: string,
}


/**
 * Role definition used in metadata
 */
export interface Role {
    /** Unique identifier for a catalog element */
    id?: string,
    /** Human-readable title */
    title?: string,
}


/**
 * Party definition (person or organization)
 */
export interface Party {
    /** UUID for catalog or resource element */
    uuid?: string,
    /** Party type (e.g., organization, person) */
    type?: string,
    /** Name of a property or part */
    name?: string,
    /** Short display name for a party */
    short_name?: string,
    /** Party email addresses */
    email_addresses?: string[],
    /** Postal addresses */
    addresses?: Address[],
}


/**
 * Postal address
 */
export interface Address {
    /** Address lines */
    addr_lines?: string[],
    /** City name */
    city?: string,
    /** State or region */
    state?: string,
    /** Postal code */
    postal_code?: string,
}


/**
 * Assignment of parties to a role
 */
export interface ResponsibleParty {
    /** Assigned role identifier */
    role_id?: string,
    /** Referenced party UUIDs */
    party_uuids?: string[],
}


/**
 * OSCAL back-matter section containing resource references
 */
export interface BackMatter {
    /** Back-matter resources */
    resources?: Resource[],
}


/**
 * Referenced resource in back-matter
 */
export interface Resource {
    /** UUID for catalog or resource element */
    uuid?: string,
    /** Human-readable title */
    title?: string,
    /** Resource links */
    rlinks?: ResourceLink[],
}


/**
 * Reference link for a back-matter resource
 */
export interface ResourceLink {
    /** Link or resource reference */
    href?: string,
    /** Media type for a resource link */
    media_type?: string,
}



