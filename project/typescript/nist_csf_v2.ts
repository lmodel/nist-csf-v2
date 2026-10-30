/**
* The state the catalog gives a category or subcategory that CSF 2.0 no longer carries. A category or subcategory of CSF 2.0 has no status.
*/
export enum CsfElementStatus {
    
    /** The element was in CSF 1.1 and CSF 2.0 withdrew it. The catalog keeps it, and names where it moved or what incorporated it where NIST recorded that. */
    withdrawn = "withdrawn",
};


/**
 * One edition of the CSF as a whole: its functions, each holding its categories and their subcategories.
 */
export interface CsfFramework {
    /** The CSF edition, as NIST numbers it in the publication's title, such as 2.0. */
    csf_version: string,
    /** The six functions, in the order CSWP 29 gives them. */
    csf_functions: CsfFunction[],
}


/**
 * One of the six functions that sort the CSF's outcomes at the highest level: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND and RECOVER. Each is named by two letters and described in a sentence.
 */
export interface CsfFunction {
    /** The name CSWP 29 gives the function or category. */
    title: string,
    /** What the function, category, subcategory or example says, in the words of whoever records it. */
    description?: string,
    /** The function's two letters, such as GV for GOVERN. */
    csf_function_id: string,
    /** The categories of the function. A knowledge bundle relates a category to its function with isPartOf instead. */
    function_categories?: CsfCategory[],
}


/**
 * A group of related cybersecurity outcomes within a function, such as Organizational Context (GV.OC), or a CSF 1.1 category that CSF 2.0 withdrew, which the catalog keeps with its status and, where NIST recorded it, where it moved or what incorporated it.
 */
export interface CsfCategory {
    /** The name CSWP 29 gives the function or category. */
    title: string,
    /** What the function, category, subcategory or example says, in the words of whoever records it. */
    description?: string,
    /** The category's identifier, such as GV.OC. */
    csf_category_id: string,
    /** The subcategories of the category. A knowledge bundle relates a subcategory to its category with isPartOf instead. */
    category_subcategories?: CsfSubcategory[],
    /** withdrawn for a CSF 1.1 category that CSF 2.0 withdrew. A category of CSF 2.0 has no status. */
    category_status?: string,
    /** The CSF 2.0 category a withdrawn category moved to, as the catalog states it, such as PR.AA for PR.AC. */
    category_moved_to?: string[],
    /** The function, category or subcategory of CSF 2.0 that took in a withdrawn category's outcomes, as the catalog states it, such as GV.OC for ID.BE. The catalog names none for some withdrawn categories. */
    category_incorporated_into?: string[],
}


/**
 * A cybersecurity outcome: one statement of a result within a category, such as GV.OC-01, or a CSF 1.1 subcategory that CSF 2.0 withdrew, which the catalog keeps with its statement, its status and where it moved or what incorporated it.
 */
export interface CsfSubcategory {
    /** What the function, category, subcategory or example says, in the words of whoever records it. */
    description: string,
    /** The subcategory's identifier, such as GV.OC-01. */
    csf_subcategory_id: string,
    /** The implementation examples NIST publishes for the subcategory. CSWP 29 says they are notional, that none is required, and that they are not a complete list of what could be done. */
    subcategory_examples?: CsfImplementationExample[],
    /** withdrawn for a CSF 1.1 subcategory that CSF 2.0 withdrew. A subcategory of CSF 2.0 has no status. */
    subcategory_status?: string,
    /** The CSF 2.0 subcategory a withdrawn subcategory moved to, as the catalog states it, such as GV.OC-03 for ID.GV-03. The catalog names two for a few. */
    subcategory_moved_to?: string[],
    /** The CSF 2.0 category or subcategory that took in a withdrawn subcategory's outcome, as the catalog states it, such as GV.OC-01 for ID.BE-02. */
    subcategory_incorporated_into?: string[],
}


/**
 * An implementation example: one concise, action-oriented step that could help achieve a subcategory's outcome. NIST publishes the examples beside the Core, in its reference tool and its catalog, not in CSWP 29 itself.
 */
export interface CsfImplementationExample {
    /** What the function, category, subcategory or example says, in the words of whoever records it. */
    description: string,
    /** The example's identifier in NIST's reference data, such as GV.OC-01.001 for the first example of subcategory GV.OC-01. */
    csf_implementation_example_id: string,
}



