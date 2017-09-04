
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
 * <p>Original spec-file type: DendrogramOutput</p>
 * <pre>
 * Ouput of the run_dendrogram function
 * result_plots - List of result plot path(s)
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "result_plots"
})
public class DendrogramOutput {

    @JsonProperty("result_plots")
    private List<String> resultPlots;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("result_plots")
    public List<String> getResultPlots() {
        return resultPlots;
    }

    @JsonProperty("result_plots")
    public void setResultPlots(List<String> resultPlots) {
        this.resultPlots = resultPlots;
    }

    public DendrogramOutput withResultPlots(List<String> resultPlots) {
        this.resultPlots = resultPlots;
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
        return ((((("DendrogramOutput"+" [resultPlots=")+ resultPlots)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
