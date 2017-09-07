
package us.kbase.kbkeutil;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: LinkageOutput</p>
 * <pre>
 * Ouput of the run_linkage function
 * linkage_matrix - The hierarchical clustering encoded as a linkage matrix
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "linkage_matrix"
})
public class LinkageOutput {

    @JsonProperty("linkage_matrix")
    private List<List<Double>> linkageMatrix;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("linkage_matrix")
    public List<List<Double>> getLinkageMatrix() {
        return linkageMatrix;
    }

    @JsonProperty("linkage_matrix")
    public void setLinkageMatrix(List<List<Double>> linkageMatrix) {
        this.linkageMatrix = linkageMatrix;
    }

    public LinkageOutput withLinkageMatrix(List<List<Double>> linkageMatrix) {
        this.linkageMatrix = linkageMatrix;
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
        return ((((("LinkageOutput"+" [linkageMatrix=")+ linkageMatrix)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
