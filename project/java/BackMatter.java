package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  OSCAL back-matter section containing resource references
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BackMatter  {

  private List<Resource> resources;

}