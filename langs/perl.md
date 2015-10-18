###### Hex to ASCII
* %68%74%74%70%3A%2F%2F
* cat file | perl -pe 's/%(..)/chr(hex($1))/ge'

###### UTF-16 to ASCII
* %u7468%u7074%u2F3A%u782F%u6169
* cat file | perl -pe 's/%u(..)(..)/chr(hex($2))/chr(hex($1))/ge'

###### Decimal to ASCII (/ = decimal)
* /104/116/116/112/58/47/47
* cat file | perl -pe 's/\/([0-9]+)/chr($1)/ge'

###### Octal to ASCII (\ = octal)
* \150\164\164\160\72\57\57
* cat file | perl -pe 's/\\([0-9]+)/chr(oct($1))/ge'

###### Eliminate Whitespace
* cat file | perl -pe 's/\n//g' | perl -pe 's/ //g'
