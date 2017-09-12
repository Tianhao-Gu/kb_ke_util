
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
 * <p>Original spec-file type: EnrichOnthologyOutput</p>
 * <pre>
 * Ouput of the enrich_onthology function
 * enrichment_profile_shock_id: shock node where the zipped JSON enrichment info output is stored
 * JSON format:
 * {"go_term_1": {"sample_count": 10,
 *                "total_count": 20,
 *                "p_value": 0.1,
 *                "ontology_type": "P"}}
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "enrichment_profile_shock_id"
})
public class EnrichOnthologyOutput {

    @JsonProperty("enrichment_profile_shock_id")
    private String enrichmentProfileShockId;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("enrichment_profile_shock_id")
    public String getEnrichmentProfileShockId() {
        return enrichmentProfileShockId;
    }

    @JsonProperty("enrichment_profile_shock_id")
    public void setEnrichmentProfileShockId(String enrichmentProfileShockId) {
        this.enrichmentProfileShockId = enrichmentProfileShockId;
    }

    public EnrichOnthologyOutput withEnrichmentProfileShockId(String enrichmentProfileShockId) {
        this.enrichmentProfileShockId = enrichmentProfileShockId;
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
        return ((((("EnrichOnthologyOutput"+" [enrichmentProfileShockId=")+ enrichmentProfileShockId)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
