package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  Postal address
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Address  {

  private List<String> addr-lines;
  private String city;
  private String state;
  private String postal-code;

}