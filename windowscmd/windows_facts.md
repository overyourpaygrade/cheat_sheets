###### SIDs (Security Identifiers)
* unique idenitifiers assigned to objects by Windows systems and domain controllers.
* Windows uses these SIDs to ref specific accounts and check security privileges for those accounts
* Well known account SIDs:
  * S-1-5-18 - LocalSystem
  * S-1-5-19 - LocalService
  * S-1-5-20 - NetworkService
* Group SIDs:
  * S-1-5-32-544 - Administrators
  * S-1-5-32-545 - Users
  * S-1-5-32-546 - Guests

###### Useful Registry Keys
* Start Menu -> Run
	* HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
* Typed URLs
	* HKCU\Software\Microsoft\Internet Explorer\TyperURLs
* User Assist (Followed by a GUID, Names are Rot13 "encrypted")
	* HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist
* Start up Locations
	* HKLM\SOftware\Microsoft\Windows\CurrentVersion\Runonce
	* HKLM\SOftware\Microsoft\Windows\CurrentVersion\policies\Explorer\Run
	* HKLM\SOftware\Microsoft\Windows\CurrentVersion\Run
	* HKCU\SOftware\Microsoft\Windows NT\CurrentVersion\Windows\Run
	* HKCU\SOftware\Microsoft\Windows\CurrentVersion\Run
	* HKCU\SOftware\Microsoft\Windows\CurrentVersion\RunOnce
