
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
 * <p>Original spec-file type: PdistParams</p>
 * <pre>
 * Input of the run_pdist function
 * data_matrix - raw data matrix with row_ids, col_ids and values
 *               e.g.{'row_ids': ['gene_1', 'gene_2'], 
 *                    'col_ids': ['condition_1', 'condition_2'],
 *                    'values': [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]}
 * Optional arguments:
 * metric - The distance metric to use. Default set to 'euclidean'.
 *          The distance function can be 
 *          ["braycurtis", "canberra", "chebyshev", "cityblock", "correlation", "cosine", 
 *           "dice", "euclidean", "hamming", "jaccard", "kulsinski", "matching", 
 *           "rogerstanimoto", "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean", 
 *           "yule"]
 *           Details refer to: 
 *           https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html
 * Note: Advanced metric functions 'minkowski', 'seuclidean' and 'mahalanobis' included in 
 *       scipy.spatial.distance.pdist library are not implemented
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "data_matrix",
    "metric"
})
public class PdistParams {

    @JsonProperty("data_matrix")
    private Map<String, List<String>> dataMatrix;
    @JsonProperty("metric")
    private java.lang.String metric;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("data_matrix")
    public Map<String, List<String>> getDataMatrix() {
        return dataMatrix;
    }

    @JsonProperty("data_matrix")
    public void setDataMatrix(Map<String, List<String>> dataMatrix) {
        this.dataMatrix = dataMatrix;
    }

    public PdistParams withDataMatrix(Map<String, List<String>> dataMatrix) {
        this.dataMatrix = dataMatrix;
        return this;
    }

    @JsonProperty("metric")
    public java.lang.String getMetric() {
        return metric;
    }

    @JsonProperty("metric")
    public void setMetric(java.lang.String metric) {
        this.metric = metric;
    }

    public PdistParams withMetric(java.lang.String metric) {
        this.metric = metric;
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
        return ((((((("PdistParams"+" [dataMatrix=")+ dataMatrix)+", metric=")+ metric)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
