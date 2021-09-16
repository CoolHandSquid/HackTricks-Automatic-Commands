<h1 align="center">HackTricks Automatic Commands "HAC"</h1>
<p align="center">HackTricks Automatic Commands (HAC) is an enumeration platform powered by <a href="https://book.hacktricks.xyz">HackTricks</a>!</p>
<p align="center">
  <a><img src="https://img.shields.io/badge/price-FREE-0098f7.svg" height="20"/></a>
  <a><img src="https://img.shields.io/github/license/mashape/apistatus.svg" height="20"/></a>
  <a><img src="https://img.shields.io/badge/OS-Kali-yellow.svg" height="20"/></a>
  <a><img src="https://img.shields.io/badge/python-3.7%2B-blue.svg" height="20"/></a>
  <a><img src="https://img.shields.io/badge/version-1.0.0-lightgrey.svg" height="20"/></a>
  <a href="https://twitter.com/intent/tweet?text=I%20love%20automating%20the%20scanning%20and%20enumeration%20capabilities%20I%20have%20with%20the%20enumeration%20platform%20powered%20by%20https%3A%2F%2Fbook.HackTricks.xyz%21%20It%20is%20so%20convenient%21&url=https://github.com/CoolHandSquid/HAC&via=CoolHandSquid&hashtags=infosec,oscp,HackTheBox,kalilinux,pentesting"><img src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social" alt="tweet" height="20"></a>
</p>

## Contents
  - [About](#about)
  - [Philosophy](#philosophy)
  - [Demo](#demo)
    - [Tmux](#tmux)
    - [Tilix](#tilix)
    - [Terminator](#terminator)
  - [Build and Kickoff](#build-and-kickoff)
  - [Methodology](#methodology)
  - [ProTips](#protips)
  - [How To Contribute](#how-to-contribute)
  - [Supporters](#supporters)
  - [Contact](#contact)

## About
- HackTricks Automatic Commands (HAC) is an enumeration platform powered by [HackTricks](https://book.hacktricks.xyz)
- Updated weekly from "HackTricks Automatic Commands" yaml code blocks in Hacktricks
- Product of 19% Security Solutions

## Philosophy
Where other enumeration tools are fire and forget (sometimes running hundereds of scans without your control), HAC is semi-automatic, meaning that you initiate every scan. This is a valuable trait becasue you...
- are able to limit your footprint
- end with a convenient list of all scans sent from HAC to the target
- will gain more profitable experience on training boxes (OSCP, HTB, TryHackMe)
- can approach network penetration tests with confidence and reliability

## Demo

### Tmux
![TmuxRecon](https://github.com/CoolHandSquid/HAC/blob/main/Images/TmuxRecon.gif)
### Tilix
![Tire Fire](https://github.com/CoolHandSquid/HAC/blob/main/Images/TireFireFinal1.gif)
### Terminator
Still in development, coming soon!

## Build and Kickoff
```
git clone https://github.com/CoolHandSquid/HAC.git
cd HAC
./Build.sh

#cd /dir/you/want/to/enumerate/from
HAC x.x.x.x -i tmux #Chose "tmux", "tilix", or "terminator" as your interface.
```

## Methodology
1. Kickoff TmuxRecon (TmuxRecon 10.10.10.5).  
  ![alt text](https://github.com/CoolHandSquid/HAC/blob/main/Images/HAC_Kickoff_1.png)
2. C-b w (Move into the TmuxRecon Session).
  ![alt text](https://github.com/CoolHandSquid/HAC/blob/main/Images/HAC_Kickoff_2.png)
3. When prompted, type "Y" to kickoff a Quick, Banner, All-Port, and UDP nmap scan.
  ![alt text](https://github.com/CoolHandSquid/HAC/blob/main/Images/TmuxRecon_Init_2.png)
4. Notice that new windows were opened kicking off those scans. Depending upon the ports returned, run scans for those ports.
  ![alt text](https://github.com/CoolHandSquid/HAC/blob/main/Images/TmuxRecon_InAction_3.png)
5. Change variables as you need to suit your target (Example: HTTP running on port 8500).
  ![alt text](https://github.com/CoolHandSquid/HAC/blob/main/Images/TmuxRecon_Variables_6.png)

## ProTips
- Run multiple commands from a table at once by splitting the command numbers with commas. EX: 0,1,2 (Spaces and periods work aswell)

## How To Contribute
What makes HackTricks Automatic Commands so powerful is the People! You can help contribute by sending a PR to book.hacktricks.xyz (into an existing HackTricks Automatic Commands yaml code block or create your own), or sending and email to coolhandsquid@gmail.com. Simply follow this template when creating your own. Notice that
- the title must be correct (It is used for parsing)
- each entry has a different name
- each entry has either a "Note" or a "Command" section. A Command section will get executed, where a Note section will only be read to screen
```
## HackTricks Automatic Commands

```text
Protocol_Name: DNS    #Protocol Abbreviation if there is one.
Port_Number:  53     #Comma separated if there is more than one.
Protocol_Description: Domain Name Service        #Protocol Abbreviation Spelled out

Entry_1:
  Name: Notes
  Description: Notes for DNS
  Note: |
    #These are the commands I run every time I see an open DNS port

    dnsrecon -r 127.0.0.0/24 -n {IP} -d {Domain_Name}
    dnsrecon -r 127.0.1.0/24 -n {IP} -d {Domain_Name}
    dnsrecon -r {Network}{CIDR} -n {IP} -d {Domain_Name}
    dig axfr @{IP}
    dig axfr {Domain_Name} @{IP}
    nslookup
        SERVER {IP}
        127.0.0.1
        {IP}
        Domain_Name
        exit

    https://book.hacktricks.xyz/pentesting/pentesting-dns

Entry_2:
  Name: Banner Grab
  Description: Grab DNS Banner
  Command: dig version.bind CHAOS TXT @DNS
```

### HAC Meta Language
```
&&&&
&&&& Anywhere in the command will split the line and start each command individually in separate tabs.
Example: whoami &&&& id &&&& ifconfig will open three tabs and run the desired command in each. &&&& is useful if you initially run multiple separate commands every time you see a specific port open.

?
"?" is for sending a question to the user. The responce will be set to a numbered variable.
You can send multiple lines of questions for multiple variables.
Example:
?What is the location of the wp-login.php? Example: /Yeet/cannon/wp-login.php
?What is a known password you would like to brute force?
wpscan --url {Web_Proto}://{IP}{1} --enumerate ap,at,cb,dbe && wpscan --url {Web_Proto}://{IP}{1} --enumerate u,tt,t,vp --password {2} -e 

{}
{} is for grabbing a variable from HAC.
Available variables are:
  IP
  Network
  CIDR
  Domain_Name
  Naming_Context
  Web_Proto
  Web_Port
  Username
  Password
  Big_Passwordlist
  Small_Passwordlist
  Big_Dirlist
  Small_Dirlist
  Tool_Dir
Current variable values can be viewed in the variables table.
```
## Supporters
[![Stargazers repo roster for @coolhandsquid/HAC](https://reporoster.com/stars/coolhandsquid/HAC)](https://github.com/coolhandsquid/HAC/stargazers)
[![Forkers repo roster for coolhandsquid/HAC](https://reporoster.com/forks/coolhandsquid/HAC)](https://github.com/coolhandsquid/HAC/network/members)

## Contact
Please contact me at CoolHandSquid32@gmail.com for contribution, suggestions, and ideas!  
<p align="center">
<img src="https://github.com/CoolHandSquid/HAC/blob/main/Images/TireFireLogo1.png" width="200" />  
</p>
<p align="center">
<img src="https://github.com/CoolHandSquid/HAC/blob/main/Images/CoolHandSquid.jpg" width="200" /> 
</p>

<p align="center"><a href="https://github.com/coolhandsquid/HAC#Contents"><img src="https://github.com/CoolHandSquid/HAC/blob/main/Images/backToTopButton.png" alt="Back to top" height="29"/></a></p>
