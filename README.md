# Homemade-Hashing
My novice attempt at learning python by creating a simple hashing program <br>
I started this project as an introduction for myself to learn a bit of python while creating something useful. My goal was to use the standards paper for the SHA-256 hashing algorithm and create a simple tool that could take a string of finite length, and output the SHA-256 hash to the terminal. 
I followed <a href="https://csrc.nist.gov/files/pubs/fips/180-2/final/docs/fips180-2.pdf">this standards document</a> <br><br>
This was my first attempt at learning python, and coding as a whole besides some small attempts as a child. The methods I used here are doubtless not the best implementation, but I digress. <br><br>
What will follow here is a breakdown of my code and an explanation of how I decided upon each method, with pictures attached! <br>
![lines1-10](https://github.com/wtpreston/Homemade-Hashing/assets/168564307/98eafae7-fbfe-4e4b-a9d6-14249d22f7ab) 
The idea for this first section of code was to read a users input, and format it into a concatenated string of binary numbers. This is necessary because the hashing function requires the input to be a very specific length. If the message is *exactly* 512 bits in length, then it can be hashed freely. But this rarely occurs by chance, so some grooming will need to be done to the message so that it can be processed by the hashing function. Essentially I need to measure the length of the string, (Line 3) and find the next multiple of 512 that is *larger* than the message length (Lines 5 through 10). Once the while loop in Line 6 has completed, we're left with two useful pieces of information. the blockCount variable in line 4 will tell us how many 512-bit blocks the message will be divided into. Using this we can determine the 'padCount' which is the number of 0 bits we will append to the message so it fits the exact length required by the algorithm. 
