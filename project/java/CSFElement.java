package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  Abstract base class for CSF catalog elements
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CSFElement  {

  private String id;
  private String class;
  private String title;
  private List<CSFProperty> props;
  private List<CSFPart> parts;

}