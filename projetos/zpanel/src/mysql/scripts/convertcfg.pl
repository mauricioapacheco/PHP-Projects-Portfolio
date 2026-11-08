#!/usr/bin/perl
#
# $Id: convertcfg.pl,v 2.0 2003/11/18 15:20:45 nijel Exp $
#
# Configuration converter
# Converts from old-style (Pre-2.3) configuration files to new format found in PMA-2.3
#
# Takes input from STDIN, sends output to STDOUT
#
# By Robin Johnson contato@example.invalid
# Many thanks to Patrick Lougheed contato@example.invalid
#

while(<>) 
{	s/\$cfg(\w+)/\$cfg\[\'$1\'\]/g; 
	print; 
	}


