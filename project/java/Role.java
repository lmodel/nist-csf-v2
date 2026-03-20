package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  Role definition used in metadata
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Role  {

  private String id;
  private String title;

}