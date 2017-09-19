package us.kbase.kbkeutil;

import com.fasterxml.jackson.core.type.TypeReference;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import us.kbase.auth.AuthToken;
import us.kbase.common.service.JsonClientCaller;
import us.kbase.common.service.JsonClientException;
import us.kbase.common.service.RpcContext;
import us.kbase.common.service.UnauthorizedException;

/**
 * <p>Original spec-file module name: kb_ke_util</p>
 * <pre>
 * A KBase module: kb_ke_util
 * </pre>
 */
public class KbKeUtilClient {
    private JsonClientCaller caller;
    private String serviceVersion = null;


    /** Constructs a client with a custom URL and no user credentials.
     * @param url the URL of the service.
     */
    public KbKeUtilClient(URL url) {
        caller = new JsonClientCaller(url);
    }
    /** Constructs a client with a custom URL.
     * @param url the URL of the service.
     * @param token the user's authorization token.
     * @throws UnauthorizedException if the token is not valid.
     * @throws IOException if an IOException occurs when checking the token's
     * validity.
     */
    public KbKeUtilClient(URL url, AuthToken token) throws UnauthorizedException, IOException {
        caller = new JsonClientCaller(url, token);
    }

    /** Constructs a client with a custom URL.
     * @param url the URL of the service.
     * @param user the user name.
     * @param password the password for the user name.
     * @throws UnauthorizedException if the credentials are not valid.
     * @throws IOException if an IOException occurs when checking the user's
     * credentials.
     */
    public KbKeUtilClient(URL url, String user, String password) throws UnauthorizedException, IOException {
        caller = new JsonClientCaller(url, user, password);
    }

    /** Constructs a client with a custom URL
     * and a custom authorization service URL.
     * @param url the URL of the service.
     * @param user the user name.
     * @param password the password for the user name.
     * @param auth the URL of the authorization server.
     * @throws UnauthorizedException if the credentials are not valid.
     * @throws IOException if an IOException occurs when checking the user's
     * credentials.
     */
    public KbKeUtilClient(URL url, String user, String password, URL auth) throws UnauthorizedException, IOException {
        caller = new JsonClientCaller(url, user, password, auth);
    }

    /** Get the token this client uses to communicate with the server.
     * @return the authorization token.
     */
    public AuthToken getToken() {
        return caller.getToken();
    }

    /** Get the URL of the service with which this client communicates.
     * @return the service URL.
     */
    public URL getURL() {
        return caller.getURL();
    }

    /** Set the timeout between establishing a connection to a server and
     * receiving a response. A value of zero or null implies no timeout.
     * @param milliseconds the milliseconds to wait before timing out when
     * attempting to read from a server.
     */
    public void setConnectionReadTimeOut(Integer milliseconds) {
        this.caller.setConnectionReadTimeOut(milliseconds);
    }

    /** Check if this client allows insecure http (vs https) connections.
     * @return true if insecure connections are allowed.
     */
    public boolean isInsecureHttpConnectionAllowed() {
        return caller.isInsecureHttpConnectionAllowed();
    }

    /** Deprecated. Use isInsecureHttpConnectionAllowed().
     * @deprecated
     */
    public boolean isAuthAllowedForHttp() {
        return caller.isAuthAllowedForHttp();
    }

    /** Set whether insecure http (vs https) connections should be allowed by
     * this client.
     * @param allowed true to allow insecure connections. Default false
     */
    public void setIsInsecureHttpConnectionAllowed(boolean allowed) {
        caller.setInsecureHttpConnectionAllowed(allowed);
    }

    /** Deprecated. Use setIsInsecureHttpConnectionAllowed().
     * @deprecated
     */
    public void setAuthAllowedForHttp(boolean isAuthAllowedForHttp) {
        caller.setAuthAllowedForHttp(isAuthAllowedForHttp);
    }

    /** Set whether all SSL certificates, including self-signed certificates,
     * should be trusted.
     * @param trustAll true to trust all certificates. Default false.
     */
    public void setAllSSLCertificatesTrusted(final boolean trustAll) {
        caller.setAllSSLCertificatesTrusted(trustAll);
    }
    
    /** Check if this client trusts all SSL certificates, including
     * self-signed certificates.
     * @return true if all certificates are trusted.
     */
    public boolean isAllSSLCertificatesTrusted() {
        return caller.isAllSSLCertificatesTrusted();
    }
    /** Sets streaming mode on. In this case, the data will be streamed to
     * the server in chunks as it is read from disk rather than buffered in
     * memory. Many servers are not compatible with this feature.
     * @param streamRequest true to set streaming mode on, false otherwise.
     */
    public void setStreamingModeOn(boolean streamRequest) {
        caller.setStreamingModeOn(streamRequest);
    }

    /** Returns true if streaming mode is on.
     * @return true if streaming mode is on.
     */
    public boolean isStreamingModeOn() {
        return caller.isStreamingModeOn();
    }

    public void _setFileForNextRpcResponse(File f) {
        caller.setFileForNextRpcResponse(f);
    }

    public String getServiceVersion() {
        return this.serviceVersion;
    }

    public void setServiceVersion(String newValue) {
        this.serviceVersion = newValue;
    }

    /**
     * <p>Original spec-file function name: run_pdist</p>
     * <pre>
     * run_pdist: a wrapper method for scipy.spatial.distance.pdist
     * reference: 
     * https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html
     * </pre>
     * @param   params   instance of type {@link us.kbase.kbkeutil.PdistParams PdistParams}
     * @return   parameter "returnVal" of type {@link us.kbase.kbkeutil.PdistOutput PdistOutput}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public PdistOutput runPdist(PdistParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<PdistOutput>> retType = new TypeReference<List<PdistOutput>>() {};
        List<PdistOutput> res = caller.jsonrpcCall("kb_ke_util.run_pdist", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    /**
     * <p>Original spec-file function name: run_linkage</p>
     * <pre>
     * run_linkage: a wrapper method for scipy.cluster.hierarchy.linkage
     * reference: 
     * https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
     * </pre>
     * @param   params   instance of type {@link us.kbase.kbkeutil.LinkageParams LinkageParams}
     * @return   parameter "returnVal" of type {@link us.kbase.kbkeutil.LinkageOutput LinkageOutput}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public LinkageOutput runLinkage(LinkageParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<LinkageOutput>> retType = new TypeReference<List<LinkageOutput>>() {};
        List<LinkageOutput> res = caller.jsonrpcCall("kb_ke_util.run_linkage", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    /**
     * <p>Original spec-file function name: run_fcluster</p>
     * <pre>
     * run_fcluster: a wrapper method for scipy.cluster.hierarchy.fcluster
     * reference: 
     * https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html
     * </pre>
     * @param   params   instance of type {@link us.kbase.kbkeutil.FclusterParams FclusterParams}
     * @return   parameter "returnVal" of type {@link us.kbase.kbkeutil.FclusterOutput FclusterOutput}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public FclusterOutput runFcluster(FclusterParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<FclusterOutput>> retType = new TypeReference<List<FclusterOutput>>() {};
        List<FclusterOutput> res = caller.jsonrpcCall("kb_ke_util.run_fcluster", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    /**
     * <p>Original spec-file function name: run_dendrogram</p>
     * <pre>
     * run_dendrogram: a wrapper method for scipy.cluster.hierarchy.dendrogram
     * reference: 
     * https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html
     * </pre>
     * @param   params   instance of type {@link us.kbase.kbkeutil.DendrogramParams DendrogramParams}
     * @return   parameter "returnVal" of type {@link us.kbase.kbkeutil.DendrogramOutput DendrogramOutput}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public DendrogramOutput runDendrogram(DendrogramParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<DendrogramOutput>> retType = new TypeReference<List<DendrogramOutput>>() {};
        List<DendrogramOutput> res = caller.jsonrpcCall("kb_ke_util.run_dendrogram", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    /**
     * <p>Original spec-file function name: build_biclusters</p>
     * <pre>
     * build_biclusters: build biclusters and store result feature sets as JSON into shock
     * </pre>
     * @param   params   instance of type {@link us.kbase.kbkeutil.BuildBiclustersParams BuildBiclustersParams}
     * @return   parameter "returnVal" of type {@link us.kbase.kbkeutil.BuildBiclustersOutput BuildBiclustersOutput}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public BuildBiclustersOutput buildBiclusters(BuildBiclustersParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<BuildBiclustersOutput>> retType = new TypeReference<List<BuildBiclustersOutput>>() {};
        List<BuildBiclustersOutput> res = caller.jsonrpcCall("kb_ke_util.build_biclusters", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    /**
     * <p>Original spec-file function name: enrich_onthology</p>
     * <pre>
     * enrich_onthology: run GO term enrichment analysis
     * </pre>
     * @param   params   instance of type {@link us.kbase.kbkeutil.EnrichOnthologyParams EnrichOnthologyParams}
     * @return   parameter "returnVal" of type {@link us.kbase.kbkeutil.EnrichOnthologyOutput EnrichOnthologyOutput}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public EnrichOnthologyOutput enrichOnthology(EnrichOnthologyParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<EnrichOnthologyOutput>> retType = new TypeReference<List<EnrichOnthologyOutput>>() {};
        List<EnrichOnthologyOutput> res = caller.jsonrpcCall("kb_ke_util.enrich_onthology", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    /**
     * <p>Original spec-file function name: calc_onthology_dist</p>
     * <pre>
     * calc_onthology_dist: calculate onthology distance
     *                      (sum of steps for each node in onthology_pair travels to 
     *                       the nearest common ancestor node)
     *                      NOTE: return inf if no common ancestor node found
     * </pre>
     * @param   params   instance of type {@link us.kbase.kbkeutil.CalcOnthologyDistParams CalcOnthologyDistParams}
     * @return   parameter "returnVal" of type {@link us.kbase.kbkeutil.CalcOnthologyDistOutput CalcOnthologyDistOutput}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public CalcOnthologyDistOutput calcOnthologyDist(CalcOnthologyDistParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<CalcOnthologyDistOutput>> retType = new TypeReference<List<CalcOnthologyDistOutput>>() {};
        List<CalcOnthologyDistOutput> res = caller.jsonrpcCall("kb_ke_util.calc_onthology_dist", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    public Map<String, Object> status(RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        TypeReference<List<Map<String, Object>>> retType = new TypeReference<List<Map<String, Object>>>() {};
        List<Map<String, Object>> res = caller.jsonrpcCall("kb_ke_util.status", args, retType, true, false, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }
}
