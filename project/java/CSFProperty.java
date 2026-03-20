package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  A name-value property with optional namespace and supplemental remarks
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CSFProperty  {

  private String name;
  private String value;
  private String ns;
  private String remarks;

}