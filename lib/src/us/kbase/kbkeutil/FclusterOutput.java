
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
 * <p>Original spec-file type: FclusterOutput</p>
 * <pre>
 * Ouput of the run_fcluster function
 * flat_cluster - A dictionary of flat clusters.
 *                Each element of flat_cluster representing a cluster contains a label array. 
 *                (If labels is none, element position array is returned to each cluster group)
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "flat_cluster"
})
public class FclusterOutput {

    @JsonProperty("flat_cluster")
    private Map<String, List<String>> flatCluster;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("flat_cluster")
    public Map<String, List<String>> getFlatCluster() {
        return flatCluster;
    }

    @JsonProperty("flat_cluster")
    public void setFlatCluster(Map<String, List<String>> flatCluster) {
        this.flatCluster = flatCluster;
    }

    public FclusterOutput withFlatCluster(Map<String, List<String>> flatCluster) {
        this.flatCluster = flatCluster;
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
        return ((((("FclusterOutput"+" [flatCluster=")+ flatCluster)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
