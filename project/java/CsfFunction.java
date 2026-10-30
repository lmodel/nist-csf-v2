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
  One of the six functions that sort the CSF's outcomes at the highest level: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND and RECOVER. Each is named by two letters and described in a sentence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CsfFunction  {

  private String title;
  private String description;
  private String csfFunctionId;
  private List<CsfCategory> functionCategories;


}