# M Beauty
M Beauty is a B2C nail and beauty business located in Killarney. This business was stated up in 2020, and is a one woman operation that is very busy and this website should help with the day to day operations, being notified when a user makes a booking. 

# UX

## Strategy 

This website was designed and implemented with Django, Python, HTML, and CSS.
It aims to provide an easy-to-use interface where customers can browse through the skincare products, or can choose a service provided and make a booking.
The site offers an inbuilt stock system to ensure users cannot buy things that are not currently in stock. Once signed in, users can save an address to their profile for easy and convenient checkout. Once a user makes a booking they can check the time and date of the booking once the user is signed through a view bookings link and can also cancel a booking.

## User Stories

### Epic 1 - Registration and User Accounts

- As a Site User I want to be able to register for an account so that I can save my personal details.
- As a Site User I want to be able to easily login or logout at any time so that I can access my personal account information on different devices.
- As a Site User I want to be able to recover my password so that I can regain access to my account in the event I lose my password.

### Epic 2 - User Booking

- As a site user I want to be able to create a user account so that I can login to make a booking.
- As a site user I want to be able to view my bookings from my account so that I have proof that the booking was made.
- As a site user I want to be able to cancel my bookings from my account so that I can free up my appointment slot for somebody else.


### Epic 3 - User Products

- As a site user I want to view a list of clearly defined products so that I can browse freely.
- As a site user I want to view individual product details so that I can get the full description, choose the quantity and add to cart.
- As a site user I want to be able to see my shopping cart once I add a product to the cart for ease of navigation.


### Epic 4 - Site Navigation

- As a site user I want to be able to view a site which is attractive yet informative so that I can gain an understanding of the sites purpose and navigation easily.
- As a site user I want to be able to view salon service and price details so that I can clearly see what the salon can offer and the cost.
- As a site user I want to be able to view a gallery of examples of past work completed so I can see the level of skill of the beautition.


### Epic 5 - Admin

- As admin I want to be able to read, add, edit and delete products from the front end in the website.
- As admin I want to be able to read, add and cancel bookings from the front end in the website.
- As admin I want to be able to see, add, update and delete services from the front end in the website



## Features

### Nav bar

The nav bar is the core navigation for the site. It differs slightly from mobile to desktop; however, both include all the same components.
It consists of several integral links to allow the user ease of navigation.

- The logo on the left, witch is Martas brand logo is featuired throughout the site also doubles as a return to home button.



- Gallery, witch takes you to a dedicated page of Martas best work.

- Products, brings you to beauty related products.

- Price List, witch takes you to a dedicated page of Martas prices and deals.

- Services, where the user chooses a service to make a booking.


- Account, is a dropdown menu witch changes based on if you are logged in or not. If the user is not logged in there are two options in the dropdown, witch are 'login' or 'register'. If the user is logged in there is three options in the dropdown menu; 'Product management', 'My profile' and 'logout'

. When logged in as admin the Product management takes you to the product management page, witch is an add product page





- Shopping bag, is in the form of the icon representing the bag total and is a link to take you to the bag once ready to checkout with a product or a booking deposit.





 ### Footer

The footer is divided into three sections
- Contact details, with Martas work adderss and work mobile number.
- Social media, there is a link to Martas instagram and facebook accounts for her m_beauty business.
- Opening hours of the salon.



### The Home Page

- Carousel
The background on the home page is designed around M_beauty logo, and the first section of the home page is a carousel. The first image in the carousel is martas logo so when the user first visits the page they are greeted with the illusion of a cohesive full image but the carousel changes photos to three more images of some of martas work, but the theme stays the same through out the site.


- The Price List
An integral part of any competitive beauty is keeping your clients and future clients informed of your current rates. For this reason I thought it was important enough to dedicate it a portion of the homepage. The price list carries a similar theme to the homepage so it is not a visual problem. 


- Services
The services are in another carousel. Instead of listing all or any services I thought it would be more visually appealing and save space on the homepage as it has a dedicated page where they are located.


### Gallery 

This is a simple gallery page that showcases some of Martas best work. Most of the images are the same as on the social media, but this gives the option for quick access for any user or a chance for the possibility of an older client who dose not have social media to see examples of previous clients.



### Products

The products page offers to showcase the beauty products offered by M Beauty witch are all handcreams, and a few gift set.
A product is made up of the product image, the price and the stock level. 
Once a product is clicked you are redirected to the product detail page.


## Product Detail

On the product detail page you have a full size image on the left of the screen and on th right of it is product title, the price, the product description and a wiget to choose the quantity. 
Below that is two buttons; Keep shopping, which takes you back to the products page. The other button is Add to cart which once clicked it triggers a small bag summary in the right of the screen and this button also triggers the bag icon to update with the price of the bag.

For admin there is also an edit and a delete button.

- The edit button takes you to the product management page where the item is filled out waiting to edit.

- The delete button, brings you tp the products delete page witch is just gives you the option to delete or to cancel. If cancel is selected you are redirected back to the product detail page.
If delete is selected the product is deleted and you are redirected to the products page.



### Price List

The price list is something a user is likley to want to see upon visiting thee site, and is such an important part of the business and it is nice for the user to have access from any page as its on the navbar. The price list is a similar theme to the background so the price list page looks visually appealing.


### Services

The services page provides the range of services that are offered. Each service has an image relating to the service, has a brief summary of each of the services and the price of the service.
Below is a 'Book now' button that is a link to the bookings page where a user can make the booking but the user must be logged in to be able to view that page.
If user is admin there is full crud capabilities.
- Add service
    The add service button is located at the top of the page. This brings me to the add service form page.
    This form has five input fields - service name, service type, descrioption, price and image.
    This allows admin ease of adding a new booking from the website.

    



### Bookings.

Once a user has logged in they are taken frpm the services page to the the bookings page. The user is greeted with your username and is informed how to make your booking, that you have the ability to to view your upcoming and past bookings and that you have the ability to cancel upcoming bookings.
There are two buttons on the bookings page:

#### View bookings

- view bookings, which opens up a hidden dropdown of a list that is broken into:
 - client, which displays the first and last name of the name provided in the bookings form.
 - service, which displays the service selected in the bookings form.
 - appiontment, which displays the date and the time of appointment.
 - cancel, which gives the user, and admin the ability to cancel appointment as long as the date has not passed.


#### Make booking

The make booking form has five input fields for a site user. First and last name, the date, the time and the service. 
If logged in as admin there is another field of user. 
If confirm is clicked, the booking is saved, the user is brought back to the bookings page, where the user can view the booking to view the booking details. 
Also a success message of "added booking deposit to your bag" and you have the bag summary attacthed to it in the top right corner of the screen, with a link to go to secure checkout for ease of navigation for the user.


