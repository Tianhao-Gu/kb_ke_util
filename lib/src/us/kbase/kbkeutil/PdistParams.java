
package us.kbase.kbkeutil;

import java.util.HashMap;
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
 * data_matrix - raw data matrix in json format
 *                   e.g.{u'condition_1': {u'gene_1': 0.1, u'gene_2': 0.3, u'gene_3': None},
 *                        u'condition_2': {u'gene_1': 0.2, u'gene_2': 0.4, u'gene_3': None},
 *                        u'condition_3': {u'gene_1': 0.3, u'gene_2': 0.5, u'gene_3': None},
 *                        u'condition_4': {u'gene_1': 0.4, u'gene_2': 0.6, u'gene_3': None}}
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
    private String dataMatrix;
    @JsonProperty("metric")
    private String metric;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("data_matrix")
    public String getDataMatrix() {
        return dataMatrix;
    }

    @JsonProperty("data_matrix")
    public void setDataMatrix(String dataMatrix) {
        this.dataMatrix = dataMatrix;
    }

    public PdistParams withDataMatrix(String dataMatrix) {
        this.dataMatrix = dataMatrix;
        return this;
    }

    @JsonProperty("metric")
    public String getMetric() {
        return metric;
    }

    @JsonProperty("metric")
    public void setMetric(String metric) {
        this.metric = metric;
    }

    public PdistParams withMetric(String metric) {
        this.metric = metric;
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
        return ((((((("PdistParams"+" [dataMatrix=")+ dataMatrix)+", metric=")+ metric)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
