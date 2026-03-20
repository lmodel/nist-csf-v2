package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  Relationship link with href and optional rel attribute
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Link  {

  private String href;
  private String rel;

}