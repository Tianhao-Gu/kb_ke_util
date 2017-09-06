
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
 * square_dist_matrix - square form of distance matrix (refer to run_pdist return)
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
    "square_dist_matrix",
    "method"
})
public class LinkageParams {

    @JsonProperty("square_dist_matrix")
    private List<List<String>> squareDistMatrix;
    @JsonProperty("method")
    private java.lang.String method;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("square_dist_matrix")
    public List<List<String>> getSquareDistMatrix() {
        return squareDistMatrix;
    }

    @JsonProperty("square_dist_matrix")
    public void setSquareDistMatrix(List<List<String>> squareDistMatrix) {
        this.squareDistMatrix = squareDistMatrix;
    }

    public LinkageParams withSquareDistMatrix(List<List<String>> squareDistMatrix) {
        this.squareDistMatrix = squareDistMatrix;
        return this;
    }

    @JsonProperty("method")
    public java.lang.String getMethod() {
        return method;
    }

    @JsonProperty("method")
    public void setMethod(java.lang.String method) {
        this.method = method;
    }

    public LinkageParams withMethod(java.lang.String method) {
        this.method = method;
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
        return ((((((("LinkageParams"+" [squareDistMatrix=")+ squareDistMatrix)+", method=")+ method)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
