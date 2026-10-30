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
  One edition of the CSF as a whole: its functions, each holding its categories and their subcategories.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CsfFramework  {

  private String csfVersion;
  private List<CsfFunction> csfFunctions;


}