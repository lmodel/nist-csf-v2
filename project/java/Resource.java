package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  Referenced resource in back-matter
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Resource  {

  private String uuid;
  private String title;
  private List<ResourceLink> rlinks;

}