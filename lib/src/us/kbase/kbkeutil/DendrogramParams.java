
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
 * <p>Original spec-file type: DendrogramParams</p>
 * <pre>
 * Input of the run_dendrogram function
 * linkage_matrix - hierarchical clustering linkage matrix (refer to run_linkage return)
 * Optional arguments:
 * dist_threshold - the threshold to apply when forming flat clusters (draw a horizontal line to dendrogram)
 * labels - items corresponding to each linkage_matrix element 
 *          (If labels are given, result dendrogram x-axis will be mapped to element in labels.)
 * last_merges - show only last given value merged clusters
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "linkage_matrix",
    "dist_threshold",
    "labels",
    "last_merges"
})
public class DendrogramParams {

    @JsonProperty("linkage_matrix")
    private List<List<String>> linkageMatrix;
    @JsonProperty("dist_threshold")
    private Double distThreshold;
    @JsonProperty("labels")
    private List<String> labels;
    @JsonProperty("last_merges")
    private Long lastMerges;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("linkage_matrix")
    public List<List<String>> getLinkageMatrix() {
        return linkageMatrix;
    }

    @JsonProperty("linkage_matrix")
    public void setLinkageMatrix(List<List<String>> linkageMatrix) {
        this.linkageMatrix = linkageMatrix;
    }

    public DendrogramParams withLinkageMatrix(List<List<String>> linkageMatrix) {
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

    public DendrogramParams withDistThreshold(Double distThreshold) {
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

    public DendrogramParams withLabels(List<String> labels) {
        this.labels = labels;
        return this;
    }

    @JsonProperty("last_merges")
    public Long getLastMerges() {
        return lastMerges;
    }

    @JsonProperty("last_merges")
    public void setLastMerges(Long lastMerges) {
        this.lastMerges = lastMerges;
    }

    public DendrogramParams withLastMerges(Long lastMerges) {
        this.lastMerges = lastMerges;
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
        return ((((((((((("DendrogramParams"+" [linkageMatrix=")+ linkageMatrix)+", distThreshold=")+ distThreshold)+", labels=")+ labels)+", lastMerges=")+ lastMerges)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
