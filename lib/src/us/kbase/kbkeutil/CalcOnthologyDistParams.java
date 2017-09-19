
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
 * <p>Original spec-file type: CalcOnthologyDistParams</p>
 * <pre>
 * Input of the calc_onthology_dist function
 * onthology_set: dict structure stores mapping of gene_id to paried onthology
 *                e.g. {"gene_id_1": ["go_term_1", "go_term_2"]}
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "onthology_set"
})
public class CalcOnthologyDistParams {

    @JsonProperty("onthology_set")
    private Map<String, List<String>> onthologySet;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("onthology_set")
    public Map<String, List<String>> getOnthologySet() {
        return onthologySet;
    }

    @JsonProperty("onthology_set")
    public void setOnthologySet(Map<String, List<String>> onthologySet) {
        this.onthologySet = onthologySet;
    }

    public CalcOnthologyDistParams withOnthologySet(Map<String, List<String>> onthologySet) {
        this.onthologySet = onthologySet;
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
        return ((((("CalcOnthologyDistParams"+" [onthologySet=")+ onthologySet)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
