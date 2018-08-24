
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
 * <p>Original spec-file type: PCAOutput</p>
 * <pre>
 * Ouput of the run_PCA function
 * PCA_matrix - PCA matrix in json format
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "PCA_matrix"
})
public class PCAOutput {

    @JsonProperty("PCA_matrix")
    private String PCAMatrix;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("PCA_matrix")
    public String getPCAMatrix() {
        return PCAMatrix;
    }

    @JsonProperty("PCA_matrix")
    public void setPCAMatrix(String PCAMatrix) {
        this.PCAMatrix = PCAMatrix;
    }

    public PCAOutput withPCAMatrix(String PCAMatrix) {
        this.PCAMatrix = PCAMatrix;
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
        return ((((("PCAOutput"+" [PCAMatrix=")+ PCAMatrix)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
