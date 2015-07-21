###### VDI to VMDK
* qemu-img convert input.vdi -O vmdk output.vmdk

###### VMDK to VDI
* qemu-img convert input.vmdk output.raw (then raw to vdi with vboxmanage)
