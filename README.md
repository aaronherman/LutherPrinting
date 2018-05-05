# LutherPrinting

## Ideas
* Database will log who enters their username (no password is saved) into the login form.
* Have the email contain a query parameter with unique code that will also say who has clicked on the link.
* Once they have clicked the link and been added to the database of being at risk, send them an email immediately saying what happened.
* URL should be masked as "print.luther.edu" but really go to "printluther.com/<generated param>
* From IT department

## Who's Doing What
* Devin: Back-end
    * API for query parameter
        * `printluther.com/?<norsekey>`
    * API for username and add to database
        * `printluther.com/signin/<norsekey>`
* Kyle: Front-end & email
    * Create table for the above API
      * username (string), clicked_link (bool), and entered_password (bool)
    * Login page
* Taylor: Front-end
    * Print dashboard
* Aaron: Email
    * Draft of email
    * Easy way to add query paramter to link of email
