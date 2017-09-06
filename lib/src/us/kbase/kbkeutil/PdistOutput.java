
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
 * <p>Original spec-file type: PdistOutput</p>
 * <pre>
 * Ouput of the run_pdist function
 * dist_matrix - distance matrix where the data is mirrored across the diagonal
 * labels - item name corresponding to each dist_matrix element
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "dist_matrix",
    "labels"
})
public class PdistOutput {

    @JsonProperty("dist_matrix")
    private List<List<String>> distMatrix;
    @JsonProperty("labels")
    private List<String> labels;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("dist_matrix")
    public List<List<String>> getDistMatrix() {
        return distMatrix;
    }

    @JsonProperty("dist_matrix")
    public void setDistMatrix(List<List<String>> distMatrix) {
        this.distMatrix = distMatrix;
    }

    public PdistOutput withDistMatrix(List<List<String>> distMatrix) {
        this.distMatrix = distMatrix;
        return this;
    }

    @JsonProperty("labels")
    public List<String> getLabels() {
        return labels;
    }

    @JsonProperty("labels")
    public void setLabels(List<String> labels) {
        this.labels = labels;
    }

    public PdistOutput withLabels(List<String> labels) {
        this.labels = labels;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((("PdistOutput"+" [distMatrix=")+ distMatrix)+", labels=")+ labels)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
