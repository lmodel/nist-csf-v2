package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  Main CSF catalog object
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CSFCatalogBody  {

  private String uuid;
  private CSFMetadata metadata;
  private List<CSFFunction> groups;
  private BackMatter back-matter;

}