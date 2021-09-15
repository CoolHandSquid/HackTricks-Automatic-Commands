# HAC
HackTricks Automatic Commands (HAC) is an enumeration platform powered by [HackTricks](https://book.hacktricks.xyz)! 
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

### Tilix

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
  ![alt text](https://github.com/CoolHandSquid/HAC/blob/main/Images/TmuxRecon_Kickoff_1.png)
2. C-b w (Move into the TmuxRecon Session).
  ![alt text](https://github.com/CoolHandSquid/HAC/blob/main/Images/TmuxRecon_Kickoff_1.5.png)
3. When prompted, type "Y" to kickoff a Quick, Banner, All-Port, and UDP nmap scan.
  ![alt text](https://github.com/CoolHandSquid/HAC/blob/main/Images/TmuxRecon_Init_2.png)
4. Notice that new windows were opened kicking off those scans. Depending upon the ports returned, run scans for those ports.
  ![alt text](https://github.com/CoolHandSquid/HAC/blob/main/Images/TmuxRecon_InAction_3.png)
5. Change variables as you need to suit your target (Example: HTTP running on port 8500).
  ![alt text](https://github.com/CoolHandSquid/HAC/blob/main/Images/TmuxRecon_Variables_6.png)

## ProTips
- Run multiple commands from a table at once by splitting the command numbers with commas. EX: 0,1,2 (Spaces and periods work aswell)

## How To Contribute
[![Stargazers repo roster for @coolhandsquid/HAC](https://reporoster.com/stars/coolhandsquid/HAC)](https://github.com/coolhandsquid/HAC/stargazers)
[![Forkers repo roster for coolhandsquid/HAC](https://reporoster.com/forks/coolhandsquid/HAC)](https://github.com/coolhandsquid/HAC/network/members)

### HAC Meta Language

## Supporters

## Contact
