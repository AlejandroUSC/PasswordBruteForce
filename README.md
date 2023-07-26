## Password Brute Force Cracker

### *The Script*

 The script has been attached in the same zip as this document. There are 2 different script .py files. “FiveLineBruteForce.py” and “ComprehensiveBruteForce.py”.

ComprehensiveBruteForce.py contains a complete script that is relatively simple to understand. A script that generates 1 character at a time through a recursive call. Creating a “password” of the desired length will yield the word and compare its MD5 to the MD5 hash provided in hashes.txt. Upon discovery, it will print to the screen the standard password along with the time it took to discover.

FiveLineBruteForce.py contains a fully functional Brute Forcing script that operates in 5 lines of code. Same code as ComprehensiveBruteForce.py except fully compressed into 5 lines of code. Two versions are provided, a 3/4 length script that does the same as ComprehensiveBruteForce.py. And the other version is a 4/5 length script that does not print out the time it takes to crack the password hash.

### *Testing*
<p align="center">

|  Password  |  MD5  |  Time to Crack  |
|  :---:    | :----:| :------:  |
|  Z  |  21c2e59531c8710156d34a3c30ac81d5 |  0.000 ms  |
|  AD  |  e182ebbc166d73366e7986813a7fc5f1  |  0.000 ms  |
|  God  |  aeb9573c09919d210512b643907e56b8  |  0.085 ms  |
| 1234 | 81dc9bdb52d04dc20036dbd8313ed055 | 20.243 ms |
| AbCdE | 37e464916dcb6dfc3994ca4549e97272 | 26.387 sec |
| Trojan | a5312fd5717d3e2fd419132e3c3ac51b | 18.69 hrs |
| F1ghtOn | 57b46b0a1ac529ef1a3d6fa016b6995e | N/A |
| Earlgrey | 46216a0b09453799f35d04e7343ba0e6 | N/A |

</p>