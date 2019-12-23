# Cook Book


Cook Book is a online recipe cook book, where users can create, edit, delete and search recipes.  This application is a full stack project using Flask web development.  The application is a project based assssement for Code Institiute to demonstrate good knowledge of Python programming language, working with a external database  MongoDB and deploying to Heroku.


# UX

The application's style and layout was designed to look modern, fresh, simple yet visually exciting.  The site must be mobile first friendly, and also maintain its style feeling in all web browser versions.  To support these aims, the colour scheme of the site was white, light grey (#f5f5f5) and greenish blue (#17a2b8 Bootstrap color info).  Text content was kept to a minimum - all text was written to be clear, short and directive.  Most importantly, the site used images to support user navigation/site know-how rather than long text explanations. 

# User Stories
  
- #1 - when I enter the site, I want to be visually impressed and understand its purpose.
- #2 - when navigating the home page I want the text to be balanced, light text on dark background and dark text on white background, so its easy for me to read.
- #3 - the images on the home page should support a sense of feeling as to what the text content is saying.
- #4 - if I want to continue browsing the site, the home page should have some links that can direct me, rather than replying on the navbar.
- #5 - if I visit other pages of the site, I would like to see clarificaiton that i am on the correct page.
- #6 - if I decide to use the navbar to visit other pages, I want the navbar to be clear as to what its purpose is.
- #7 - if i visit the recipes.html page, i dont want long text explanantions, pop-ups, or anything which prevents me from just seeing the recipes
- #8 - when looking at the advertised recipes on the recipes.html page - i want the recipes to advertised in a visually nice way which has clues/description as to what the recipe is.
- #9 - when wanting to visit a recipe, i want to have some confirmation that what i am doing is correct, or have clues of what to do to.
- #10 - if i decide to check a recipe in detail, i want the information of that recipe to be shown in a clear way which is nice to read and visually appealing.
- #11 - if i decide to edit a recipe, i would to know how to do this or how to get there to edit the recipe
- #12 - if i decide to edit a recipe, i would to clearly see the content of what i can edit and have some information which tells me if its is correct or not.
- #13 - when i have made updates, i would like some confirmation that what i have done has been confirmed.
- #14 - if i decide to delete a recipe, i would like to know how to do this or how to get there to delete the recipe.
- #15 - as i know that deletion has a negative feeling, it would be good to know that if i delete something, is it the recipe or just an element of the recipe?  In case i made a mistake in understanding this, just to be safe - does delete mean delete all?
- #16 - if i decide to create a recipe, i would to know how to do this or how to get there to create a recipe.
- #17 - if i decide to create a recipe, i would like to clearly see the content of what i can add and have some information which tells me if its is correct or not.
- #18 - when i have created a recipe, i would like some confirmation that what i have done has been confirmed.
- #19 - if i want to search for a recipe, i dont want the search to be based on simple conditions - i dont want to search for ingredients as that could mean i have too many recipes to look at - instead i want to see recipes based on some criteria of recipe title, type of food - vegetarian, vegan, meat or something else which helps me to find a recipe that i am or would be interested in.
- #20 - if there was a recipe i liked but forgot the whole name, it would be nice to know if i remebered something of that title that i could use as a search parameter.
- #21 - when navigating the recipes page, it would be nice if it wasn't too cluttered with recipes.
  
# Features

- Home.html - user can see site banner and some link sto the sites fucntionality - search recipes, create recipes, view recipes.
- recipes.html - user can see the recipe collection - the user can see how many recipes have been created.  When the user selects a recipes, they will be shown all the content information and be given a choice to either edit or delete or continue browsing.  This page is paginated so that it is easy for the user to view recipes in clear order and navigate more if they choose to.
- search.html - user can search for specific recipes based on 3 conditions : 
- RECIPE TYPE - when creating a recipe, the user must select a food type - this is a pre-set select list based from a google search on food type categories.
- RECIPE CUISINE - when creating a recipe, the user must select a food cuisine - this is a pre-set select list based from a google search on food cuisines.
- RECIPE NAME TAGS - when creating a recipe, the user must enter a title name - this search will find all posiible fields in this title name.
- Important features of site development and database schema - as the site needed to have some visual clues as to what the user can view or search based on their interest, whilst also trying to support a coherent search paramater and user engagement - the application used recipe_tags to do this.  If a recipe included onion as an ingredient, and 'as a user i searched onion' - then the chances are my search would return all recipes - because of this that search feature would defeat its purpose.  Instead, the application based it on looking for meat dish, or egg dish or spanish dish or chinese dish.  For the user, this makes it much easier to find something they are intersted in.  The title search is there to help the user if it is something specific that they are familiar with - something that they know to be true.


# Features Left to Implement

 - user registration, log in/log out
 - user feedback - recipe social media connection with likes, up-votes
 - user video uploads or youtube links to show how to make the recipe
 - on a bigger scale, the site could be sectioned in terms of starters, mains, desserts - this would only be worthwhile if there was a large enough database and user following
 
 
# Technologies Used

 - [HTML 5](https://html.spec.whatwg.org/)
 - [CSS 3](https://www.w3.org/Style/CSS/)
 - [Bootstrap 4](https://getbootstrap.com/)
 - [Javascript](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
 - [Font Awesome](https://fontawesome.com/)
 - [Google Fonts](https://fonts.google.com/)
 - [Python](https://www.python.org/)
 - [Flask](http://flask.palletsprojects.com/en/1.1.x/)
 -  [MongoDB](https://www.mongodb.com/)

 # Testing
 
  - Manuel testing was performed through out project development and regulary git commited.  The testing was based on the user stories
  - Project initialised with basic requirements added and deployed to heroku.
  - Development flowed from creating basic recipe cards, image banner, creating MDB schema, creating the_recipe view page, adding create recipe and update recipes features, delete page and search fields.
  - Throughout testing - the project was testing that the styling was mobile first responsive.
  - Test investigations: deciding on how best to work with the wireframe designs and image appearance so that they maintained consistant style appearance in all screen sizes.
 - Test investigations: User forms - upon testing - required fields were added to ensure that some content is added to a form field to prevent recipes being created that were empty.
 - Test investigations: add bootstrap styling to user forms to show positive/negative feedback.
 - Test investigations - how to render a image to the site if non added (this is a optinal user choice) - default image added, however, issues arose if the user entered a bad URL address.  The input fields were set to look for correct URL input, but this can still break if a bad URL.  Therefore, onerror functionality added to spot bad URL and load default image.
 - Test investigations - when searching for title names/tags - if the user entered a title with mixed small and upper case values - the search paramater would not find this object_id - therefore JS functionality added to accept form input as lower case only on search fields that were to be searchable.
 
 ### Test 1 (Full site user test)

 - On page load - does the site look good, appealing, exciting and clean?  Does it describe or show its purpose?  Is it easy to navigate?  Is the content easy for the user to read?  
 
 ### Test 2 (Full site user test)

 - when navigating to the recipes.html page do the recipes cards look clean and organised?  Do the images render consistantly in all screen sizes?  When updating or creating recipes, is the information consistant, does it include user feedback information with flash messaging, input field success/danger, and can the user be prevented from adding a image which cannot be rendered to the site.
 
 ### Test 3 (Full site user test)

 - do all search fields work correctly?
  
 ### Test 4 (Full site user test)

 - is the site consistant in its color scheme?  Does the site contain good images which makes the site purposeful and interesting?  Is the site easy to navigate?  Can the user break the code?  Are there any known erros? Does it feel nce to use this application?





# Deployment

There is no difference from the deployed project from the developed project.

#### Project set-up
Install flask web development

```sh
 sudo pip3 install flask
```

Install the dependencies

```sh
 pip3 freeze --local > requirements.txt
```
In requirements.txt file > flask, jinja, MarkupSafe, Werkzeug, Click, itsdangerous

Create procfile
```sh
 echo web: python > Procfile 
```

Project creation in Heroku, named cookbook-mp3 and then deployed

 ##### Heroku Config Apps
  - IP - 0.0.0.0
  - PORT - 5000
 
```sh
git init
git add
git commit -m 
heroku git: remote -a cookbook-mp3
git push heroku master
heroku ps:scale web=1
```
#### In production

 ##### Heroku Config Apps
  - added MONOG_URI password
  
```sh
sudo snap install heroku --classic
heroko login --interactive
git add .
git commit -m
git push heroku master
```

# Credits

- Code Institute - learning tools from Data Centric Development
- [Pretty Printed](https://prettyprinted.com/)
- [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
- Code Institute Slack Community - i recieved alot of support from the slack community members who helped with looking at search functionality and dano5342 whose project had the pagination that i used for this project
- Stack Overflow


# Media
 - Most images were sourced from
- [Unsplash](https://unsplash.com/) 
- other from google search engine

# Acknowledgments

 - Whilst planning this project, i was inspired by this food recipe website - [Gila Gris](https://gillagris.se/recept/?os=pasta&gclid=Cj0KCQiAxfzvBRCZARIsAGA7YMwRhHZdwLSkg9i2k6ri8v5qnYR6SoHkv4ngrMqX0Np2Ad8EK_ToPr0aAicxEALw_wcB), which i found from this google search - [My Cook Book Online](https://www.mycookbook-online.net/search/) 
 - Thanks to the Code Institute Slack Community for providing various information about solving issues with python and flask web development.  As mentioned, the code for the recipe pagination came from dano5342.
