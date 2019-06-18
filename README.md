# LutherPrinting

Phishing project for Information Assurance and Security (CS439) used to help us understand the social engineering techniques used to gather information. The ultimate goal of this project is to not only understand the techniques, but also be able to provide data on who clicks on the link. We recommended that if the College's IT department were to do a sample phishing attack, they should immediately follow up and provide education on how to spot phishing attacks to increase security posture.

## What we did
* Drafted [emails](https://github.com/aaronherman/LutherPrinting/blob/master/project7-emails.pdf) to students, faculty and staff
* Email sent contains a query parameter with unique code that will also say who has clicked on the link.
* Database will log who enters their username (no password is saved) into the login form.
* URL should be masked as "print.luther.edu" but really go to "printluther.com/<generated param>
