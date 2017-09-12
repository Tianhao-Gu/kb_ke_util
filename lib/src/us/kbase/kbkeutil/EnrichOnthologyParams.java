
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
 * <p>Original spec-file type: EnrichOnthologyParams</p>
 * <pre>
 * Input of the enrich_onthology function
 * sample_set_shock_id: shock node id where the zipped JSON biclustering info output is stored
 *                      JSON format: ["gene_id_1", "gene_id_2", "gene_id_3"]
 * entity_term_set: entity terms dict structure where global GO term and gene_ids are stored
 *                  e.g. {'gene_id_1': ['go_term_1', 'go_term_2']}
 * Optional arguments:
 * propagation: includes is_a relationship to all go terms (default is 0)
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "sample_set_shock_id",
    "entity_term_set",
    "propagation"
})
public class EnrichOnthologyParams {

    @JsonProperty("sample_set_shock_id")
    private java.lang.String sampleSetShockId;
    @JsonProperty("entity_term_set")
    private Map<String, List<String>> entityTermSet;
    @JsonProperty("propagation")
    private Long propagation;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("sample_set_shock_id")
    public java.lang.String getSampleSetShockId() {
        return sampleSetShockId;
    }

    @JsonProperty("sample_set_shock_id")
    public void setSampleSetShockId(java.lang.String sampleSetShockId) {
        this.sampleSetShockId = sampleSetShockId;
    }

    public EnrichOnthologyParams withSampleSetShockId(java.lang.String sampleSetShockId) {
        this.sampleSetShockId = sampleSetShockId;
        return this;
    }

    @JsonProperty("entity_term_set")
    public Map<String, List<String>> getEntityTermSet() {
        return entityTermSet;
    }

    @JsonProperty("entity_term_set")
    public void setEntityTermSet(Map<String, List<String>> entityTermSet) {
        this.entityTermSet = entityTermSet;
    }

    public EnrichOnthologyParams withEntityTermSet(Map<String, List<String>> entityTermSet) {
        this.entityTermSet = entityTermSet;
        return this;
    }

    @JsonProperty("propagation")
    public Long getPropagation() {
        return propagation;
    }

    @JsonProperty("propagation")
    public void setPropagation(Long propagation) {
        this.propagation = propagation;
    }

    public EnrichOnthologyParams withPropagation(Long propagation) {
        this.propagation = propagation;
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
        return ((((((((("EnrichOnthologyParams"+" [sampleSetShockId=")+ sampleSetShockId)+", entityTermSet=")+ entityTermSet)+", propagation=")+ propagation)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
