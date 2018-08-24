package kb_ke_util::kb_ke_utilClient;

use JSON::RPC::Client;
use POSIX;
use strict;
use Data::Dumper;
use URI;
use Bio::KBase::Exceptions;
my $get_time = sub { time, 0 };
eval {
    require Time::HiRes;
    $get_time = sub { Time::HiRes::gettimeofday() };
};

use Bio::KBase::AuthToken;

# Client version should match Impl version
# This is a Semantic Version number,
# http://semver.org
our $VERSION = "0.1.0";

=head1 NAME

kb_ke_util::kb_ke_utilClient

=head1 DESCRIPTION


A KBase module: kb_ke_util


=cut

sub new
{
    my($class, $url, @args) = @_;
    

    my $self = {
	client => kb_ke_util::kb_ke_utilClient::RpcClient->new,
	url => $url,
	headers => [],
    };

    chomp($self->{hostname} = `hostname`);
    $self->{hostname} ||= 'unknown-host';

    #
    # Set up for propagating KBRPC_TAG and KBRPC_METADATA environment variables through
    # to invoked services. If these values are not set, we create a new tag
    # and a metadata field with basic information about the invoking script.
    #
    if ($ENV{KBRPC_TAG})
    {
	$self->{kbrpc_tag} = $ENV{KBRPC_TAG};
    }
    else
    {
	my ($t, $us) = &$get_time();
	$us = sprintf("%06d", $us);
	my $ts = strftime("%Y-%m-%dT%H:%M:%S.${us}Z", gmtime $t);
	$self->{kbrpc_tag} = "C:$0:$self->{hostname}:$$:$ts";
    }
    push(@{$self->{headers}}, 'Kbrpc-Tag', $self->{kbrpc_tag});

    if ($ENV{KBRPC_METADATA})
    {
	$self->{kbrpc_metadata} = $ENV{KBRPC_METADATA};
	push(@{$self->{headers}}, 'Kbrpc-Metadata', $self->{kbrpc_metadata});
    }

    if ($ENV{KBRPC_ERROR_DEST})
    {
	$self->{kbrpc_error_dest} = $ENV{KBRPC_ERROR_DEST};
	push(@{$self->{headers}}, 'Kbrpc-Errordest', $self->{kbrpc_error_dest});
    }

    #
    # This module requires authentication.
    #
    # We create an auth token, passing through the arguments that we were (hopefully) given.

    {
	my %arg_hash2 = @args;
	if (exists $arg_hash2{"token"}) {
	    $self->{token} = $arg_hash2{"token"};
	} elsif (exists $arg_hash2{"user_id"}) {
	    my $token = Bio::KBase::AuthToken->new(@args);
	    if (!$token->error_message) {
	        $self->{token} = $token->token;
	    }
	}
	
	if (exists $self->{token})
	{
	    $self->{client}->{token} = $self->{token};
	}
    }

    my $ua = $self->{client}->ua;	 
    my $timeout = $ENV{CDMI_TIMEOUT} || (30 * 60);	 
    $ua->timeout($timeout);
    bless $self, $class;
    #    $self->_validate_version();
    return $self;
}




=head2 run_PCA

  $returnVal = $obj->run_PCA($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a kb_ke_util.PCAParams
$returnVal is a kb_ke_util.PCAOutput
PCAParams is a reference to a hash where the following keys are defined:
	data_matrix has a value which is a string
PCAOutput is a reference to a hash where the following keys are defined:
	PCA_matrix has a value which is a string

</pre>

=end html

=begin text

$params is a kb_ke_util.PCAParams
$returnVal is a kb_ke_util.PCAOutput
PCAParams is a reference to a hash where the following keys are defined:
	data_matrix has a value which is a string
PCAOutput is a reference to a hash where the following keys are defined:
	PCA_matrix has a value which is a string


=end text

=item Description

run_PCA: perform PCA on a n-dimensional matrix

=back

=cut

 sub run_PCA
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function run_PCA (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to run_PCA:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'run_PCA');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "kb_ke_util.run_PCA",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'run_PCA',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method run_PCA",
					    status_line => $self->{client}->status_line,
					    method_name => 'run_PCA',
				       );
    }
}
 


=head2 run_kmeans2

  $returnVal = $obj->run_kmeans2($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a kb_ke_util.KmeansParams
$returnVal is a kb_ke_util.KmeansOutput
KmeansParams is a reference to a hash where the following keys are defined:
	dist_matrix has a value which is a reference to a list where each element is a float
	k_num has a value which is an int
KmeansOutput is a reference to a hash where the following keys are defined:
	centroid has a value which is a reference to a list where each element is a float
	idx has a value which is a reference to a list where each element is an int

</pre>

=end html

=begin text

$params is a kb_ke_util.KmeansParams
$returnVal is a kb_ke_util.KmeansOutput
KmeansParams is a reference to a hash where the following keys are defined:
	dist_matrix has a value which is a reference to a list where each element is a float
	k_num has a value which is an int
KmeansOutput is a reference to a hash where the following keys are defined:
	centroid has a value which is a reference to a list where each element is a float
	idx has a value which is a reference to a list where each element is an int


=end text

=item Description

run_kmeans2: a wrapper method for  scipy.cluster.vq.kmeans2
reference:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.kmeans2.html#scipy.cluster.vq.kmeans2

=back

=cut

 sub run_kmeans2
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function run_kmeans2 (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to run_kmeans2:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'run_kmeans2');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "kb_ke_util.run_kmeans2",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'run_kmeans2',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method run_kmeans2",
					    status_line => $self->{client}->status_line,
					    method_name => 'run_kmeans2',
				       );
    }
}
 


=head2 run_pdist

  $returnVal = $obj->run_pdist($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a kb_ke_util.PdistParams
$returnVal is a kb_ke_util.PdistOutput
PdistParams is a reference to a hash where the following keys are defined:
	data_matrix has a value which is a string
	metric has a value which is a string
PdistOutput is a reference to a hash where the following keys are defined:
	dist_matrix has a value which is a reference to a list where each element is a float
	labels has a value which is a reference to a list where each element is a string

</pre>

=end html

=begin text

$params is a kb_ke_util.PdistParams
$returnVal is a kb_ke_util.PdistOutput
PdistParams is a reference to a hash where the following keys are defined:
	data_matrix has a value which is a string
	metric has a value which is a string
PdistOutput is a reference to a hash where the following keys are defined:
	dist_matrix has a value which is a reference to a list where each element is a float
	labels has a value which is a reference to a list where each element is a string


=end text

=item Description

run_pdist: a wrapper method for scipy.spatial.distance.pdist
reference: 
https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html

=back

=cut

 sub run_pdist
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function run_pdist (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to run_pdist:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'run_pdist');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "kb_ke_util.run_pdist",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'run_pdist',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method run_pdist",
					    status_line => $self->{client}->status_line,
					    method_name => 'run_pdist',
				       );
    }
}
 


=head2 run_linkage

  $returnVal = $obj->run_linkage($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a kb_ke_util.LinkageParams
$returnVal is a kb_ke_util.LinkageOutput
LinkageParams is a reference to a hash where the following keys are defined:
	dist_matrix has a value which is a reference to a list where each element is a float
	method has a value which is a string
LinkageOutput is a reference to a hash where the following keys are defined:
	linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a float

</pre>

=end html

=begin text

$params is a kb_ke_util.LinkageParams
$returnVal is a kb_ke_util.LinkageOutput
LinkageParams is a reference to a hash where the following keys are defined:
	dist_matrix has a value which is a reference to a list where each element is a float
	method has a value which is a string
LinkageOutput is a reference to a hash where the following keys are defined:
	linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a float


=end text

=item Description

run_linkage: a wrapper method for scipy.cluster.hierarchy.linkage
reference: 
https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

=back

=cut

 sub run_linkage
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function run_linkage (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to run_linkage:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'run_linkage');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "kb_ke_util.run_linkage",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'run_linkage',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method run_linkage",
					    status_line => $self->{client}->status_line,
					    method_name => 'run_linkage',
				       );
    }
}
 


=head2 run_fcluster

  $returnVal = $obj->run_fcluster($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a kb_ke_util.FclusterParams
$returnVal is a kb_ke_util.FclusterOutput
FclusterParams is a reference to a hash where the following keys are defined:
	linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a float
	dist_threshold has a value which is a float
	labels has a value which is a reference to a list where each element is a string
	criterion has a value which is a string
FclusterOutput is a reference to a hash where the following keys are defined:
	flat_cluster has a value which is a reference to a hash where the key is a string and the value is a reference to a list where each element is a string

</pre>

=end html

=begin text

$params is a kb_ke_util.FclusterParams
$returnVal is a kb_ke_util.FclusterOutput
FclusterParams is a reference to a hash where the following keys are defined:
	linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a float
	dist_threshold has a value which is a float
	labels has a value which is a reference to a list where each element is a string
	criterion has a value which is a string
FclusterOutput is a reference to a hash where the following keys are defined:
	flat_cluster has a value which is a reference to a hash where the key is a string and the value is a reference to a list where each element is a string


=end text

=item Description

run_fcluster: a wrapper method for scipy.cluster.hierarchy.fcluster
reference: 
https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html

=back

=cut

 sub run_fcluster
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function run_fcluster (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to run_fcluster:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'run_fcluster');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "kb_ke_util.run_fcluster",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'run_fcluster',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method run_fcluster",
					    status_line => $self->{client}->status_line,
					    method_name => 'run_fcluster',
				       );
    }
}
 


=head2 run_dendrogram

  $returnVal = $obj->run_dendrogram($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a kb_ke_util.DendrogramParams
$returnVal is a kb_ke_util.DendrogramOutput
DendrogramParams is a reference to a hash where the following keys are defined:
	linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a string
	dist_threshold has a value which is a float
	labels has a value which is a reference to a list where each element is a string
	last_merges has a value which is an int
DendrogramOutput is a reference to a hash where the following keys are defined:
	result_plots has a value which is a reference to a list where each element is a string

</pre>

=end html

=begin text

$params is a kb_ke_util.DendrogramParams
$returnVal is a kb_ke_util.DendrogramOutput
DendrogramParams is a reference to a hash where the following keys are defined:
	linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a string
	dist_threshold has a value which is a float
	labels has a value which is a reference to a list where each element is a string
	last_merges has a value which is an int
DendrogramOutput is a reference to a hash where the following keys are defined:
	result_plots has a value which is a reference to a list where each element is a string


=end text

=item Description

run_dendrogram: a wrapper method for scipy.cluster.hierarchy.dendrogram
reference: 
https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html

=back

=cut

 sub run_dendrogram
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function run_dendrogram (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to run_dendrogram:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'run_dendrogram');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "kb_ke_util.run_dendrogram",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'run_dendrogram',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method run_dendrogram",
					    status_line => $self->{client}->status_line,
					    method_name => 'run_dendrogram',
				       );
    }
}
 


=head2 build_biclusters

  $returnVal = $obj->build_biclusters($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a kb_ke_util.BuildBiclustersParams
$returnVal is a kb_ke_util.BuildBiclustersOutput
BuildBiclustersParams is a reference to a hash where the following keys are defined:
	ndarray_ref has a value which is a kb_ke_util.obj_ref
	dist_threshold has a value which is a float
	dist_metric has a value which is a string
	linkage_method has a value which is a string
	fcluster_criterion has a value which is a string
obj_ref is a string
BuildBiclustersOutput is a reference to a hash where the following keys are defined:
	biclusters has a value which is a reference to a list where each element is a reference to a list where each element is a string

</pre>

=end html

=begin text

$params is a kb_ke_util.BuildBiclustersParams
$returnVal is a kb_ke_util.BuildBiclustersOutput
BuildBiclustersParams is a reference to a hash where the following keys are defined:
	ndarray_ref has a value which is a kb_ke_util.obj_ref
	dist_threshold has a value which is a float
	dist_metric has a value which is a string
	linkage_method has a value which is a string
	fcluster_criterion has a value which is a string
obj_ref is a string
BuildBiclustersOutput is a reference to a hash where the following keys are defined:
	biclusters has a value which is a reference to a list where each element is a reference to a list where each element is a string


=end text

=item Description

build_biclusters: build biclusters and store result feature sets as JSON into shock

=back

=cut

 sub build_biclusters
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function build_biclusters (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to build_biclusters:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'build_biclusters');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "kb_ke_util.build_biclusters",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'build_biclusters',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method build_biclusters",
					    status_line => $self->{client}->status_line,
					    method_name => 'build_biclusters',
				       );
    }
}
 


=head2 enrich_onthology

  $returnVal = $obj->enrich_onthology($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a kb_ke_util.EnrichOnthologyParams
$returnVal is a kb_ke_util.EnrichOnthologyOutput
EnrichOnthologyParams is a reference to a hash where the following keys are defined:
	sample_set has a value which is a reference to a list where each element is a string
	entity_term_set has a value which is a reference to a hash where the key is a kb_ke_util.entity_guid and the value is a kb_ke_util.assigned_term_guids
	propagation has a value which is a kb_ke_util.boolean
entity_guid is a string
assigned_term_guids is a reference to a list where each element is a string
boolean is an int
EnrichOnthologyOutput is a reference to a hash where the following keys are defined:
	enrichment_profile has a value which is a reference to a hash where the key is a kb_ke_util.term_guid and the value is a kb_ke_util.TermEnrichment
term_guid is a string
TermEnrichment is a reference to a hash where the following keys are defined:
	sample_count has a value which is an int
	total_count has a value which is an int
	expected_count has a value which is an int
	p_value has a value which is a float

</pre>

=end html

=begin text

$params is a kb_ke_util.EnrichOnthologyParams
$returnVal is a kb_ke_util.EnrichOnthologyOutput
EnrichOnthologyParams is a reference to a hash where the following keys are defined:
	sample_set has a value which is a reference to a list where each element is a string
	entity_term_set has a value which is a reference to a hash where the key is a kb_ke_util.entity_guid and the value is a kb_ke_util.assigned_term_guids
	propagation has a value which is a kb_ke_util.boolean
entity_guid is a string
assigned_term_guids is a reference to a list where each element is a string
boolean is an int
EnrichOnthologyOutput is a reference to a hash where the following keys are defined:
	enrichment_profile has a value which is a reference to a hash where the key is a kb_ke_util.term_guid and the value is a kb_ke_util.TermEnrichment
term_guid is a string
TermEnrichment is a reference to a hash where the following keys are defined:
	sample_count has a value which is an int
	total_count has a value which is an int
	expected_count has a value which is an int
	p_value has a value which is a float


=end text

=item Description

enrich_onthology: run GO term enrichment analysis

=back

=cut

 sub enrich_onthology
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function enrich_onthology (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to enrich_onthology:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'enrich_onthology');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "kb_ke_util.enrich_onthology",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'enrich_onthology',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method enrich_onthology",
					    status_line => $self->{client}->status_line,
					    method_name => 'enrich_onthology',
				       );
    }
}
 


=head2 calc_onthology_dist

  $returnVal = $obj->calc_onthology_dist($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a kb_ke_util.CalcOnthologyDistParams
$returnVal is a kb_ke_util.CalcOnthologyDistOutput
CalcOnthologyDistParams is a reference to a hash where the following keys are defined:
	onthology_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is a kb_ke_util.onthology_pair
gene_id is a string
onthology_pair is a reference to a list where each element is a string
CalcOnthologyDistOutput is a reference to a hash where the following keys are defined:
	onthology_dist_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is an int

</pre>

=end html

=begin text

$params is a kb_ke_util.CalcOnthologyDistParams
$returnVal is a kb_ke_util.CalcOnthologyDistOutput
CalcOnthologyDistParams is a reference to a hash where the following keys are defined:
	onthology_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is a kb_ke_util.onthology_pair
gene_id is a string
onthology_pair is a reference to a list where each element is a string
CalcOnthologyDistOutput is a reference to a hash where the following keys are defined:
	onthology_dist_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is an int


=end text

=item Description

calc_onthology_dist: calculate onthology distance
(sum of steps for each node in onthology_pair travels to 
 the nearest common ancestor node)
NOTE: return inf if no common ancestor node found

=back

=cut

 sub calc_onthology_dist
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function calc_onthology_dist (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to calc_onthology_dist:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'calc_onthology_dist');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "kb_ke_util.calc_onthology_dist",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'calc_onthology_dist',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method calc_onthology_dist",
					    status_line => $self->{client}->status_line,
					    method_name => 'calc_onthology_dist',
				       );
    }
}
 


=head2 calc_weighted_onthology_dist

  $returnVal = $obj->calc_weighted_onthology_dist($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a kb_ke_util.CalcOnthologyDistParams
$returnVal is a kb_ke_util.CalcOnthologyDistOutput
CalcOnthologyDistParams is a reference to a hash where the following keys are defined:
	onthology_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is a kb_ke_util.onthology_pair
gene_id is a string
onthology_pair is a reference to a list where each element is a string
CalcOnthologyDistOutput is a reference to a hash where the following keys are defined:
	onthology_dist_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is an int

</pre>

=end html

=begin text

$params is a kb_ke_util.CalcOnthologyDistParams
$returnVal is a kb_ke_util.CalcOnthologyDistOutput
CalcOnthologyDistParams is a reference to a hash where the following keys are defined:
	onthology_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is a kb_ke_util.onthology_pair
gene_id is a string
onthology_pair is a reference to a list where each element is a string
CalcOnthologyDistOutput is a reference to a hash where the following keys are defined:
	onthology_dist_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is an int


=end text

=item Description

calc_weighted_onthology_dist: calculate weighted onthology distance
(edges are weighted from root to leaves
 root edges are weighted 1/2
 each child's edge weights half of its parent's edge)
NOTE: return inf if no common ancestor node found

=back

=cut

 sub calc_weighted_onthology_dist
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function calc_weighted_onthology_dist (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to calc_weighted_onthology_dist:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'calc_weighted_onthology_dist');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "kb_ke_util.calc_weighted_onthology_dist",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'calc_weighted_onthology_dist',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method calc_weighted_onthology_dist",
					    status_line => $self->{client}->status_line,
					    method_name => 'calc_weighted_onthology_dist',
				       );
    }
}
 
  
sub status
{
    my($self, @args) = @_;
    if ((my $n = @args) != 0) {
        Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
                                   "Invalid argument count for function status (received $n, expecting 0)");
    }
    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
        method => "kb_ke_util.status",
        params => \@args,
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
                           code => $result->content->{error}->{code},
                           method_name => 'status',
                           data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
                          );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method status",
                        status_line => $self->{client}->status_line,
                        method_name => 'status',
                       );
    }
}
   

sub version {
    my ($self) = @_;
    my $result = $self->{client}->call($self->{url}, $self->{headers}, {
        method => "kb_ke_util.version",
        params => [],
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(
                error => $result->error_message,
                code => $result->content->{code},
                method_name => 'calc_weighted_onthology_dist',
            );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(
            error => "Error invoking method calc_weighted_onthology_dist",
            status_line => $self->{client}->status_line,
            method_name => 'calc_weighted_onthology_dist',
        );
    }
}

sub _validate_version {
    my ($self) = @_;
    my $svr_version = $self->version();
    my $client_version = $VERSION;
    my ($cMajor, $cMinor) = split(/\./, $client_version);
    my ($sMajor, $sMinor) = split(/\./, $svr_version);
    if ($sMajor != $cMajor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Major version numbers differ.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor < $cMinor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Client minor version greater than Server minor version.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor > $cMinor) {
        warn "New client version available for kb_ke_util::kb_ke_utilClient\n";
    }
    if ($sMajor == 0) {
        warn "kb_ke_util::kb_ke_utilClient version is $svr_version. API subject to change.\n";
    }
}

=head1 TYPES



=head2 boolean

=over 4



=item Description

A boolean - 0 for false, 1 for true.
@range (0, 1)


=item Definition

=begin html

<pre>
an int
</pre>

=end html

=begin text

an int

=end text

=back



=head2 obj_ref

=over 4



=item Description

An X/Y/Z style reference


=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 PCAParams

=over 4



=item Description

Input of the run_PCA function
data_matrix - raw data matrix in json format
              e.g.{u'condition_1': {u'gene_1': 0.1, u'gene_2': 0.3, u'gene_3': None},
                   u'condition_2': {u'gene_1': 0.2, u'gene_2': 0.4, u'gene_3': None},
                   u'condition_3': {u'gene_1': 0.3, u'gene_2': 0.5, u'gene_3': None},
                   u'condition_4': {u'gene_1': 0.4, u'gene_2': 0.6, u'gene_3': None}}


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
data_matrix has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
data_matrix has a value which is a string


=end text

=back



=head2 PCAOutput

=over 4



=item Description

Ouput of the run_PCA function
PCA_matrix - PCA matrix in json format


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
PCA_matrix has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
PCA_matrix has a value which is a string


=end text

=back



=head2 KmeansParams

=over 4



=item Description

Input of the run_kmeans2 function
dist_matrix - a condensed distance matrix (refer to run_pdist return)
k_num: number of clusters to form


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
dist_matrix has a value which is a reference to a list where each element is a float
k_num has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
dist_matrix has a value which is a reference to a list where each element is a float
k_num has a value which is an int


=end text

=back



=head2 KmeansOutput

=over 4



=item Description

Ouput of the run_kmeans2 function
centroid - centroids found at the last iteration of k-means
idx - index of the centroid


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
centroid has a value which is a reference to a list where each element is a float
idx has a value which is a reference to a list where each element is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
centroid has a value which is a reference to a list where each element is a float
idx has a value which is a reference to a list where each element is an int


=end text

=back



=head2 PdistParams

=over 4



=item Description

Input of the run_pdist function
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


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
data_matrix has a value which is a string
metric has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
data_matrix has a value which is a string
metric has a value which is a string


=end text

=back



=head2 PdistOutput

=over 4



=item Description

Ouput of the run_pdist function
dist_matrix - 1D distance matrix
labels - item name corresponding to each dist_matrix element


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
dist_matrix has a value which is a reference to a list where each element is a float
labels has a value which is a reference to a list where each element is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
dist_matrix has a value which is a reference to a list where each element is a float
labels has a value which is a reference to a list where each element is a string


=end text

=back



=head2 LinkageParams

=over 4



=item Description

Input of the run_linkage function
dist_matrix - 1D distance matrix (refer to run_pdist return)

Optional arguments:
method - The linkage algorithm to use. Default set to 'ward'.
         The method can be 
         ["single", "complete", "average", "weighted", "centroid", "median", "ward"]
         Details refer to: 
         https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
dist_matrix has a value which is a reference to a list where each element is a float
method has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
dist_matrix has a value which is a reference to a list where each element is a float
method has a value which is a string


=end text

=back



=head2 LinkageOutput

=over 4



=item Description

Ouput of the run_linkage function
linkage_matrix - The hierarchical clustering encoded as a linkage matrix


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a float

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a float


=end text

=back



=head2 FclusterParams

=over 4



=item Description

Input of the run_fcluster function
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


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a float
dist_threshold has a value which is a float
labels has a value which is a reference to a list where each element is a string
criterion has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a float
dist_threshold has a value which is a float
labels has a value which is a reference to a list where each element is a string
criterion has a value which is a string


=end text

=back



=head2 FclusterOutput

=over 4



=item Description

Ouput of the run_fcluster function
flat_cluster - A dictionary of flat clusters.
               Each element of flat_cluster representing a cluster contains a label array. 
               (If labels is none, element position array is returned to each cluster group)


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
flat_cluster has a value which is a reference to a hash where the key is a string and the value is a reference to a list where each element is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
flat_cluster has a value which is a reference to a hash where the key is a string and the value is a reference to a list where each element is a string


=end text

=back



=head2 DendrogramParams

=over 4



=item Description

Input of the run_dendrogram function
linkage_matrix - hierarchical clustering linkage matrix (refer to run_linkage return)

Optional arguments:
dist_threshold - the threshold to apply when forming flat clusters (draw a horizontal line to dendrogram)
labels - items corresponding to each linkage_matrix element 
         (If labels are given, result dendrogram x-axis will be mapped to element in labels.)
last_merges - show only last given value merged clusters


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a string
dist_threshold has a value which is a float
labels has a value which is a reference to a list where each element is a string
last_merges has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
linkage_matrix has a value which is a reference to a list where each element is a reference to a list where each element is a string
dist_threshold has a value which is a float
labels has a value which is a reference to a list where each element is a string
last_merges has a value which is an int


=end text

=back



=head2 DendrogramOutput

=over 4



=item Description

Ouput of the run_dendrogram function
result_plots - List of result plot path(s)


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
result_plots has a value which is a reference to a list where each element is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
result_plots has a value which is a reference to a list where each element is a string


=end text

=back



=head2 BuildBiclustersParams

=over 4



=item Description

Input of the build_biclusters function
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


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
ndarray_ref has a value which is a kb_ke_util.obj_ref
dist_threshold has a value which is a float
dist_metric has a value which is a string
linkage_method has a value which is a string
fcluster_criterion has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
ndarray_ref has a value which is a kb_ke_util.obj_ref
dist_threshold has a value which is a float
dist_metric has a value which is a string
linkage_method has a value which is a string
fcluster_criterion has a value which is a string


=end text

=back



=head2 BuildBiclustersOutput

=over 4



=item Description

Ouput of the build_biclusters function
biclusters: list of biclusters
            e.g. [["gene_id_1", "gene_id_2"], ["gene_id_3"]]


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
biclusters has a value which is a reference to a list where each element is a reference to a list where each element is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
biclusters has a value which is a reference to a list where each element is a reference to a list where each element is a string


=end text

=back



=head2 entity_guid

=over 4



=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 assigned_term_guids

=over 4



=item Definition

=begin html

<pre>
a reference to a list where each element is a string
</pre>

=end html

=begin text

a reference to a list where each element is a string

=end text

=back



=head2 term_guid

=over 4



=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 TermEnrichment

=over 4



=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
sample_count has a value which is an int
total_count has a value which is an int
expected_count has a value which is an int
p_value has a value which is a float

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
sample_count has a value which is an int
total_count has a value which is an int
expected_count has a value which is an int
p_value has a value which is a float


=end text

=back



=head2 EnrichOnthologyParams

=over 4



=item Description

Input of the enrich_onthology function
sample_set: list of gene_ids in clustering
            e.g. ["gene_id_1", "gene_id_2", "gene_id_3"]
entity_term_set: entity terms dict structure where global GO term and gene_ids are stored
                 e.g. {"gene_id_1": ["go_term_1", "go_term_2"]}

Optional arguments:
propagation: includes is_a relationship to all go terms (default is 0)


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
sample_set has a value which is a reference to a list where each element is a string
entity_term_set has a value which is a reference to a hash where the key is a kb_ke_util.entity_guid and the value is a kb_ke_util.assigned_term_guids
propagation has a value which is a kb_ke_util.boolean

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
sample_set has a value which is a reference to a list where each element is a string
entity_term_set has a value which is a reference to a hash where the key is a kb_ke_util.entity_guid and the value is a kb_ke_util.assigned_term_guids
propagation has a value which is a kb_ke_util.boolean


=end text

=back



=head2 EnrichOnthologyOutput

=over 4



=item Description

Ouput of the enrich_onthology function
enrichment_profile: dict structure stores enrichment info
                    e.g. {"go_term_1": {"sample_count": 10,
                                        "total_count": 20,
                                        "p_value": 0.1,
                                        "ontology_type": "P"}}


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
enrichment_profile has a value which is a reference to a hash where the key is a kb_ke_util.term_guid and the value is a kb_ke_util.TermEnrichment

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
enrichment_profile has a value which is a reference to a hash where the key is a kb_ke_util.term_guid and the value is a kb_ke_util.TermEnrichment


=end text

=back



=head2 onthology_pair

=over 4



=item Definition

=begin html

<pre>
a reference to a list where each element is a string
</pre>

=end html

=begin text

a reference to a list where each element is a string

=end text

=back



=head2 gene_id

=over 4



=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 CalcOnthologyDistParams

=over 4



=item Description

Input of the calc_onthology_dist function
onthology_set: dict structure stores mapping of gene_id to paried onthology
               e.g. {"gene_id_1": ["go_term_1", "go_term_2"]}


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
onthology_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is a kb_ke_util.onthology_pair

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
onthology_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is a kb_ke_util.onthology_pair


=end text

=back



=head2 CalcOnthologyDistOutput

=over 4



=item Description

Ouput of the calc_onthology_dist function
onthology_dist_set: dict structure stores mapping of gene_id to dist
                    e.g. {"gene_id_1": 3}


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
onthology_dist_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
onthology_dist_set has a value which is a reference to a hash where the key is a kb_ke_util.gene_id and the value is an int


=end text

=back



=cut

package kb_ke_util::kb_ke_utilClient::RpcClient;
use base 'JSON::RPC::Client';
use POSIX;
use strict;

#
# Override JSON::RPC::Client::call because it doesn't handle error returns properly.
#

sub call {
    my ($self, $uri, $headers, $obj) = @_;
    my $result;


    {
	if ($uri =~ /\?/) {
	    $result = $self->_get($uri);
	}
	else {
	    Carp::croak "not hashref." unless (ref $obj eq 'HASH');
	    $result = $self->_post($uri, $headers, $obj);
	}

    }

    my $service = $obj->{method} =~ /^system\./ if ( $obj );

    $self->status_line($result->status_line);

    if ($result->is_success) {

        return unless($result->content); # notification?

        if ($service) {
            return JSON::RPC::ServiceObject->new($result, $self->json);
        }

        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    elsif ($result->content_type eq 'application/json')
    {
        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    else {
        return;
    }
}


sub _post {
    my ($self, $uri, $headers, $obj) = @_;
    my $json = $self->json;

    $obj->{version} ||= $self->{version} || '1.1';

    if ($obj->{version} eq '1.0') {
        delete $obj->{version};
        if (exists $obj->{id}) {
            $self->id($obj->{id}) if ($obj->{id}); # if undef, it is notification.
        }
        else {
            $obj->{id} = $self->id || ($self->id('JSON::RPC::Client'));
        }
    }
    else {
        # $obj->{id} = $self->id if (defined $self->id);
	# Assign a random number to the id if one hasn't been set
	$obj->{id} = (defined $self->id) ? $self->id : substr(rand(),2);
    }

    my $content = $json->encode($obj);

    $self->ua->post(
        $uri,
        Content_Type   => $self->{content_type},
        Content        => $content,
        Accept         => 'application/json',
	@$headers,
	($self->{token} ? (Authorization => $self->{token}) : ()),
    );
}



1;
