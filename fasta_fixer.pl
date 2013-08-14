#!usr/bin/perl;
use warnings;
use strict;

chomp(my $filename = $ARGV[0]);
unless(open(BROKEN,"<",$filename)){
	die "That file doesn't exist: $!";
}

$filename = $filename . ".fixed";
unless(open(FIXED,">$filename")){
	die "That outfile cannot be opened: $!";
}

while (<BROKEN>){
	chomp;
	if ($_ =~ /^>/){
		print FIXED "\n",$_,"\n";
	} else {
		print FIXED $_;
	}
}

close(BROKEN);
close(FIXED);

