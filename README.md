# MAIL -IN BALLOTS SYSTEM

**THEME**

*Imagine living in times where there are secure servers and we get an opportunity to vote online*

## HOW TO USE ?

*YOU NEED TWO EMAILS*

*ONE WHERE YOU WILL ACT AS COMMISSION AND THE OTHER WHERE ONE IS A VOTER*

*Line number 112 in commission.py where you will give commission's mail*

*Line number 115 in commission.py where you will give app password*

## ASSUMPTIONS

- This is a mere demo of a big system so we assume that there is only one system and a voter

- We assume that there are only 5 voter-id's to pick

- We assume that there are only a certain number of political parties

## WORKING OF CODES

*VOTER GIVES HIS EMAIL ,RECEIVES AN OTP,CONFIRMS THE OTP AND THEN GIVES HIS VOTER-ID NUMBER ,DATABASE SEARCHES FOR THAT VOTER-ID IN THE SYSTEM AND IF THE VOTER ID IS FOUND,IT ASKS TO CAST VOTE AND THEN SENDS THE CONFIRMATION RECEIPT TO YOUR EMAIL.ON THE OTHER HAND ,IT LOGS THAT VOTER ID AND VOTE INTO COMMISSIONS LOG FILE AND CONFIRMS WITH NUMBER '1' THAT YOU HAVE VOTED WHICH IS OTHERWISE SET TO ZERO.PUBLIC.PY IS FOR VOTERS WHICH IS MERGED INTO COMMISSION.PY LATER WHICH IS FOR COMMISSION*


