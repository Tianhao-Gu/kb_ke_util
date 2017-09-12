
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
 * shock_id_list: list of the id of the shock node where the zipped JSON biclustering info output is stored
 * JSON format:
 * ["gene_id_1", "gene_id_2", "gene_id_3"]
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "shock_id_list"
})
public class BuildBiclustersOutput {

    @JsonProperty("shock_id_list")
    private List<String> shockIdList;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("shock_id_list")
    public List<String> getShockIdList() {
        return shockIdList;
    }

    @JsonProperty("shock_id_list")
    public void setShockIdList(List<String> shockIdList) {
        this.shockIdList = shockIdList;
    }

    public BuildBiclustersOutput withShockIdList(List<String> shockIdList) {
        this.shockIdList = shockIdList;
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
        return ((((("BuildBiclustersOutput"+" [shockIdList=")+ shockIdList)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
