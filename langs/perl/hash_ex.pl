#!/usr/bin/env perl

use strict;
use warnings;

my %category_hash =
  (
   1 => {
         name => 'whatever',
         children => {
           2 => {
                 name => 'something',
                 children => {
                   3 => { name => 'another subcategory' }
                 }
                }
          }
         },
    4 => { name => 'something else' }
  );

show(\%category_hash, 0);

sub show {
  my ($hash, $lvl) = @_;

  my $prefix = '  ' x $lvl;

  foreach (sort keys %$hash) {
    print "$prefix$_ : $hash->{$_}{name}\n";
    show($hash->{$_}{children}, ++$lvl)
      if exists $hash->{$_}{children};
  }
}

