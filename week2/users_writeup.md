  # Part 1 – /etc/passwd Explanation

Command used:
cat /etc/passwd | grep -E "dev_alice|dev_bob"

Example entry:
dev_alice:x:1003:1003::/home/dev_alice:/bin/bash

## Field Breakdown

1. Username  
   The login name used to access the system.

2. Password Placeholder  
   The `x` indicates that the encrypted password is stored securely in `/etc/shadow`.

3. UID (User ID)  
   A unique numerical identifier assigned to the user.

4. GID (Group ID)  
   The numerical identifier of the user’s primary group.

5. GECOS / Comment Field  
   Used to store additional information about the user (often full name). It is empty in this case.

6. Home Directory  
   The directory assigned to the user where personal files are stored.

7. Default Shell  
   The command-line shell assigned to the user. In this case, `/bin/bash`.
