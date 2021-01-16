

# Web app to  build ,  sell & buy  your paintings

The project as part of Module4:Code Institute  .


Frameworks used including Django and PosgresSQL  s3 and heroku.


----------------------------------
         



## User Stories for building the app : 


### Viewing and Navigation

| UserStoryID      | As a | I want to be able to |So that I can|Implemented|
| ------------- |:-------------:| ---------:|---------------:| ------------:|
| 1  |  Shopper| See a list of Paintings| Select some to purchase|  Yes|
|  2 | Shopper| View Indivudual Painting details   |  Identify Painting Details , Price and framing options | Yes|
|  3 | Shopper| View Shopping Basket   |  Identify Shopping details and price costs at any time during purchase |Yes|
| 4 | Shopper| View new paintings  created by user image and style preferences | to create photo art from image|Yes|

### Registration and User Stories

| UserStoryID      | As a | I want to be able to |So that I can|Implemented|
| ------------- |:-------------:| ---------:|---------------:| ------------:|
| 5 |  SiteUser|Easily Register for an account| Have a personal account and be able to view my profile|Yes|
|  6 | SiteUser| Easily logon or logout|  Access my Personal account information |Yes|
|  7 | Shopper| Easily recover my password   |  Recover access to my account|Yes|
| 8 | Shopper|Have a personalised user profile| View my Personal order History , order confirmation and save my payment information|Yes|




### Searching

| UserStoryID      | As a | I want to be able to |So that I can|Implemented|
| ------------- |:-------------:| ---------:|---------------:|------------:|
| 9 |  Shopper|Search for a painting by Name and description| Find a specific Painting I had like to Purchase|Yes|
|  10 |Shopper| Easily see what I have searched for | quickly decide whether the painting was available |Yes|
|  11| Shopper| Easily recover my password   |  Recover access to my account|Yes|
| 12 | Shopper|Sort paintings in each category| Easily identify products|Yes|





### Purchasing and Checkout

| UserStoryID      | As a | I want to be able to |So that I can|Implemented|
| ------------- |:-------------:| ---------:|---------------:|------------:|
| 13 |  Shopper|Easily select the type of frame , size and quantity of a painting when purchasing it | easily get the right painting|Yes|
|  14 |Shopper| view items in my bag to be purchased| Identify quantity and price of items being purchased|Yes|
|  15| Shopper| Easily enter my payment information   |  checkout quicky|Yes|
| 16 |Shopper| View order confirmation after checkout| Verify that havent made any mistakes|Yes|


###  Admin and Store Management

| UserStoryID      | As a | I want to be able to |So that I can|Implemented|
| ------------- |:-------------:| ---------:|---------------:|------------:|
| 17 |  Shopper|Add /Sell a Painting on Site | So I can earn money on site|Yes|
|  18 |Shopper| Edit/update a painting|Change Painting details|Yes|
|  19| Shopper| Remove Paintings  | So i can painting no longer on sale|Yes|
|  20| Shopper|Sell a Painting on Site    |earn money |No|




## UX Design 

+ The Skeleton Layout:


    - A HomePage : Page explaining User needs and Web app Goals  
    - Gallery: Page to display Paintings along with a Title , likes & No of Images uploaded  with search and sorting options
    - View Painting: Page to display a single Paintings in a User chosen Frame  and option to save the shopping bag 
    - Create  : A form page which allows users to create new paintings and allow users to either save it to the Gallery or simply view the painting
    - Shopping bag : A page which allows users to view theur shopping products
    - Subsuquent Edit and Delete Pages from the above
    - Sign In / Create Account : Allow users to sign-up or login in to the website information
    - Order History: Allow users to view their previous Order History
    - Payment Form : Which Allows users to pay for their items in the shopping bag
    
Initial wireframe used for developing a prototype :

> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/wireframe1.png)	
> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/wireframe2.png)	
> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/wireframe3.png)	
> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/wireframe4.png)	
> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/wireframe5.png)	


## DB Design 

+  Postgres SQL were designed as Follows :
    - Category Table which contains various categories for the paintings:
   
     
    - Painting Table which contains uploaded images ,created paintings , user choices etc regarding painitings:
        
    -  Order Table which contains Info regarding order , delivery info etc .
    - User Profile table  which contants info about user 

A full schema of the table is as follows :
    


> ![](https://github.com/rbnphlp/HolidayStories/blob/master/Screenshot%20from%202020-08-23%2017-40-51.png)	




## Design 


The Web-Pages are designed to make easy  add and share holiday memories and Images with little effort.


+ Features Added: 
    - Allow Users Add Holidays with a Title & Destination 
    - Allow Users to Add Memories for Each holidays
    - Allow Users to Add Images for each Memory along with short , titles and descriptions
    - Allows users to edit and Delete Memories 
    - Allow users to delete Holidays from Mongo-db
    - Allow users to up-vote Holidays they are intrested in
    

+ Features Not Implemented or nice to Haves :
    - Pagination 
    - Search bar based on Country,Date etc
    - USer profiles
    - A comment section
    - Long titles and description can break up the container grid and hence need to povide a maximum in the form fields




## Technologies :


### Languages:

+ HTML
+ CSS
+ Javascript
+ Python (Flask , boto3, jinja, json)
+ Mongo-db
    
### Libraries /Frameworks:
+ Materialise
+ Jquery
+ MaterialIcons

  
## Testing :



+ Header & Navigation bar :
     - Href links to correct elements -checked and working
     - Nav Bar correcly alligned for Desktop Version only ! 
     - NAv bar side display added for Mobile Version
     


+ Body  :
     - Loaded Holidays Page in  (Safari,Firefox and Chrome)
     - Works well in Desktop versions , Allignment issues when Title is long in Holidays Page for Laptop + Mobile views
     - Memories Page compatible in all views , however carousel is sometime non-responsive  on mobile versions
     - Forms render well in all views , buttons however too big fo mobile view.
     
+
            
     
+ Full web page checks : 
     - Tested all of the above on desktop (firefox and chrome) - *Other Screen sizes not implemented*
     - Ran the web page for any html/css errors on https://validator.w3.org/ - issues with closing a tags

     
### Bug Fixes (Open & Closed) :


| Bug-Location      | Bug-Type  | Bug-Status|
| ------------- |:-------------:| ---------:|
|  view_jolidays.html   |  html-validation error | Fixed |
|  view_memories.html   |  html-validation error   |  Fixed |
|  Various routes in Flask (Add_memories )|   logic |  Fixed |
|   css &html |   Resposniveness - Carousel sometimes not responsive on mobile  |  Open |

## Deployment

The Web pages was deployed through following :
+  Setting up a heroku app with login.
+ adding files through git remote 
+ made sure all keys + access keys were deleted and any accidentally uplodaded keys were rotated to new ones .All config variables were set to enviornment variables using Heroku set CLI and using a pylib dot env to read the env variables.
+ Build process through git remote heroku and push





## Acknowledgements
 Thanks for Code institute and their awesome tutor support team along with my mentor :)
 




## Image Art User-Stories




