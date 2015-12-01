# Manipulate Files with Perl
# http://www.devdungeon.com/content/manipulate-files-perl

print "Check if a file exists\n";

if ( -e "text.txt") {
  print "File exists\n";
} else {
  print "File does not exist\n";
}

print "Example 2 - Get File Size in bytes\n";

my $fileSizeInBytes = -s 'text.txt';
print $fileSizeInBytes, "\n";

print "Example 3 - Change File Permissions\n";
my $filePath = "text.txt";
chmod(0755, $filePath);

print "Example 4 - Deleting Files\n";
#unlink($filePath);

print "Example 5 - Opening and Closing Files\n";
$file = 'test.txt';

# Pick one:
#open(INFO, $file); # Open for input
#open(INFO, "<$file"); # Another way to open for input
#open(INFO, ">$file"); # Open for output
open(INFO, ">>$file"); # Open for appending

# Close when finished
#close(INFO);

print "Example 6 - Read File Contents\n";
# Store all the lines of the file into an array
@line = <INFO>;

print "Example 7 - Write to File\n";

print INFO "This line goes to the file.\n";
