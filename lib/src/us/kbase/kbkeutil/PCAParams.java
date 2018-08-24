
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
 * <p>Original spec-file type: PCAParams</p>
 * <pre>
 * Input of the run_PCA function
 * data_matrix - raw data matrix in json format
 *               e.g.{u'condition_1': {u'gene_1': 0.1, u'gene_2': 0.3, u'gene_3': None},
 *                    u'condition_2': {u'gene_1': 0.2, u'gene_2': 0.4, u'gene_3': None},
 *                    u'condition_3': {u'gene_1': 0.3, u'gene_2': 0.5, u'gene_3': None},
 *                    u'condition_4': {u'gene_1': 0.4, u'gene_2': 0.6, u'gene_3': None}}
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "data_matrix"
})
public class PCAParams {

    @JsonProperty("data_matrix")
    private String dataMatrix;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("data_matrix")
    public String getDataMatrix() {
        return dataMatrix;
    }

    @JsonProperty("data_matrix")
    public void setDataMatrix(String dataMatrix) {
        this.dataMatrix = dataMatrix;
    }

    public PCAParams withDataMatrix(String dataMatrix) {
        this.dataMatrix = dataMatrix;
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
        return ((((("PCAParams"+" [dataMatrix=")+ dataMatrix)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
