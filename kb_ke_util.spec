/*
A KBase module: kb_ke_util
*/

module kb_ke_util {

  /* A boolean - 0 for false, 1 for true.
    @range (0, 1)
  */
  typedef int boolean;

  /* Input of the run_pdist function
    data_matrix - raw data matrix with row_ids, col_ids and values
                  e.g.{'row_ids': ['gene_1', 'gene_2'], 
                       'col_ids': ['condition_1', 'condition_2'],
                       'values': [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]}

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
    mapping<string, string> data_matrix;
    string metric;
  } PdistParams;

  /* Ouput of the run_pdist function
    square_dist_matrix - square form of distance matrix where the data is mirrored across 
                         the diagonal
    labels - item name corresponding to each square_dist_matrix element
  */
  typedef structure {
    list<list<string>> square_dist_matrix;
    list<string> labels;
  } PdistOutput;

  /* run_pdist: a wrapper method for scipy.spatial.distance.pdist
     reference: 
     https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html*/
  funcdef run_pdist(PdistParams params) returns(PdistOutput returnVal) authentication required;

  /* Input of the run_linkage function
    square_dist_matrix - square form of distance matrix (refer to run_pdist return)

    Optional arguments:
    method - The linkage algorithm to use. Default set to 'ward'.
             The method can be 
             ["single", "complete", "average", "weighted", "centroid", "median", "ward"]
             Details refer to: 
             https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
  */
  typedef structure {
    list<list<string>> square_dist_matrix;
    string method;
  } LinkageParams;

  /* Ouput of the run_linkage function
    linkage_matrix - The hierarchical clustering encoded as a linkage matrix
  */
  typedef structure {
    list<list<string>> linkage_matrix;
  } LinkageOutput;

  /* run_pdist: a wrapper method for scipy.cluster.hierarchy.linkage
     reference: 
     https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html*/
  funcdef run_linkage(LinkageParams params) returns(LinkageOutput returnVal) authentication required;


};
