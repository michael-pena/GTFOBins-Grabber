# GTFOBins-Grabber
A post exploitation tool for pen testing/CTFs. After running a command like 


``` find / -type f -perm -04000 -ls 2>/dev/null ```

to find all SUID files on a target system, copy the output to a text file and feed it as command line parameter to this tool. It will tell you which binaries can be foud on GTFOBins along with a link to the page.


![GTFOBins Grabber Screen Shot](https://i.imgur.com/lL4GQRZ.png)
