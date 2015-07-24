#### Forensic Tools
##### Foremost
###### Grab all supported file types
* foremost -t all 

##### bulk_extractor
###### Scan an image (mem/partition/etc) and create analysis and carves
* bulk_extractor -o output_dir memory

##### Windows
###### Image a Shadow Copy
* dd.exe if=\\.\\HarddiskVolumeShadowCopy4 of=F:\snapshot4.img --localwrt
