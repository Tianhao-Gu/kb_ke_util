
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
 * <p>Original spec-file type: LinkageParams</p>
 * <pre>
 * Input of the run_linkage function
 * dist_matrix - 1D distance matrix (refer to run_pdist return)
 * Optional arguments:
 * method - The linkage algorithm to use. Default set to 'ward'.
 *          The method can be 
 *          ["single", "complete", "average", "weighted", "centroid", "median", "ward"]
 *          Details refer to: 
 *          https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "dist_matrix",
    "method"
})
public class LinkageParams {

    @JsonProperty("dist_matrix")
    private List<Double> distMatrix;
    @JsonProperty("method")
    private String method;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("dist_matrix")
    public List<Double> getDistMatrix() {
        return distMatrix;
    }

    @JsonProperty("dist_matrix")
    public void setDistMatrix(List<Double> distMatrix) {
        this.distMatrix = distMatrix;
    }

    public LinkageParams withDistMatrix(List<Double> distMatrix) {
        this.distMatrix = distMatrix;
        return this;
    }

    @JsonProperty("method")
    public String getMethod() {
        return method;
    }

    @JsonProperty("method")
    public void setMethod(String method) {
        this.method = method;
    }

    public LinkageParams withMethod(String method) {
        this.method = method;
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
        return ((((((("LinkageParams"+" [distMatrix=")+ distMatrix)+", method=")+ method)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
