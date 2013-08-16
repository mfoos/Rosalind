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

my $previous = 0;
while (<BROKEN>){
	chomp;
	if ($_ =~ /^>/){
		if ($previous == 0){
			print FIXED $_,"\n";
			$previous = 1;
		}
		else {
			print FIXED "\n",$_,"\n";
		}	
	} else {
		print FIXED $_;
	}
}

close(BROKEN);
close(FIXED);

