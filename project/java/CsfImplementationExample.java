package example;

/* metamodel_version: 1.12.0 */
/* version: 2.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An implementation example: one concise, action-oriented step that could help achieve a subcategory's outcome. NIST publishes the examples beside the Core, in its reference tool and its catalog, not in CSWP 29 itself.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CsfImplementationExample  {

  private String csfImplementationExampleId;
  private String description;


}