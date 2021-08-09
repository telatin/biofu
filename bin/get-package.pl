#!/usr/bin/env perl

use 5.014;
use warnings;
use JSON::PP;           # In core since v5.13.9
use File::Basename;
use File::Spec;
use Getopt::Long;
my $VERSION = "1.0";
my (  $opt_version, $opt_help, $opt_verbose, $opt_destdir);
GetOptions(
    'o|output-dir=s' => \$opt_destdir,
    'verbose' => \$opt_verbose,
    'version' => \$opt_version,
    'help'    => \$opt_help,
);

my $program_name = basename($0);
my $program_dir  = File::Basename::dirname($0);
my $json_list    = $program_dir . '/packages.json';
my $package      = shift @ARGV;

# Home dir
my $home_dir = $ENV{'HOME'};
my $bin_dir  = $home_dir . '/bin/';
if ( ! -d "$bin_dir" and not defined "$opt_destdir" ) {
    my $dest_dir = "$bin_dir";
}

if (! -f $json_list) {
    die "Error: $json_list not found\n";
}
my $json_text = do {
   open(my $json_fh, "<:encoding(UTF-8)", $json_list)
      or die("Can't open \$json_list\": $!\n");
   local $/;
   <$json_fh>
};

my $data = decode_json($json_text);


if (defined $package) {
    my $package_data = $data->{$package};
    if (defined $package_data) {
        my $cmd = $package_data->{"command"};
        if (defined $cmd) {
            print "$cmd\n";
            exec "$cmd";
        } 
    } else {
        die "Error: Package $package not found\n";
    }
} else {
    foreach my $package_name (keys(%$data)) {
        print " [$package_name]\n\t", $data->{$package_name}->{'name'} ,"\n" if defined $data->{$package_name}->{'name'};
    }
}