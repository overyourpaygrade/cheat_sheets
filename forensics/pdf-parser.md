###### show contents of pdf (BONUS)
* pdfinfo pdf1.pdf

###### Search for JS object in pdf1
* pdf-parser.py --search /JavaScript pdf1.pdf

###### View contents of indirect object 32
* pdf-parser.py --object 32 pdf1.pdf

###### Extract using correct filter into a raw file to look at contents
* pdf-parser.py --object 32 --filter --raw pdf1.pdf > out.js
