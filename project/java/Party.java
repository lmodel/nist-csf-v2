package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  Party definition (person or organization)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Party  {

  private String uuid;
  private String type;
  private String name;
  private String short-name;
  private List<String> email-addresses;
  private List<Address> addresses;

}