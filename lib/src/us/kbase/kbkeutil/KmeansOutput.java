
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
 * <p>Original spec-file type: KmeansOutput</p>
 * <pre>
 * Ouput of the run_kmeans2 function
 * centroid - centroids found at the last iteration of k-means
 * idx - index of the centroid
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "centroid",
    "idx"
})
public class KmeansOutput {

    @JsonProperty("centroid")
    private List<Double> centroid;
    @JsonProperty("idx")
    private List<Long> idx;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("centroid")
    public List<Double> getCentroid() {
        return centroid;
    }

    @JsonProperty("centroid")
    public void setCentroid(List<Double> centroid) {
        this.centroid = centroid;
    }

    public KmeansOutput withCentroid(List<Double> centroid) {
        this.centroid = centroid;
        return this;
    }

    @JsonProperty("idx")
    public List<Long> getIdx() {
        return idx;
    }

    @JsonProperty("idx")
    public void setIdx(List<Long> idx) {
        this.idx = idx;
    }

    public KmeansOutput withIdx(List<Long> idx) {
        this.idx = idx;
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
        return ((((((("KmeansOutput"+" [centroid=")+ centroid)+", idx=")+ idx)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
