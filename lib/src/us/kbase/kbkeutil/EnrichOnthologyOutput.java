
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
 * enrichment_profile: dict structure stores enrichment info
 *                     e.g. {"go_term_1": {"sample_count": 10,
 *                                         "total_count": 20,
 *                                         "p_value": 0.1,
 *                                         "ontology_type": "P"}}
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "enrichment_profile"
})
public class EnrichOnthologyOutput {

    @JsonProperty("enrichment_profile")
    private Map<String, TermEnrichment> enrichmentProfile;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("enrichment_profile")
    public Map<String, TermEnrichment> getEnrichmentProfile() {
        return enrichmentProfile;
    }

    @JsonProperty("enrichment_profile")
    public void setEnrichmentProfile(Map<String, TermEnrichment> enrichmentProfile) {
        this.enrichmentProfile = enrichmentProfile;
    }

    public EnrichOnthologyOutput withEnrichmentProfile(Map<String, TermEnrichment> enrichmentProfile) {
        this.enrichmentProfile = enrichmentProfile;
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
        return ((((("EnrichOnthologyOutput"+" [enrichmentProfile=")+ enrichmentProfile)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
