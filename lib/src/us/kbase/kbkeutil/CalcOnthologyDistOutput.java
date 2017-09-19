
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
 * <p>Original spec-file type: CalcOnthologyDistOutput</p>
 * <pre>
 * Ouput of the calc_onthology_dist function
 * onthology_dist_set: dict structure stores mapping of gene_id to dist
 *                     e.g. {"gene_id_1": 3}
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "onthology_dist_set"
})
public class CalcOnthologyDistOutput {

    @JsonProperty("onthology_dist_set")
    private Map<String, Long> onthologyDistSet;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("onthology_dist_set")
    public Map<String, Long> getOnthologyDistSet() {
        return onthologyDistSet;
    }

    @JsonProperty("onthology_dist_set")
    public void setOnthologyDistSet(Map<String, Long> onthologyDistSet) {
        this.onthologyDistSet = onthologyDistSet;
    }

    public CalcOnthologyDistOutput withOnthologyDistSet(Map<String, Long> onthologyDistSet) {
        this.onthologyDistSet = onthologyDistSet;
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
        return ((((("CalcOnthologyDistOutput"+" [onthologyDistSet=")+ onthologyDistSet)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
