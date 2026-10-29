package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
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
  private String functionId;
  private List<CsfCategory> functionCategories;

}