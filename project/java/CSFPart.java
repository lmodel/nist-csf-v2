package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  Structured narrative part (statement, overview, or example)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CSFPart  {

  private String id;
  private String name;
  private String ns;
  private String prose;

}