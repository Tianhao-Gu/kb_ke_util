
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
 * <p>Original spec-file type: BuildBiclustersOutput</p>
 * <pre>
 * Ouput of the build_biclusters function
 * biclusters: list of biclusters
 *             e.g. [["gene_id_1", "gene_id_2"], ["gene_id_3"]]
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "biclusters"
})
public class BuildBiclustersOutput {

    @JsonProperty("biclusters")
    private List<List<String>> biclusters;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("biclusters")
    public List<List<String>> getBiclusters() {
        return biclusters;
    }

    @JsonProperty("biclusters")
    public void setBiclusters(List<List<String>> biclusters) {
        this.biclusters = biclusters;
    }

    public BuildBiclustersOutput withBiclusters(List<List<String>> biclusters) {
        this.biclusters = biclusters;
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
        return ((((("BuildBiclustersOutput"+" [biclusters=")+ biclusters)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
