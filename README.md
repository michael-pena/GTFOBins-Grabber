# GTFOBins Grabber
A quick and dirty post exploitation tool I made to assist with SUID privilege escalation. I thought of this while studying for the OSCP.
After gaining a shell on the target and running the command:

``` find / -type f -perm -04000 -ls 2>/dev/null ```

to find SUID files, a penetration tester will often compare the results of the output on the target to the binaries listed on GTFOBins. This tool lets penetration testers know which binaries on the target system can be found on GTFOBins, saving a little bit of time. 

Simply run the find command and save the output to a text file (on your attacking machine). Run this tool with the text file as a command line parameter and it will tell you which binaries can be found on GTFObins along with a url to the page that will aid in privilege escalation.


![GTFOBins Grabber Screen Shot](https://i.imgur.com/lL4GQRZ.png)
