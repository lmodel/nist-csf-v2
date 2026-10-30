package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  A cybersecurity outcome: one statement of a result within a category, such as GV.OC-01, or a CSF 1.1 subcategory that CSF 2.0 withdrew, which the catalog keeps with its statement, its status and where it moved or what incorporated it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CsfSubcategory  {

  private String description;
  private String csfSubcategoryId;
  private List<CsfImplementationExample> subcategoryExamples;
  private String subcategoryStatus;
  private List<String> subcategoryMovedTo;
  private List<String> subcategoryIncorporatedInto;

}