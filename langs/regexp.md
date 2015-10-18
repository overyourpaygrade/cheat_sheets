###### IPv4
* ^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$

###### IPv4 CIDR
* ^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)/(3[0-2]|[1-2]?[0-9])$

###### MAC Address
* ([a-fA-F0-9]{2}\:){5}[a-fA-F0-9]{2}

###### Email
* [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}
* '/^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})*$/'
* "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]"

###### URLs
* (http|https|ftp|mail)\:[\/\w.]+
* '/^(((http|https|ftp):\/\/)?([[a-zA-Z0-9]\-\.])+(\.)([[a-zA-Z0-9]]){2,4}([[a-zA-Z0-9]\/+=%&_\.~?\-]*))*$/'

###### [Dates](http://www.virtuosimedia.com/dev/php/37-tested-php-perl-and-javascript-regular-expressions)
* '#^((19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01]))*$#'

###### Domain Names
* "[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU|UK)"


##### Resources
* [A Security Site](http://asecuritysite.com/subjects/chapter20)
