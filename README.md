# Supreme Bot 
---
- Design Specifications
    - We already have the clientele, advertising will be fine.
    - the bot has to automate the process of buying in advance. 
        - UI
            - create interface to add items from droplists in advance
            - create interface for checkout delay
            - refresh interval to be able to see the new items on drop time as soon as possible.
            - basket delay 
            - notification system for users in US and Japan when an item has been sold out (completely or a specific color that the user wanted). Give options on preferred color. -> Color Priority List?
            - Text messages for captcha, and other notifications, etc. Telling them to go online to fill it out, log in to google or whatever.
            - have user defaults. have a settings tab with a restore defaults option.
            - maybe have an info button that leads to information on what numbers to input.
            - Renewal Fee? $20/yr
            - interface to log in to google?
            - if a user has 10 different things they want to buy, we need say 10 proxies.
            - create an interface for the user to manage their google emails that they use in order to run in parallel.
            - start with supreme, and then add palace and Kith.
            - autodropbot.com
        - Workflow
            1. User add items they want from droplists
                - Option 1: Sync with SupremeCommunity.com
                - Option 2: Load a UI for adding what the want on the spot without using a SupremeCommunity account.
                - Add color priority lists, as well as other settings (date and time of the drop, etc)
            2. User enters Bot Settings
                - the checkout delay, refresh delay, and basket delay
                - option to use multiple emails
                - option to use incognito (first the user has to enable the extension in Incognito)
            3. Billing info
                - bad practice to store users credit card info, so try to sync with Autofill (or some other 3rd party safe credit card info hosting platform), or just cache the info, but never save it to any of our servers (if servers are ever needed).
            4. Notifications (text, email, )
                - Make sure your computer is on
                - Item Sold out 
                - Color Sold out. Looking for x preference.
        - Backend
            - simple database with userid and emails.
        - Implementation
            - A Chrome App 
---
- End goals
    - get ready for the December 1st drop
---