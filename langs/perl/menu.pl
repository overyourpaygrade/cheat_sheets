#!/usr/bin/env perl

use strict;
use warnings;

# Define the actions to take
my %action = (
  '1' => \&do_exit,
  'main' => \&main_prompt,
  'config' => \&config_prompt,
  'shut' => \&shut_down,
  'show' => \&scenario_get
);

my $prompt = "test> ";
my $scen;

TLD: while (1) {
  print $prompt;
  my $input = <>;
  chomp($input);
  if (defined $action{$input}) {
    $action{$input}->();
  } else {
    print "I didn't understand the command.\n";
  }
}

#-------------------------------------------------------------
sub main_prompt {
  $prompt = "test> ";
  return;
}

sub config_prompt {
  $prompt = "test# ";
  return;
}

sub do_exit {
  last TLD;
  return;
}

sub shut_down {
  $prompt = "shut# ";
  print "interface shutdown\n";
  system("ls -l");
}

sub scenario_get {
  print "int eth 1/1\n";
  $scen = "one";
}

