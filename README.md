# The Burger Store!

The burger store is a simple burger ordering program that runs in Code Institute's mockup terminal on Heroku.

It allows the user to put in an order for hamburgers, sides and drinks all of their choosing.

Have a go for yourself!
https://the-burger-store.herokuapp.com/
![Am I responsive](assets/images/Ska%CC%88rmavbild%202023-04-07%20kl.%2008.42.37.png)

## How to use it?
<hr>
Since it's a command line interface program the user simply makes their choices with numbers between 1-5 and answer questions with y for Yes and n for No.
After the user has completed their first order they are given the opportunity to add a menu for their friend aswell or finish their order with just food for themself.

## Features
<hr>

### Existing Features
<ul>

![Alt text](assets/images/Ska%CC%88rmavbild%202023-04-07%20kl.%2008.44.39.png)
    <li>Opening question if the user wants to place an order
        <ul><li>Allows the user to answer yes or no
        <li>If user selects yes the burger menu shows up and they can start to place their order
        <li>If user selects no they recive a message "Thank you for stopping by!" and the application closes</li></ul>
    <li>Menus for burgers, extras, sides and drinks
        <ul><li>The menu items are found in the begining of the code consisting of key-value pairs for all the items</li></ul>
        ![Alt text](assets/images/Ska%CC%88rmavbild%202023-04-07%20kl.%2008.45.59.png)
    <li> Hamburger menu with choices 0-5![Alt text](assets/images/Ska%CC%88rmavbild%202023-04-07%20kl.%2008.47.13.png)
    <li> Extras menu with choices 0-3![Alt text](assets/images/Ska%CC%88rmavbild%202023-04-07%20kl.%2008.48.38.png)
    <li> Sides menus with choices 0-4![Alt text](assets/images/Ska%CC%88rmavbild%202023-04-07%20kl.%2008.49.20.png)
    <li> Drinks menu with choices 0-4
    <li> All the menus allows the user to choose No Thanks (0) which add no cost to their basket and lets them skip that step![Alt text](assets/images/Ska%CC%88rmavbild%202023-04-07%20kl.%2008.49.46.png)
    <li>Question if they would like to add more products
        <ul><li>If user chooses yes the ordering proces starts from the begining again but keep the user choices in their basket
        <li>If user chooses no the user recives a message "Thank you for your order, your food is beeing prepared!" and the code restarts from the beging with an empty basket</li></ul>
</ul>

## Future Features
<ul>
    <li>Get menu from Google Sheets insted of having it in the code
        <ul><li>Would make it easier for other users to change the menu</li></ul>
    <li>Being able to skip a step without adding a free product to the basket
        <ul><li>Would make the recipt look cleaner and easier to read</li></ul>
    </li>
</ul>

## Testing
<hr>
<ul>
    <li>Ran the code through PEP8 tester supplied by Code Institute with no issues

https://pep8ci.herokuapp.com/ 
    </li>
</ul>

### Manual Testing
<ul>
    <li>Tested the deployed app in Chrome, Firefox and Safari
        <ul>
        <li>Chrome and Firefox loads the app and allows me to make inputs
        <li>Safari both on the computer and iphone does not respond to inputs in the app</li></ul>
    <li>Press y on first input - Expected burger menu to load
        <ul> Results:
        <li>Lower case y loads burger menu
        <li>Upper case Y loads burger menu
        </li></ul>
    <li> Press n on first input - Expected text response "Thank you for stopping by!" and loop to finish
        <ul>Results:
        <li>Lower case n recives expected result
        <li>Upper case N recives expected result
        </li></ul>
    <li>Entering any other key on first input - Expected text "Invalid input. Please enter Y or N." and question to reload
        <ul>Results:
        <li>Entering A-Ö exept Y and N recives text and question reloads
        <li>Entering 0-9 recives expected result
        </li></ul>
    <li>Entering correct value (0-3, 0-4, 0-5) on following questions (burger menu, extras menu, sides menu and drinks menu) - Expected text showing what you orderd at what price and next question to load
        <ul>Results:
        <li>Expected result accured
        </li></ul>   
    <li>Entering incorrect value on following questions (burger menu, extras menu, sides menu and drinks menu) - Expected test response "Please enter a number thats on the menu" and question to reload
        <ul>Results:
        <li>Entering A-Ö exept Y and N recives text and question reloads
        <li>Entering 0-9 recives expected result
        </li></ul>
</ul>

## Deployment on Heroku
<hr>
<ul>
    <li>Createt an account on Heroku website

https://www.heroku.com
<li>Click "New -> Create new app" button
<li>Insert your app's Name and Choose your region then click the "Create App" button
<li>On the menu on the top click "Setting"
<li>Go to "Buildpacks" and select "Add buildpacks"
<li>Add Python and NodeJS buildpack, in that order
<li>Click on the "Depoly" tab and select GitHub
<li>Click "App connected to GitHub" and enter your GitHub repository
<li>Choose if you want to manual or automatic deplyment
<li>When deployment is finnished a link will be provided to your site
</li>
</ul>

## Clone the Repository Code Locally
<hr>
Navigate to the GitHub Repository you want to clone
<ul>
<li>Click on the code drop down button
<li>Select HTTPS
<li>Copy the repository link to your clipboard
<li>Open you IDE of choice (git must be installed for the next step)
<li>Type git clone copied-git-url into the IDE termial
<li>The project will now been cloned on your local machine for use.
</li></ul>

## Credits
<hr>






    
