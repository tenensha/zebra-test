# zebra-test

The script performs the required tasks set by Aviad of Zebra-Med. It gets as an argument a .txt file, which contains several JSON objects. It then addes a randomized field to each object, indicating a successful or failed login attempt. The script creates 2 .txt files: One similar to the input .txt file, with the added field. The other contains a list of all the usernames whose login attempt failed at least once. It prints the paths of the 2 new .txt files.
