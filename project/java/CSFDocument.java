package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  Root wrapper for CSF catalog content
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CSFDocument  {

  private CSFCatalogBody catalog;

}