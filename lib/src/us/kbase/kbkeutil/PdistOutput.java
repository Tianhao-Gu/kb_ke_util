
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
 * square_dist_matrix - square form of distance matrix where the data is mirrored across 
 *                      the diagonal
 * labels - item name corresponding to each square_dist_matrix element
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "square_dist_matrix",
    "labels"
})
public class PdistOutput {

    @JsonProperty("square_dist_matrix")
    private List<List<String>> squareDistMatrix;
    @JsonProperty("labels")
    private List<String> labels;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("square_dist_matrix")
    public List<List<String>> getSquareDistMatrix() {
        return squareDistMatrix;
    }

    @JsonProperty("square_dist_matrix")
    public void setSquareDistMatrix(List<List<String>> squareDistMatrix) {
        this.squareDistMatrix = squareDistMatrix;
    }

    public PdistOutput withSquareDistMatrix(List<List<String>> squareDistMatrix) {
        this.squareDistMatrix = squareDistMatrix;
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
        return ((((((("PdistOutput"+" [squareDistMatrix=")+ squareDistMatrix)+", labels=")+ labels)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
