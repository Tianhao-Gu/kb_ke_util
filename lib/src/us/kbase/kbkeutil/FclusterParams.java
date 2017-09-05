
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
 * <p>Original spec-file type: FclusterParams</p>
 * <pre>
 * Input of the run_fcluster function
 * linkage_matrix - hierarchical clustering linkage matrix (refer to run_linkage return)
 * dist_threshold - the threshold to apply when forming flat clusters
 * Optional arguments:
 * labels - items corresponding to each linkage_matrix element 
 *          (If labels are given, result flat_cluster will be mapped to element in labels.)
 * criterion - The criterion to use in forming flat clusters. Default set to 'distance'.
 *             The criterion can be 
 *             ["inconsistent", "distance", "maxclust"]
 *             Note: Advanced criterion 'monocrit', 'maxclust_monocrit' in 
 *             scipy.cluster.hierarchy.fcluster library are not implemented
 *             Details refer to: 
 *             https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "linkage_matrix",
    "dist_threshold",
    "labels",
    "criterion"
})
public class FclusterParams {

    @JsonProperty("linkage_matrix")
    private List<List<String>> linkageMatrix;
    @JsonProperty("dist_threshold")
    private Double distThreshold;
    @JsonProperty("labels")
    private List<String> labels;
    @JsonProperty("criterion")
    private java.lang.String criterion;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("linkage_matrix")
    public List<List<String>> getLinkageMatrix() {
        return linkageMatrix;
    }

    @JsonProperty("linkage_matrix")
    public void setLinkageMatrix(List<List<String>> linkageMatrix) {
        this.linkageMatrix = linkageMatrix;
    }

    public FclusterParams withLinkageMatrix(List<List<String>> linkageMatrix) {
        this.linkageMatrix = linkageMatrix;
        return this;
    }

    @JsonProperty("dist_threshold")
    public Double getDistThreshold() {
        return distThreshold;
    }

    @JsonProperty("dist_threshold")
    public void setDistThreshold(Double distThreshold) {
        this.distThreshold = distThreshold;
    }

    public FclusterParams withDistThreshold(Double distThreshold) {
        this.distThreshold = distThreshold;
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

    public FclusterParams withLabels(List<String> labels) {
        this.labels = labels;
        return this;
    }

    @JsonProperty("criterion")
    public java.lang.String getCriterion() {
        return criterion;
    }

    @JsonProperty("criterion")
    public void setCriterion(java.lang.String criterion) {
        this.criterion = criterion;
    }

    public FclusterParams withCriterion(java.lang.String criterion) {
        this.criterion = criterion;
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
        return ((((((((((("FclusterParams"+" [linkageMatrix=")+ linkageMatrix)+", distThreshold=")+ distThreshold)+", labels=")+ labels)+", criterion=")+ criterion)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
