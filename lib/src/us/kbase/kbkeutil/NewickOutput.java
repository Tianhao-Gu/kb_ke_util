
package us.kbase.kbkeutil;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: NewickOutput</p>
 * <pre>
 * Ouput of the linkage_2_newick function
 * newick - newick representation of tree
 *          https://en.wikipedia.org/wiki/Newick_format
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "newick"
})
public class NewickOutput {

    @JsonProperty("newick")
    private String newick;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("newick")
    public String getNewick() {
        return newick;
    }

    @JsonProperty("newick")
    public void setNewick(String newick) {
        this.newick = newick;
    }

    public NewickOutput withNewick(String newick) {
        this.newick = newick;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((("NewickOutput"+" [newick=")+ newick)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
