/*
A KBase module: kb_ke_util
*/

module kb_ke_util {

  /* A boolean - 0 for false, 1 for true.
    @range (0, 1)
  */
  typedef int boolean;

  /* An X/Y/Z style reference*/
  typedef string obj_ref;

  /***************
  math layer
  ***************/

    /* Input of the linkage_2_newick function
    linkage_matrix - hierarchical clustering linkage matrix (refer to run_linkage return)
    labels - items corresponding to each linkage_matrix element 
             (If labels are given, result flat_cluster will be mapped to element in labels.)
  */
  typedef structure {
    list<list<float>> linkage_matrix;
    list<string> labels;
  } NewickParams;

  /* Ouput of the linkage_2_newick function
    newick - newick representation of tree
             https://en.wikipedia.org/wiki/Newick_format
  */
  typedef structure {
    string newick;
  } NewickOutput;

  /* linkage_2_newick: convert a linkage matrix to newick format*/
  funcdef linkage_2_newick(NewickParams params) returns(NewickOutput returnVal) authentication required;

  /* Input of the run_PCA function
    data_matrix - raw data matrix in json format
                  e.g.{u'condition_1': {u'gene_1': 0.1, u'gene_2': 0.3, u'gene_3': None},
                       u'condition_2': {u'gene_1': 0.2, u'gene_2': 0.4, u'gene_3': None},
                       u'condition_3': {u'gene_1': 0.3, u'gene_2': 0.5, u'gene_3': None},
                       u'condition_4': {u'gene_1': 0.4, u'gene_2': 0.6, u'gene_3': None}}
    n_components - number of components (default 2)
  */
  typedef structure {
    string data_matrix;
    int n_components;
  } PCAParams;

  /* Ouput of the run_PCA function
    PCA_matrix - PCA matrix in json format with principal_component_1, principal_component_2 col
                 and same index as original data matrix
  */
  typedef structure {
    string PCA_matrix;
  } PCAOutput;

  /* run_PCA: perform PCA on a n-dimensional matrix*/
  funcdef run_PCA(PCAParams params) returns(PCAOutput returnVal) authentication required;

  /* Input of the run_kmeans2 function
    dist_matrix - a condensed distance matrix (refer to run_pdist return)
    k_num: number of clusters to form
  */
  typedef structure {
    list<float> dist_matrix;
    int k_num;
  } KmeansParams;

  /* Ouput of the run_kmeans2 function
    centroid - centroids found at the last iteration of k-means
    idx - index of the centroid
  */
  typedef structure {
    list<float> centroid;
    list<int> idx;
  } KmeansOutput;

  /* run_kmeans2: a wrapper method for  scipy.cluster.vq.kmeans2
        reference:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.kmeans2.html#scipy.cluster.vq.kmeans2*/
  funcdef run_kmeans2(KmeansParams params) returns(KmeansOutput returnVal) authentication required;

  /* Input of the run_pdist function
    data_matrix - raw data matrix in json format
                      e.g.{u'condition_1': {u'gene_1': 0.1, u'gene_2': 0.3, u'gene_3': None},
                           u'condition_2': {u'gene_1': 0.2, u'gene_2': 0.4, u'gene_3': None},
                           u'condition_3': {u'gene_1': 0.3, u'gene_2': 0.5, u'gene_3': None},
                           u'condition_4': {u'gene_1': 0.4, u'gene_2': 0.6, u'gene_3': None}}

    Optional arguments:
    metric - The distance metric to use. Default set to 'euclidean'.
             The distance function can be 
             ["braycurtis", "canberra", "chebyshev", "cityblock", "correlation", "cosine", 
              "dice", "euclidean", "hamming", "jaccard", "kulsinski", "matching", 
              "rogerstanimoto", "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean", 
              "yule"]
              Details refer to: 
              https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html

    Note: Advanced metric functions 'minkowski', 'seuclidean' and 'mahalanobis' included in 
          scipy.spatial.distance.pdist library are not implemented
  */
  typedef structure {
    string data_matrix;
    string metric;
  } PdistParams;

  /* Ouput of the run_pdist function
    dist_matrix - 1D distance matrix
    labels - item name corresponding to each dist_matrix element
  */
  typedef structure {
    list<float> dist_matrix;
    list<string> labels;
  } PdistOutput;

  /* run_pdist: a wrapper method for scipy.spatial.distance.pdist
     reference: 
     https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html*/
  funcdef run_pdist(PdistParams params) returns(PdistOutput returnVal) authentication required;

  /* Input of the run_linkage function
    dist_matrix - 1D distance matrix (refer to run_pdist return)

    Optional arguments:
    method - The linkage algorithm to use. Default set to 'single'.
             The method can be 
             ["single", "complete", "average", "weighted", "centroid", "median", "ward"]
             Details refer to: 
             https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
  */
  typedef structure {
    list<float> dist_matrix;
    string method;
  } LinkageParams;

  /* Ouput of the run_linkage function
    linkage_matrix - The hierarchical clustering encoded as a linkage matrix
  */
  typedef structure {
    list<list<float>> linkage_matrix;
  } LinkageOutput;

  /* run_linkage: a wrapper method for scipy.cluster.hierarchy.linkage
     reference: 
     https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html*/
  funcdef run_linkage(LinkageParams params) returns(LinkageOutput returnVal) authentication required;


  /* Input of the run_fcluster function
    linkage_matrix - hierarchical clustering linkage matrix (refer to run_linkage return)
    dist_threshold - the threshold to apply when forming flat clusters

    Optional arguments:
    labels - items corresponding to each linkage_matrix element 
             (If labels are given, result flat_cluster will be mapped to element in labels.)
    criterion - The criterion to use in forming flat clusters. Default set to 'distance'.
                The criterion can be 
                ["inconsistent", "distance", "maxclust"]
                Note: Advanced criterion 'monocrit', 'maxclust_monocrit' in 
                scipy.cluster.hierarchy.fcluster library are not implemented
                Details refer to: 
                https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html
  */
  typedef structure {
    list<list<float>> linkage_matrix;
    float dist_threshold;
    list<string> labels;
    string criterion;
  } FclusterParams;

  /* Ouput of the run_fcluster function
     flat_cluster - A dictionary of flat clusters.
                    Each element of flat_cluster representing a cluster contains a label array. 
                    (If labels is none, element position array is returned to each cluster group)
  */
  typedef structure {
    mapping<string, list<string>> flat_cluster;
  } FclusterOutput;

  /* run_fcluster: a wrapper method for scipy.cluster.hierarchy.fcluster
     reference: 
     https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html*/
  funcdef run_fcluster(FclusterParams params) returns(FclusterOutput returnVal) authentication required;

  /* Input of the run_dendrogram function
    linkage_matrix - hierarchical clustering linkage matrix (refer to run_linkage return)

    Optional arguments:
    dist_threshold - the threshold to apply when forming flat clusters (draw a horizontal line to dendrogram)
    labels - items corresponding to each linkage_matrix element 
             (If labels are given, result dendrogram x-axis will be mapped to element in labels.)
    last_merges - show only last given value merged clusters
  */
  typedef structure {
    list<list<string>> linkage_matrix;
    float dist_threshold;
    list<string> labels;
    int last_merges;
  } DendrogramParams;

  /* Ouput of the run_dendrogram function
     result_plots - List of result plot path(s)
  */
  typedef structure {
    list<string> result_plots;
  } DendrogramOutput;

  /* run_dendrogram: a wrapper method for scipy.cluster.hierarchy.dendrogram
     reference: 
     https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html*/
  funcdef run_dendrogram(DendrogramParams params) returns(DendrogramOutput returnVal) authentication required;

  /***************
  persistence layer
  ***************/

  /* Input of the build_biclusters function
    ndarray_ref: NDArray object reference
    dist_threshold: the threshold to apply when forming flat clusters

    Optional arguments:
    dist_metric: The distance metric to use. Default set to 'euclidean'.
                 The distance function can be
                 ["braycurtis", "canberra", "chebyshev", "cityblock", "correlation", "cosine", 
                  "dice", "euclidean", "hamming", "jaccard", "kulsinski", "matching", 
                  "rogerstanimoto", "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean", 
                  "yule"]
                 Details refer to:
                 https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html

    linkage_method: The linkage algorithm to use. Default set to 'ward'.
                    The method can be
                    ["single", "complete", "average", "weighted", "centroid", "median", "ward"]
                    Details refer to:
                    https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

    fcluster_criterion: The criterion to use in forming flat clusters. Default set to 'distance'.
                        The criterion can be
                        ["inconsistent", "distance", "maxclust"]
                        Details refer to:
                        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html
  */
  typedef structure{
      obj_ref ndarray_ref;
      float dist_threshold;

      string dist_metric;
      string linkage_method;
      string fcluster_criterion;
  } BuildBiclustersParams;

  /* Ouput of the build_biclusters function
    biclusters: list of biclusters
                e.g. [["gene_id_1", "gene_id_2"], ["gene_id_3"]]
  */
  typedef structure {
    list<list<string>> biclusters;
  } BuildBiclustersOutput;

  /*
  build_biclusters: build biclusters and store result feature sets as JSON into shock
  */
  funcdef build_biclusters(BuildBiclustersParams params) returns (BuildBiclustersOutput returnVal) authentication required;

  typedef string entity_guid;
  typedef list<string> assigned_term_guids;
  typedef string term_guid;

  typedef structure{
      int sample_count;
      int total_count;
      int expected_count;
      float p_value;
  } TermEnrichment;

  /* Input of the enrich_onthology function
    sample_set: list of gene_ids in clustering
                e.g. ["gene_id_1", "gene_id_2", "gene_id_3"]
    entity_term_set: entity terms dict structure where global GO term and gene_ids are stored
                     e.g. {"gene_id_1": ["go_term_1", "go_term_2"]}

    Optional arguments:
    propagation: includes is_a relationship to all go terms (default is 0)
  */
  typedef structure{
      list<string> sample_set;
      mapping<entity_guid, assigned_term_guids> entity_term_set;

      boolean propagation;
  } EnrichOnthologyParams;

  /* Ouput of the enrich_onthology function
    enrichment_profile: dict structure stores enrichment info
                        e.g. {"go_term_1": {"sample_count": 10,
                                            "total_count": 20,
                                            "p_value": 0.1,
                                            "ontology_type": "P"}}
  */
  typedef structure {
    mapping<term_guid, TermEnrichment> enrichment_profile;
  } EnrichOnthologyOutput;

  /*
  enrich_onthology: run GO term enrichment analysis
  */
  funcdef enrich_onthology(EnrichOnthologyParams params) returns (EnrichOnthologyOutput returnVal) authentication required;

  typedef list<string> onthology_pair;
  typedef string gene_id;

  /* Input of the calc_onthology_dist function
    onthology_set: dict structure stores mapping of gene_id to paried onthology
                   e.g. {"gene_id_1": ["go_term_1", "go_term_2"]}
  */
  typedef structure{
      mapping<gene_id, onthology_pair> onthology_set;
  } CalcOnthologyDistParams;

  /* Ouput of the calc_onthology_dist function
    onthology_dist_set: dict structure stores mapping of gene_id to dist
                        e.g. {"gene_id_1": 3}
  */
  typedef structure {
    mapping<gene_id, int> onthology_dist_set;
  } CalcOnthologyDistOutput;

  /*
  calc_onthology_dist: calculate onthology distance
                       (sum of steps for each node in onthology_pair travels to 
                        the nearest common ancestor node)
                       NOTE: return inf if no common ancestor node found
  */
  funcdef calc_onthology_dist(CalcOnthologyDistParams params) returns (CalcOnthologyDistOutput returnVal) authentication required;

  /*
  calc_weighted_onthology_dist: calculate weighted onthology distance
                                (edges are weighted from root to leaves
                                 root edges are weighted 1/2
                                 each child's edge weights half of its parent's edge)
                                NOTE: return inf if no common ancestor node found
  */
  funcdef calc_weighted_onthology_dist(CalcOnthologyDistParams params) returns (CalcOnthologyDistOutput returnVal) authentication required;

};
