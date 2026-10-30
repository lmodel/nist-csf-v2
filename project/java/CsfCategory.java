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
  A group of related cybersecurity outcomes within a function, such as Organizational Context (GV.OC), or a CSF 1.1 category that CSF 2.0 withdrew, which the catalog keeps with its status and, where NIST recorded it, where it moved or what incorporated it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CsfCategory  {

  private String title;
  private String description;
  private String csfCategoryId;
  private List<CsfSubcategory> categorySubcategories;
  private String categoryStatus;
  private List<String> categoryMovedTo;
  private List<String> categoryIncorporatedInto;


}