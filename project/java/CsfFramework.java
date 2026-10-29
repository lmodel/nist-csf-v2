package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  One edition of the CSF as a whole: its functions, each holding its categories and their subcategories.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CsfFramework  {

  private String csfVersion;
  private List<CsfFunction> functions;

}