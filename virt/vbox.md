###### Convert vdi to vmdk
* vboxmanage clonehd input.vdi output.vmdk --format vmdk

###### Convert vmdk to vdi
* vboxmanage clonehd input.vmdk output.vdi --format vdi

###### Covert from VDI to RAW
* vboxmanage internalcommands converttoraw img.vdi img.dd

###### Dump VBox RAM
* vboxmanage debugvm safeclone dumpvmcore --filename=getthekey
