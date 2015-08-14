##### bulk_extractor
###### Scan an image (mem/partition/etc) and create analysis and carves
* bulk_extractor -o output img

###### Scan (10 threads)
* bulk_extractor -o output img -j 10

###### Scan for PDFs
* bulk_extractor -o output img -E pdf

###### Scan with wordlist
* bulk_extractor -o output img -e wordlist

###### Scan with regex
* bulk_extractor -o output img -f 'regex'

##### Resources
* [theevilbit](http://theevilbit.blogspot.com/2013/01/backtrack-forensics-bulkextractor.html)
