# The Burger Store!

The burger store is a simple burger ordering program that runs in Code Institute's mockup terminal on Heroku.

It allows the user to put in an order for hamburgers, sides and drinks all of their choosing.

Have a go for yourself!
# link to heroku

# Main picture

## How to use it?
<hr>
Since it's a command line interface program the user simply makes their choices with numbers between 1-5 and answer questions with y for Yes and n for No.
After the user has completed their first order they are given the opportunity to add a menu for their friend aswell or finish their order with just food for themself.

## Features
<hr>

### Existing Features
<ul>
    <li>Opening question if the user wants to place an order
    <ul><li>Allows the user to answer yes or no
        <li>If user selects yes the burger menu shows up and they can start to place their order
        <li>If user selects no they recive a message "Thank you for stopping by!" and the application closes</li></ul>
    <li>Menus for burgers, extras, sides and drinks
        <ul><li>The menu items are found in the begining of the code consisting of key-value pairs for all the items</li></ul>
    <li> Hamburger menu with choices 0-5
    <li> Extras menu with choices 0-3
    <li> Sides menus with choices 0-4
    <li> Drinks menu with choices 0-4
    <li> All the menus allows the user to choose No Thanks (0) which add no cost to their basket and lets them skip that step
    <li>Question if they would like to add more products
        <ul><li>If user chooses yes the ordering proces starts from the begining again but keep the user choices in their basket
        <li>If user chooses no the user recives a message "Thank you for your order, your food is beeing prepared!" and the code restarts from the beging with an empty basket</li></ul>
</ul>



    
