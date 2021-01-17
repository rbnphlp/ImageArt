

# Web app to  build,sell & buy  paintings using Style transfer

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
    


> ![](https://github.com/rbnphlp/ImageArt/blob/master/media/home_images/DBDesign.png)	




## Design 


The Web-Pages are designed  to make it users to shop and create new paintings very accessible ( albeit for limited images sizes)


+ Features Added: 
    - Allow Users to purchase  paintings with specific frames and sizes
    - Allow Users to  create their own painting
    - Allow users how each painting is created by tiling uploaded style and content images , offering inspiration to create new paintings
    - Allow Users to  create and then view the corresponding painting
    - Allows users to create and then sell it on the website
    - Allow users to sort and select categories of various paintings
    - Allow users to search for paintings they are intrested in 
    - Allow users to have their own USer profiles with their Order History
    
    

+ Features Not Implemented or nice to Haves :
    - Pagination 
    - A comment section
    - A Rating section




## Technologies :


### Languages:

+ HTML
+ CSS
+ Javascript
+ Python (Django)
+ PosgresSQL

    
### Libraries /Frameworks:
+ Jquery


### External API's
+ deepai.org


  
## Testing :



+ Header & Navigation bar :
     - Href links to correct elements -checked and working
     - Nav Bar correcly alligned for Desktop Version only ! 
     - NAv bar side display added for Mobile Version
     


+ Body  :
     - Loaded Pages in  (Safari,Firefox and Chrome)
     - Works well in Desktop versions + Mobile views
     - Forms render well in all views 
     
     
           
     
+ Full web page checks : 
     - Tested all of the above on desktop (firefox and chrome) and mobile (iphone 6+)

+ API requests :
    - Tested API calls on large and small Image sizes 
    - Limited to 5000 calls in total
     
### Bug Fixes (Open & Closed) :


* Cannot add paitings with different frames 
* Check out painitings from home page not returning tags  when  and search bar

| Bug-Location      | Bug-Type  | Solution| Bug-Status|
| ------------- |:-------------:| ---------:| ---------:|
|  Stripe Payments   | Prices with smaller than $.50 returns error from stripe | Add $1 to prices smaller than $1 and fix the corresponding bag to show $0.00 in jinja | Fixed |
|  Index.html  |  search query   |Change url link with corresponding search terms to return entire categories| Fixed |
|  Index html |   Html-validation errors|  NA| Open|
|  R14 error Heroku | App would  close after  afew seconds due to Image processing script taking up too much memory  |  Had to exclude all the image processing scripts and Used an external API| Fixed|


## Deployment

The Web pages was deployed through following :
+  Setting up a heroku app with login.
+ adding files through git remote 
+ made sure all keys + access keys were deleted and any accidentally uplodaded keys were rotated to new ones .All config variables were set to enviornment variables using Heroku set CLI and using a pylib dot env to read the env variables.
+ Set up Postgres Database 
+ Install requirements .txt  
+ Build process through git remote heroku and push





## Acknowledgements
 Thanks for Code institute and their awesome tutor support team :)
 



