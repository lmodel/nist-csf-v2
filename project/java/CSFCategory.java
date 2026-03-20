package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  A CSF category - second-level grouping within a function (e.g. GV.OC Organizational Context, ID.AM Asset Management)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CSFCategory extends CSFElement {

  private List<CSFSubcategory> controls;

}