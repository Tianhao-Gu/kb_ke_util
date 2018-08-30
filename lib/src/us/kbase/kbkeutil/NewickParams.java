
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
 * <p>Original spec-file type: NewickParams</p>
 * <pre>
 * Input of the linkage_2_newick function
 * linkage_matrix - hierarchical clustering linkage matrix (refer to run_linkage return)
 * labels - items corresponding to each linkage_matrix element 
 *          (If labels are given, result flat_cluster will be mapped to element in labels.)
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "linkage_matrix",
    "labels"
})
public class NewickParams {

    @JsonProperty("linkage_matrix")
    private List<List<Double>> linkageMatrix;
    @JsonProperty("labels")
    private List<String> labels;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("linkage_matrix")
    public List<List<Double>> getLinkageMatrix() {
        return linkageMatrix;
    }

    @JsonProperty("linkage_matrix")
    public void setLinkageMatrix(List<List<Double>> linkageMatrix) {
        this.linkageMatrix = linkageMatrix;
    }

    public NewickParams withLinkageMatrix(List<List<Double>> linkageMatrix) {
        this.linkageMatrix = linkageMatrix;
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

    public NewickParams withLabels(List<String> labels) {
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
        return ((((((("NewickParams"+" [linkageMatrix=")+ linkageMatrix)+", labels=")+ labels)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
