
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
 * <p>Original spec-file type: KmeansParams</p>
 * <pre>
 * Input of the run_kmeans2 function
 * dist_matrix - a condensed distance matrix (refer to run_pdist return)
 * k_num: number of clusters to form
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "dist_matrix",
    "k_num"
})
public class KmeansParams {

    @JsonProperty("dist_matrix")
    private List<Double> distMatrix;
    @JsonProperty("k_num")
    private Long kNum;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("dist_matrix")
    public List<Double> getDistMatrix() {
        return distMatrix;
    }

    @JsonProperty("dist_matrix")
    public void setDistMatrix(List<Double> distMatrix) {
        this.distMatrix = distMatrix;
    }

    public KmeansParams withDistMatrix(List<Double> distMatrix) {
        this.distMatrix = distMatrix;
        return this;
    }

    @JsonProperty("k_num")
    public Long getKNum() {
        return kNum;
    }

    @JsonProperty("k_num")
    public void setKNum(Long kNum) {
        this.kNum = kNum;
    }

    public KmeansParams withKNum(Long kNum) {
        this.kNum = kNum;
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
        return ((((((("KmeansParams"+" [distMatrix=")+ distMatrix)+", kNum=")+ kNum)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
