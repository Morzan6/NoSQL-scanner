"""Test scans"""

scan1 = """Starting Nmap 7.94 ( https://nmap.org ) at 2024-01-06 14:47 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up, received conn-refused (0.000066s latency).

PORT      STATE SERVICE REASON  VERSION
27017/tcp open  mongodb syn-ack MongoDB 2.8.0
| vulscan: VulDB - https://vuldb.com:
| [191331] VS Code Extension up to 0.7.0 on MongoDB Binary File insufficiently protected credentials
| [105777] Red Hat Satellite 6 MongoDB access control
| [101984] Red Hat Satellite 6 MongoDB improper authentication
|
| MITRE CVE - https://cve.mitre.org:
| [CVE-2013-4650] MongoDB 2.4.x before 2.4.5 and 2.5.x before 2.5.1 allows remote authenticated users to obtain internal system privileges by leveraging a username of __system in an arbitrary database.
|
| SecurityFocus - https://www.securityfocus.com/bid/:
| [101689] MongoDB CVE-2017-15535 Memory Corruption Vulnerability
| [100825] MongoDB libbson CVE-2017-14227 Heap Buffer Overflow Vulnerability
| [94929] MongoDB CVE-2016-3104 Remote Denial of Service Vulnerability
| [92204] mongodb-clients CVE-2016-6494 Local Information Disclosure Vulnerability
| [77959] Mongodb CVE-2014-3971 Denial-Of-Service Vulnerability
| [64687] MongoDB BSON Object Length Parsing Information Disclosure Vulnerability
| [61309] MongoDB 'conn' Mongo Object Remote Code Execution Vulnerability
| [61007] MongoDB Remote Privilege Escalation Vulnerability
| [60252] MongoDB CVE-2013-2132 NULL Pointer Dereference Remote Denial of Service Vulnerability
| [58695] MongoDB CVE-2013-1892 Remote Code Injection Vulnerability
|
| IBM X-Force - https://exchange.xforce.ibmcloud.com:
| [85842] MongoDB CVE-2013-4142 code execution
| [85468] MongoDB privilege escalation
| [83054] MongoDB engine_spidermonkey.cpp code execution
|
| Exploit-DB - https://www.exploit-db.com:
| [24947] MongoDB nativeHelper.apply Remote Code Execution
| [24935] MongoDB nativeHelper.apply Remote Code Execution
|
| OpenVAS (Nessus) - http://www.openvas.org:
| [100748] MongoDB Web Admin Detection
| [100747] MongoDB Detection
|
| SecurityTracker - https://www.securitytracker.com:
| No findings
|
| OSVDB - http://www.osvdb.org:
| [95549] MongoDB system.users Collection Permission Weakness Password Hash Disclosure
| [95507] MongoDB V8 JavaScript Engine Unitialized conn Object Prototype Calling Arbitrary Code Execution
| [94901] MongoDB Arbitrary Database __system Name Remote Privilege Escalation
| [93804] MongoDB mongo-python-driver (pymongo) _cbsonmodule.c Null Pointer Dereference DoS
| [91717] MongoDB Default Unpassworded Administrator Account
| [91716] MongoDB Plaintext Data Local Disclosure
| [91632] MongoDB engine_spidermonkey.cpp nativeHelper.apply Function Remote Code Execution
| [84782] Wireshark MongoDB Dissector Infinite Loop Malformed Packet Parsing Remote DoS
|_

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.61 seconds"""

scan2 = """Starting Nmap 7.94 ( https://nmap.org ) at 2024-01-06 12:28 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up, received conn-refused (0.00011s latency).

PORT      STATE SERVICE REASON  VERSION
27017/tcp open  mongodb syn-ack MongoDB 2.8.0
| vulscan: scipvuldb.csv:
| [191331] VS Code Extension up to 0.7.0 on MongoDB Binary File insufficiently protected credentials
| [105777] Red Hat Satellite 6 MongoDB access control
| [101984] Red Hat Satellite 6 MongoDB improper authentication
| 
|_

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.27 seconds
"""

scan3 = """Starting Nmap 7.94 ( https://nmap.org ) at 2024-01-06 12:41 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up, received conn-refused (0.00023s latency).

PORT     STATE SERVICE REASON  VERSION
6379/tcp open  redis   syn-ack Redis key-value store 2.8.23
| vulscan: VulDB - https://vuldb.com:
| [204698] Dell PowerStore up to 2.x PowerStore T Environment os command injection
| [204697] Dell EMC PowerStore up to 2.x PSTCLI uncontrolled search path
| [201230] Dell EMC PowerStore 2.0.0.x/2.0.1.x/2.1.0.x os command injection
| [201154] Dell PowerStore X/PowerStore > 2.0.0.x/2.0.1.x credentials storage
| [144784] Redis 2.6 Temp File /tmp/redis.ds input validation
| [144783] Redis up to 2.5 Temp File /tmp/redis-%p.vm input validation
| [100510] Juniper NorthStar Controller Application up to 2.1.0 Stored information disclosure
| [100164] Oracle SuperCluster Specific Software 2.3.8/2.3.13 Backup/Restore Utility access control
| [46679] Toshiba Face Recognition 2.0.2.32 Stored credentials management
| 
| MITRE CVE - https://cve.mitre.org:
| [CVE-2012-5883] Cross-site scripting (XSS) vulnerability in the Flash component infrastructure in YUI 2.8.0 through 2.9.0, as used in Bugzilla 3.7.x and 4.0.x before 4.0.9, 4.1.x and 4.2.x before 4.2.4, and 4.3.x and 4.4.x before 4.4rc1, allows remote attackers to inject arbitrary web script or HTML via vectors related to swfstore.swf, a similar issue to CVE-2010-4209.
| [CVE-2012-0458] Mozilla Firefox before 3.6.28 and 4.x through 10.0, Firefox ESR 10.x before 10.0.3, Thunderbird before 3.1.20 and 5.0 through 10.0, Thunderbird ESR 10.x before 10.0.3, and SeaMonkey before 2.8 do not properly restrict setting the home page through the dragging of a URL to the home button, which allows user-assisted remote attackers to execute arbitrary JavaScript code with chrome privileges via a javascript: URL that is later interpreted in the about:sessionrestore context.
| [CVE-2010-4209] Cross-site scripting (XSS) vulnerability in the Flash component infrastructure in YUI 2.8.0 through 2.8.1, as used in Bugzilla 3.7.1 through 3.7.3 and 4.1, allows remote attackers to inject arbitrary web script or HTML via vectors related to swfstore/swfstore.swf.
| [CVE-2006-6949] Conti FTPServer 1.0 Build 2.8 stores user passwords in cleartext in MyServerSettings.ini, which allows local users to obtain sensitive information by reading this file.
| [CVE-2006-2020] Asterisk Recording Interface (ARI) in Asterisk@Home before 2.8 stores recordings/includes/main.conf under the web document root with insufficient access control, which allows remote attackers to obtain password information.
| [CVE-2005-1617] Willings WebCam and WebCam Lite 2.8 and earlier stores the password in memory in plaintext, which allows local users to gain sensitive information.
| [CVE-2002-2412] Winamp 2.80 stores authentication credentials in plaintext in the (1) [HTTP-AUTH] and (2) [winamp] sections in winamp.ini, which allows local users to gain access to other accounts.
| 
| SecurityFocus - https://www.securityfocus.com/bid/:
| [101050] WordPress 2kb Amazon Affiliates Store Plugin Multiple Cross Site Scripting Vulnerabilities
| [43189] Microsoft Visual C++ 2008 Redistributable Package DLL Loading Arbitrary Code Execution Vulnerability
| [14772] Microsoft Exchange Server 2003 Exchange Information Store Denial Of Service Vulnerability
| [2133] Microsoft Windows 2000 Directory Services Restore Mode Blank Password Vulnerability
| [1958] Microsoft Exchange 2000 Server EUSR_EXSTOREEVENT Account Vulnerability
| [1827] Norton AntiVirus 2001 _Restore Directory Virus Detection Bypass Vulnerability
| [1442] Debian Linux 2.1 dump Symlink Restore Vulnerability
| [1295] Microsoft Windows 2000 Default 40-bit Encrypted Protected Store Vulnerability
| 
| IBM X-Force - https://exchange.xforce.ibmcloud.com:
| [63840] Microsoft Visual C++ 2008 Redistributable Package dynamic-linked library (DLL) code execution
| [48090] Sagem F@st 2404 router restoreinfo.cgi weak security
| [15254] WebStores 2000 error.asp cross-site scripting
| [15253] WebStores 2000 browse_items.asp SQL injection
| [12135] WebStores 2000 browse_item_details.asp SQL injection
| [8015] Intel PRO/Wireless 2011B LAN USB Device driver stores WEP key in plaintext
| [5936] Microsoft Windows 2000 Server Directory Service Restore Mode allows user to login with blank password
| [4966] Roxen 2.0 local admin password stored in world readable file
| [4589] Microsoft Windows 2000 protected store can be compromised by brute force attack
| 
| Exploit-DB - https://www.exploit-db.com:
| [30373] Ability Mail Server 2013 (3.1.1) - Stored XSS (Web UI)
| [28157] VirtuaStore 2.0 Password Parameter SQL Injection Vulnerability
| [25529] StorePortal 2.63 Default.ASP Multiple SQL Injection Vulnerabilities
| [23467] iSoft-Solutions QuikStore Shopping Cart 2.12 template Parameter Directory Traversal Vulnerability
| [23466] iSoft-Solutions QuikStore Shopping Cart 2.12 store Parameter Path Disclosure Vulnerability
| [20790] businesswiki 2.5rc3 - Stored XSS & arbitrary file upload
| [20675] uebimiau webmail 2.7.2 - Stored XSS
| [20353] mailtraq 2.17.3.3150 - Stored XSS
| [20014] Solaris 2.5/2.6/7.0/8 ufsrestore Buffer Overflow Vulnerability
| [19951] QuickCommerce 2.5/3.0,Cart32 2.5 a/3.0,Shop Express 1.0,StoreCreator 3.0 Web Shopping Cart Hidden Form Field Vulnerability
| [19023] Wordpress wpStoreCart Plugin 2.5.27-2.5.29 Arbitrary File Upload
| [18980] Vanilla Forums 2.0.18.4 Tagging Stored XSS
| [18290] Winn Guestbook 2.4.8c - Stored XSS Vulnerability
| [17050] Family Connections CMS 2.3.2 (POST) Stored XSS And XML Injection
| [16233] Relevanssi 2.7.2 Wordpress Plugin Stored XSS Vulnerability
| [16232] GigPress 2.1.10 Wordpress Plugin Stored XSS Vulnerability
| [16196] eventum issue tracking system 2.3.1 - Stored XSS
| [16128] jakcms 2.0 pro rc5 - Stored XSS via useragent http header injection
| [12323] wb news (webmobo) 2.3.3 - Stored XSS
| [9964] RunCMS 2m1 store() SQL injection
| [9447] AJ Auction Pro OOPD 2.x (store.php id) SQL Injection Exploit
| [6193] E-Store Kit- <= 2 PayPal Edition (pid) SQL Injection Vulnerability
| [2710] Ariadne <= 2.4 store_config[code] Remote File Include Vulnerabilities
| [1780] phpBB <= 2.0.20 (Admin/Restore DB/default_lang) Remote Exploit
| 
| OpenVAS (Nessus) - http://www.openvas.org:
| [902469] ManageEngine ServiceDesk Plus Multiple Stored XSS Vulnerabilities
| [855496] Solaris Update for /usr/lib/fs/ufs/ufsrestore 109092-10
| [855201] Solaris Update for /usr/lib/fs/ufs/ufsrestore 109091-10
| [803109] PHP Server Monitor Multiple Stored Cross-Site Scripting Vulnerabilities
| [802270] GoAhead Webserver Multiple Stored Cross Site Scripting Vulnerabilities
| [103323] Joomla! Alameda Component 'storeid' Parameter SQL Injection Vulnerability
| [100098] Turnkey eBook Store 'keywords' Parameter Cross Site Scripting Vulnerability
| [56528] Debian Security Advisory DSA 1022-1 (storebackup)
| [14597] WS_FTP client weak stored password
| [10874] Rich Media E-Commerce Stores Sensitive Information Insecurely
| [10532] eXtropia Web Store remote file retrieval
| 
| SecurityTracker - https://www.securitytracker.com:
| [1009115] Webstores 2000 Has More Input Validation Flaws in 'browser_item_details.asp' That Let Remote Users Inject SQL Commands and Execute OS Commands
| [1006893] Webstores 2000 Input Validation Flaw Lets Remote Users Inject SQL Commands
| 
| OSVDB - http://www.osvdb.org:
| [52457] Sagem F@st 2404 restoreinfo.cgi Remote Reboot DoS
| [50589] Microsoft SQL Server 2000 sp_replwritetovarbin() Stored Procedure Overflow
| [23575] StoreBot 2005 Professional Edition MgrLogin.asp Pwd Parameter SQL Injection
| [23574] StoreBot 2002 Standard Edition manage.asp ShipMethod Parameter XSS
| [23200] Microsoft SQLServer 2000 Encrypted Stored Procedure Dynamic Query Disclosure
| [13762] Microsoft 2000 Domain Controller Directory Service Restore Mode Blank Password
| [10633] Microsoft Windows 2000 Protected Store Weak Encryption Default
| [4779] Microsoft Desktop Engine (MSDE) 2000 Stored Procedure SQL Injection
| [4778] Microsoft SQL Server 2000 Stored Procedure SQL Injection
| [3995] Webstores 2000 browse_items.asp Search_Text Parameter SQL Injection
| [3994] Webstores 2000 error.asp XSS
| [1449] Debian Linux 2.1 dump Symlink Restore
|_

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.57 seconds
"""
