package None;

/* metamodel_version: 1.7.0 */
/* version: 2.0.0 */
import java.util.List;
import lombok.*;

/**
  OSCAL metadata section for the CSF catalog
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CSFMetadata  {

  private String title;
  private String published;
  private String last-modified;
  private String version;
  private String oscal-version;
  private List<CSFProperty> props;
  private List<Link> links;
  private List<Role> roles;
  private List<Party> parties;
  private List<ResponsibleParty> responsible-parties;

}