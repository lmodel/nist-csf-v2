package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  A CSF function - top-level grouping (e.g. GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CSFFunction extends CSFElement {

  private List<CSFCategory> controls;

}