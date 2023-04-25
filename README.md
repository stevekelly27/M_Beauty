# M Beauty
M Beauty is a B2C nail and beauty business located in Killarney. This business was stated up in 2020, and is a one woman operation that is very busy and this website should help with the day to day operations, being notified when a user makes a booking. 

![18774EDC-871A-4460-B7CA-DBBE56B14F0E](https://user-images.githubusercontent.com/93382818/225476727-0100785c-0c74-45ca-81aa-f9f44aa4fc1f.jpeg)

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
- As a site user I want to be able to have access to social media accounts relating to the business.


### Epic 5 - Admin

- As admin I want to be able to read, add, edit and delete products from the front end in the website.
- As admin I want to be able to read, add and cancel bookings from the front end in the website.
- As admin I want to be able to see, add, update and delete services from the front end in the website



## Features

### Nav bar

The nav bar is the core navigation for the site. It differs slightly from mobile to desktop; however, both include all the same components.
It consists of several integral links to allow the user ease of navigation.

- The logo on the left, witch is Martas brand logo is featuired throughout the site also doubles as a return to home button.

- Contact, witch takes you to to a page for the contact details for the M Beauty business,
  as when a user is on a small screen the footer which contains the contact deatils is shrunken down to only include M Beauty social links.

- Products, brings you to beauty related products.

- Price List, witch takes you to a dedicated page of Martas prices and deals.

- Services, where the user chooses a service to make a booking.

![092F1ACB-CF23-4D66-8214-A916A7CAF3CA_4_5005_c](https://user-images.githubusercontent.com/93382818/224984301-085458bc-e2cb-4b04-b9ef-47f0bbfd8ca4.jpeg)

- Account,
  The account dropdown menu changes based on if you are logged in or not. 
  If the user is not logged in there are two options in the dropdown, which are 'login' or 'register'. 
  If the user is logged in there are two options in the dropdown, which are 'My profile' and 'Logout

  If the admin is not logged in there are two options in the dropdown, which are 'login' or 'register'.
  If the admin is logged in there are four options in the dropdown menu, which are 'Product management', 'Service management', 'My profile' and 'Logout'

  - Product management
    When logged in as admin the Product management redirects to the add product page.

  - Service management
    When logged in as admin the Product management redirects to the add services page.

![AAA43EC7-1D64-49C7-A736-4698FF5AB9BD_4_5005_c](https://user-images.githubusercontent.com/93382818/224984471-0c94d876-ee0a-49f2-9521-df13dcb3c3af.jpeg)

![71015FA6-0918-4EEE-8106-7B2727FF6BF6_4_5005_c](https://user-images.githubusercontent.com/93382818/224985116-dc493a4c-1021-419c-8715-75f27a132cd0.jpeg)

  - My profile
    My profile takes you to the profile page.
    This page consists of the users/admins delivery details information that get saved when the user completes a purchace and checks out.
    Beneth the saved delivery details is a button to update the information.
    On the right on the page is a history of all previous purchaces.
    Displayed is a table of a list of orders that have been made.
    It is displayed as: 'Order number', 'Date', 'Items' and 'Order total'.
    The Order number doubles as a link to see the full order information.


![757531F7-B757-492E-AB75-87A0075FB7DC](https://user-images.githubusercontent.com/93382818/224985938-ec459d26-a870-42bd-8a9e-5a78e1840afb.jpeg)

  - Order Information
    The order information page concists of the full order history, the full delivery details and the billing information.
    Beneth is a button labled 'back to profile' which, brings you back to thhe profile page.
    In the top right of the screen there is an alert notification, detailing that this is a past order,
    the order confirmation number and a confirmation that an email was sent on the order date.


![9C062912-86E8-4FD3-BC0C-AEB70A5CB102](https://user-images.githubusercontent.com/93382818/224986221-5f84ec1d-3e3d-4e32-994a-b592b972939a.jpeg)

- Shopping bag, is in the form of a font awesome icon representing the bag total and is a link to take you to the bag once ready to checkout with a product or a booking deposit.


![BB814889-D88C-4A92-89DD-FC5222C9516D](https://user-images.githubusercontent.com/93382818/224986499-7edda0b0-3b6a-4a0f-b4d9-312f7f8cd85f.jpeg)


 ### Footer

The footer is divided into three sections, but the footer shrinks down to just the middle section with the social media links.
The three sections are
- Contact details, with Martas work adderss and work mobile number.
- Social media, there is a link to Martas instagram and facebook accounts for her m_beauty business.
- Opening hours of the salon.

![127D4FFC-3219-44B3-B362-505BC3FFA26D_4_5005_c](https://user-images.githubusercontent.com/93382818/224987006-e7b8fb67-428b-4918-8f3f-fb426890c9c6.jpeg)

![93E7B6FD-FA03-445E-9E88-AFDBED000A43_4_5005_c](https://user-images.githubusercontent.com/93382818/224987075-2d2f9b5a-5715-49af-aca5-054295a61907.jpeg)


### The Home Page

- Carousel
The background on the home page is designed around M_beauty logo, and the first section of the home page is a carousel. The first image in the carousel is martas logo so when the user first visits the page they are greeted with the illusion of a cohesive full image but the carousel changes photos to three more images of some of martas work, but the theme stays the same through out the site.
This carousel is not visible on small screens.

![97533761-861F-472F-818A-9E1A85CDBBEA](https://user-images.githubusercontent.com/93382818/224987350-2a3db7a4-1be5-407a-8884-782c2b3a697e.jpeg)



- Services
The services are listed in cards which provide a short descrpion of each service and a link that takes you to the booking page. 


![621683C3-A051-43F5-8021-BEB205DFC2CD](https://user-images.githubusercontent.com/93382818/224988899-a65c612b-8ea6-4cef-9cbf-690b34e91308.jpeg)


- The Price List
An integral part of any competitive beauty is keeping your clients and future clients informed of your current rates. For this reason I thought it was important enough to dedicate it a portion of the homepage. The price list carries a similar theme to the homepage so it is not a visual problem. 


### Contact

The contact page is just the contact information and opening hours as when the footer is on a mobile view the contact information and oprning hours do not display.



### Products

The products page offers to showcase the beauty products offered by M Beauty witch are all handcreams, and a few gift set.
A product is made up of the product image, the price and the stock level. 
Once a product is clicked you are redirected to the product detail page.


![5CA81BF2-0277-4FE6-A866-B6FEB72F7C5C](https://user-images.githubusercontent.com/93382818/224989232-78e9c1b0-9248-4e7b-8908-0393d400443c.jpeg)


## Product Detail

On the product detail page you have a full size image on the left of the screen and on th right of it is product title, the price, the product description and a wiget to choose the increment or decrement the quantity. 
Below that is two buttons; Keep shopping, which takes you back to the products page. The other button is Add to cart which once clicked it triggers a small bag summary in the right of the screen and this button also triggers the bag icon to update with the price of the bag.

![1D27942C-1F0B-4977-BFD3-10EA0B56D07E](https://user-images.githubusercontent.com/93382818/224989612-c12b000a-bede-428f-a81f-82e17dd6b82f.jpeg)


For admin there is also an edit and a delete button.

- The edit button takes you to the product management page where the item is filled out waiting to edit.

![EC4057FB-30BF-42ED-AF9A-C4B7F07862D4](https://user-images.githubusercontent.com/93382818/224989971-5ef03f55-37ed-46c0-82d3-f2667f864a36.jpeg)

- The delete button, if delete is selected the product is deleted and you are redirected to the products page.

### Price List

The price list is something a user is likley to want to see upon visiting thee site, and is such an important part of the business and it is nice for the user to have access from any page as its on the navbar. The price list is a similar theme to the background so the price list page looks visually appealing.

![5EEE0533-66B4-413D-AFE0-E6D79B8D81D6](https://user-images.githubusercontent.com/93382818/225218016-98d7b78b-620d-4094-bf3c-30d39f628a46.jpeg)

### Services

The services page provides the range of services that are offered. Each service has an image relating to the service, has a brief summary of each of the services and the price of the service.
Below is a 'Book now' button that is a link to the bookings page where a user can make the booking but the user must be logged in to be able to view that page.
If user is admin there is full crud capabilities.

![59F6017D-A2EF-49B1-99AD-BF84D854D6E4](https://user-images.githubusercontent.com/93382818/225224390-fbc9144a-c28f-49e5-8175-58fd87230433.jpeg)

- Add service
    The add service button is located at the top of the page. This brings admin to the add service form page.
    This form has five input fields - service name, service type, descrioption, price and image.
    This allows admin ease of adding a new booking from the website.
    All fields are required except for the image field.
    If a field is missing or incorrectly filled out, they are notified by a pop-up message.
    There is two buttons at the bottom of the form:
    Confirm saves the form and adds the service to the services page.
    Cancel redirects back to the services page.


![7B172215-758B-4CA1-BA0F-9856A716377A](https://user-images.githubusercontent.com/93382818/225224788-e00c2975-76ea-4fac-a959-7a178b9241ef.jpeg)


- Edit service
    The edit button is located on each of the services. This brings admin to the edit service page.
    This page is a pre-populated form with the same fields as the add service pag.
    If a field is missing or incorrectly filled out, they are notified by a pop-up message.


![9384E8E5-64F3-4C35-B444-33FFF6D64FAD](https://user-images.githubusercontent.com/93382818/225224492-227f1969-ee99-493b-80e2-f2b3a9658045.jpeg)

- Delete service
    The delete button is located alongside the edit button, and brings. admin to the delete service page.
    A question is promped asking you if you are sure you want to delete (service name)
    There are two buttons beneth this; yes and no.
    Yes deletes the service and redirects back to the services page.
    No just redirects again back to the services page.    


![307F2258-85BC-41FA-88C9-D05BF5F041B2_4_5005_c](https://user-images.githubusercontent.com/93382818/225224572-4507c348-e08f-4985-a5fd-27b570b4a051.jpeg)


### Bookings.

The booking system in this website is to book a timeslot and if the booking from is valid and the timeslot is avalable the booking will be saved. A site user will be directed to the checkout and pay a booking deposit fee of €5. If admin makes the booking the booking will be saved to the view booings table.

#### Bookings page

Once a user has logged in they are taken frpm the services page to the the bookings page. The user is greeted with your username and is informed how to make your booking, that you have the ability to to view your upcoming and past bookings and that you have the ability to cancel upcoming bookings.

![C0071574-5695-45F9-ABAD-E02BA92BE1A2](https://user-images.githubusercontent.com/93382818/225227142-2f7d4106-1621-4b32-9157-c18c529b743d.jpeg)

#### View bookings

- view bookings, which opens up a hidden dropdown of a list that is broken into:
 - client, which displays the first and last name of the name provided in the bookings form.
 - service, which displays the service selected in the bookings form.
 - appiontment, which displays the date and the time of appointment.
 - cancel, which gives the user, and admin the ability to cancel appointment as long as the date has not passed.


![BD8AB22F-4739-4ABB-9B98-741CCE4859EA](https://user-images.githubusercontent.com/93382818/225227381-f5d79d44-b56b-49e5-acbc-f6971af4f873.jpeg)

#### Make booking

The make booking form is for a user or admin the ability to book a timeslot with Marta.
The make booking form has five input fields for a site user. First and last name, the date, the time and the service. 
If logged in as admin there is another field of user. 
There are two buttons on the bottom of the form. Confirm and cancel.
If confirm is clicked, the booking is saved, the user is brought back to the bookings page, where the user can view the booking to view the booking details. 
Also a success message of "added booking deposit to your bag" and you have the bag summary attched to it in the top right corner of the screen, with a link to go to secure checkout for ease of navigation for the user.
If cancel is selected the user is redirected back to the bookings page.

![B2931672-53E6-4E80-A412-9D8C3E65AA0C](https://user-images.githubusercontent.com/93382818/225227714-c0c37529-5970-4b34-bf3c-92571267642c.jpeg)


#### Cancel booking

From the view bookings table if cancel is selected you are directed to the cancel bookings page where you are given the opertunity to return to the bookings page if clicked accidentally or to confirm cancellation.
You are also shown the dtae and time of the booking in question.

![5FEEE34F-EA4E-4AD4-9147-079333D82C9E](https://user-images.githubusercontent.com/93382818/225228374-b5e6cccb-1433-4825-8208-249f4090d2b8.jpeg)

### Shopping Bag 

If a product or booking is in the shopping bag the user has a clear image of the item, the name, the price,
the ability to increment or decrement the order and the subtotal.
Two buttons are located under the order on medium and large screens and the buttons appear on top od the order on small screens.
There is a keep shopping button that redirects to the products page, and secure checkout button that brings you to the checkout page.


![EE955930-77FC-4DB5-B56D-CCD98A8EAB11](https://user-images.githubusercontent.com/93382818/225229510-acd05d5e-5c73-4680-90b2-f99ceaef9bd6.jpeg)

### Checkout

The checkout page has a form for the users details, shipping adderss and card details.
This is where the users info will get saved and be added to the details in my profile.
The card element is injected by the stripe API and uses a payment system that is fully PCI compliant.
The same API also handles any errors using the allocated div to display them to the user.
When the form has been submitted, the pay now button converts into a spinner and displays an overlay to show it is processing using a js function.
On the right of the screen the user has a summary of their order and a grand total.


![36EFABA5-76D7-4BA7-9BAA-02DC153A94D8](https://user-images.githubusercontent.com/93382818/225243719-f8de8a76-6d73-4c7b-843b-e6fbab85ec49.jpeg)

![5D123F74-0694-4C6F-940F-62A969F2A05E](https://user-images.githubusercontent.com/93382818/225243814-43a43d43-76f3-4315-815d-2bb70fbe57d1.jpeg)

### Checkout success

The checkout success page starts with a thank you to the customer for their order.
it contains all the information passed in from the checkout form.
A success message appears in the top right of the screen confirming that the order was successfully processed, and that an email will be sent to the one provided.


![7F576940-35B2-497C-9F1B-7E592B7AFAB3](https://user-images.githubusercontent.com/93382818/225243892-14546b70-f4cd-4559-93d7-43813deb8de3.jpeg)


### Authentication

All authentication templates are from the all-auth library

- Register

![A89505B0-7C16-4EF6-8FFD-3CD642E0556D](https://user-images.githubusercontent.com/93382818/225245729-4aa848bd-b5b9-49a8-8cf0-8cdde2d14c89.jpeg)

- Login

![C3945EBF-5248-4663-8770-10C31CFCDED6](https://user-images.githubusercontent.com/93382818/225245828-7955be77-7971-468d-a6f7-46ac3d01ffbf.jpeg)

- Logout 

![ACACC1DD-4884-4A86-9527-2F2BBDEF947B_4_5005_c](https://user-images.githubusercontent.com/93382818/225245908-4c97aa49-e8bb-47b3-b8ed-2ddfdc2d7c5a.jpeg)

## Future Features 

- The contact page
Due to time constraints I have not made the contact page.
All informaation about the business is in the social media accounts, including the contact details and opening hours.
It is disabled at the moment.

- Stripe payments
Stripe payments are still example payments, I will make it a future to be able to make real payments.

- BookingFormAdmin
I would like to on forms.py insert the paid field for admin to have control access on the frontend.

- OrderLineItem
I would like to implement a model to override save function to adjust post-order

- Webhook handler
A payment intent succeeded function to submit email confs.



## Wireframes

- Homepage

![1B76A93E-CB61-4E5D-A4DB-D57F00A66F17_1_105_c](https://user-images.githubusercontent.com/93382818/233998788-7131d965-20d1-4e8a-9b69-4362c45e7dc1.jpeg)

- Products page

![4E63C4FE-F8E5-4067-ACBA-4F082CEA3058_1_105_c](https://user-images.githubusercontent.com/93382818/233999044-95ae960b-919b-4d6c-b7ef-1edecacecb85.jpeg)

- Services page

![DDF482CC-CC5A-441C-918D-0CCF691058D7_1_105_c](https://user-images.githubusercontent.com/93382818/233999142-00228dd8-ea0c-4a93-8fc1-03972479c907.jpeg)

- Booking page

![B489DAD7-C089-40B5-8012-F5BFC53AD0E6_1_105_c](https://user-images.githubusercontent.com/93382818/233999526-e04a15f8-6f87-4258-8315-614404b54d50.jpeg)

- Booking form

![84707839-E7EE-48E0-82D7-031478F10219_1_105_c](https://user-images.githubusercontent.com/93382818/233999611-1ec71bd3-a577-41c2-aa92-e368d685405a.jpeg)

- Sign up page

![18B675B1-4516-4F74-8192-A4FFD99A8718_1_105_c](https://user-images.githubusercontent.com/93382818/233999984-2f88a4a8-1b33-43d0-896d-aa1ab97c349e.jpeg)

- Login page

![9AF49696-E5B4-4EAB-84D5-3F0A68C44B57_1_105_c](https://user-images.githubusercontent.com/93382818/234000067-9078d6c2-926c-4dcc-bba7-b0257b419d81.jpeg)


## Bugs/Fixes

## Testing

###  Testing User stories


Epic 1 - Registration and User Accounts

User Story 1a - Registration

As a Site User I want to be able to register for an account so that I can save my personal details.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|To register, a user must enter an email address , a username and a password|Enter an email adderss, username and password|User is logged in|Pass                                     |
|A user should not be able to login unless they have completed the registration|Try to login to an unregistered account|Access to site is denied|Pass|
|A user should not be able to register the same username or email address more than once  |Try to regiter with an email address already in use|Access to site is denied|Fail|
|A confirmation email should arrive on user email address to confirm the registration.|Register and check email.|A verification email|Pass|
|At the email content, a URL link to redirect page on website should appear for user to be registered on db and be able to login|Click the link in the email|The email is verified and the account is saved|Pass|

<br>


User Story 1b - Login/Logout

As a Site User I want to be able to easily login or logout at any time so that I can access my personal account information on different devices.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|The My Account dropdown menu should display if the user is logged in or out by displaying a link to the alternate option.|Once logged in go to My Account|To see logout|Pass|
|The My Account dropdown menu should display a My profile link to access personal information.|Once logged in go to My Account|To see a link to My Profile|Pass|

<br>


User Story 1c - Password Recovery

As a Site User I want to be able to recover my password so that I can regain access to my account in the event I lose my password.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|A "forgot password" link should be available to the user on the log in screen|Go to the login page|Under the login area there should be a link for 'Forgot password?'|Pass|
|The user should be prompted to enter an email address when they click on the forgot password link.|Click the link on the login page for 'Forgot Password?'|The user is redirected to the forgot password page and it requires an email address|Pass|
|An email will be sent to the entered email address providing the user with a link to use to reset their password.|Enter the email address provided for registration|An email should be sent to the registered email address with a link to reset password|Pass|

<br>



Epic 2 - User Booking
User Story 2a - Booking Accessibility 

As a site user I want to be able to create a user account so that I can login to make a booking.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|A user must be logged in to make a booking.|Try to click the book now link on a service|The user is redirected to the login page|Pass|

<br>

User Story 2b - Booking Verification/Confirmation

As a site user I want to be able to view my bookings from my account so that I have proof that the booking was made.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|The user account is set up so users can view all of their past and upcoming bookings if they are logged into their account.|If the user is logged in visit the bookings page and click view bookings|Allfuture and passed bookings should be available to view|Pass|
|Booking details must include; date, time, and service details.?click the view bookings link on the bookings page|the clients booking should contain the date, time, and service details|Pass

<br>

User Story 2c - Booking Cancellation

As a site user I want to be able to cancel my bookings from my account so that I can free up my appointment slot for somebody else.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|Users can cancel details of an upcoming booking through the click of a "Cancel" button from their user account profile or bookings page.|Click the cancel link|The booking to be deleted|Pass|
|Users are given the option to confirm a deletion before an appointment is deleted.|Click the cancel link|to be taken to the cancel bookings page to confirm cancellation|Pass|
|Users cannot delete a past booking.|Click view booings on the bookings page|If the booking is in the past there is no option to cancel|Pass|

<br>


User Story 3a - Browsing Products

As a site user I want to to view a list of clearly defined products so that I can browse freely.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|A user can clearly see a list of products available for sale.|Go to the products page|To see a list of products available|Pass|
|A stock level should be visible to let the user know if the product is available.|Go to the products page|Under each product should have a stock level|Pass|
|A price should be visible under all products.||Go to the products page|Under each product should have a price|Pass|

<br>


User Story 3b - Product Detail

As a site user I want to view individual product details so that I can get the full description, choose the quantity and add to cart.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|A user should be able to view the view the full product description.|Click on a product|User should be taken to the product detail page and view the full product description|Pass|
|A user should be able to toggle the quantity of the product.|On the product detail page click the + or - to toggle quantity|Quantity should change accordingly|Pass|
|A user should be able to add a product to the cart.|Click add to bag link on product detail page|The item should be added to the cart|Pass|
|A User should not be able to enter more amount than the availability of the product in stock.|Try to increase the quantity to more than is in stock|The quantity should not be able to go higher than what is in stock|Pass|

<br>


User Story 3c - Adding Product to Bag

As a site user I want to be able to see my shopping cart once I add a product to the cart for ease of navigation.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|As a user adds a product to the cart, a pop-up of the users bag should appear in the top right corner.|Click add to bag link on product detail page|A pop-up of the cary summary to appear|Pass|
|there must be a button/link to take the user to secure checkout.|Click add to bag link on product detail page|On the pop up tere should be a link to go to secure checkout|Pass|

<br>


User Story 4a - Linked Social Media

As a site user I want to be able to have access to social media accounts relating to the business.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|The user should have access to linked social media accounts from all pages and on all screen sizes.|Go to all pages on the site|To see the social media links in the footer of all pages.|Pass|
|The user dose not have to be logged in to view the social media pages.|As a logged out user click on the social media links|The user should be taken to the business social media|Pass|

<br>


User Story 4b - Site Navigation

As a site user I want to be able to view salon service and price details so that I can clearly see what the salon can offer and the cost.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|The user should have information on what services are provided from the home page.|GO to homepage|A list of services offered and prices are avalible|Pass|
|The user should be aware of the pricing and offers from the homepage.|Go to homepage|The pricelist is avalible from the homepage|Pass|

<br>

User Story 4c - Site Layout

As a site user I want to be able to view a site which is attractive yet informative so that I can gain an understanding of the sites purpose and navigation easily.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|There should be clear links to all pages of the site from the home page.|Go to homepage|There should be links for products, services and the pricelist in trhe headder|Pass|
|The user should have information of what the site is about and where to find more information, ie; social media links.|

<br>


User Story 5a - Admin C.R.U.D Products

As admin I want to be able to read, add, edit and delete products from the front end in the website.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|A link to add a product is only visible to admin users on the products page.|Go to the products page|There should be a link to add a product only visible to admin which redirects you to the add prodct form|Pass|
|A link to edit a product is only visible to admin users on the product detail page.|Go to the product detail page and click edit link|The edit link takes you to the pre-filled form of the product|Pass|
|A link to delete a product is only visible to admin users on the product detail page.|Go to the product detail page and click the delete link|There should be a delete link that will take you to the delete page to comfirm deletion and deletes product if confirmed|Pass|

<br>


User Story 5b - Admin C.R.U.D Bookings

As admin I want to be able to read, add and cancel bookings from the front end in the website.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|Admin users should be able to use the booking form to add a booking|Logged in as admin make a booking|The booking is confirmed and added to the view bookings list|Pass|
|Admin users should be able to cancel any upcoming booking from the booking page for any client.|Logged in as admin go to the view bookings and cancel an upcoming booking for a different user|Booking should be cancelled|Pass|


<br>


User Story 5c - Admin C.R.U.D Services

As admin I want to be able to see, add, update and delete services from the front end in the website
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|Admin users should be able to add a new service to the services page.|Logged in as admin go to the services page and click add service|Admin is redirected to the add service form which creates a new service|Pass|
|Admin users should be able to update any service in the services page.|Logged in as admin go to the services page and click update|Admin should be redirected to the pre-filled add service form and will update if changed|Pass|
|Admin users should be able to delete any service from the services page.|Logged in as admin go to the services page and click delete|Admin should be redirected to the delete service confirmation page and will delete the service if confirmed|Pass|


<br>



User Story 6a - My Profile

As a site user I want to be able to view my profile so that I can keep update/ save shipping details and previous purchases
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|Once a user buys a product/service the delivery information should be saved to the My Profile page.|As a user purchace a product|The delivery details should be saved to the My Profile page.|Pass|
|A users order history should appear if a product is purchased.|As a user purchace a product|An order history should appear in the My Profile page|Pass|

<br>


User Story 6b - Shopping Bag

As a site user I want to be able to add a product or service to a cart so that I can assess my bag and proceed to checkout.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|A list of any items added to the cart by the user.|Add multiple products and a service in to the shopping bag|There is a list of the products and service containing info, price, quantity and subtotal|Pass|
|A user should be able to update the quantity or delete an item from the cart.|Increase the quantity and update the bag and the subtotal will increase accordingly and if remove is clicked the product/service from the bag|Pass|
|A user should be able to go to secure checkout if happy|Click Secure Checkout in the shopping bag|The user should be redirected to the checkout page.|Pass|
|A User to be able to quickly navigate back to the list of products by having a Keep Shopping button.|Click the Keep Shopping link in the shopping bag|The user is redirected to the products page|Pass|


<br>


User Story 6c - Checkout

As a site user I want to be able to securely checkout so that I can complete my order
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|If a user has delivery info saved it should be pre-filled on checkout|Purchase a product then add another product to the bag and do to the checkout|The users delivery information from the previous purchase is pre-filled.|Pass|
|An order summary showing subtotal, delivery and grand total.|Add multiple products to the bag and go to the checkout.|All of the products should be in a list showing the subtotal and delivery charge and should calculate it into a grand total.|Pass|
|Implement a stripe payment system|Purchase a product or a service|The payment should go through but have webhooks in place on case of unexpected events|Pass|
|A user should be able to get back to the previous page to adjust bag|Go to checkout with a product or service|There should be an link to adjust your bag in case of a mistake|Pass|

<br>


User Story 7a Services

As a site user I want to to view a list of clearly defined services so that I can browse freely.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|A user can clearly see a list of services available.|Go to the services page|A list of the services clearly defined|Pass|
|A price should be visible under all services.|Go to the services page|A price should be clearly defined under each service|Pass|
|A description should be under each service.|Go to the services page|The service should have a brief description of what is entailed|Pass|


<br>


User Story 8a - SEO

As a site user I can find the site through web searches so that I can easily access the site
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
|SEO added through the use of informative alt tags, "description" and "keyword" meta tags in the html|Check HTML for good SEO practice|Informative alt tags for pictures avoiding duplicate content.|Pass|
|SEO added through appropriate site title and home page content|Check HTML for good SEO practice|Including keywords that will help the google algorithm suggest this site|Pass|
|Create a sitemap.xml and robots.txt file|

<br>


User Story 8b - Newsletter
 
As a site user I can subscribe to the newsletter so that I can keep up with news and offers relating to the business.
|Acceptance criteria                |Test Action                           |Expected Outcome                         |Test Outcome                             |
|-----------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------------|
User should be able to enter an email address to sign up to the site newsletter managed via mailchimp|Enter email address|To subscribe to the business mialing list|Fail - working but not functional

<br>


- W3C Markup Validation
Passed HTML validation

- Browser Testing
I have tested that this application worksusing a Macbook Pro, with macOS Ventura version 13.1 installed, using Safari, Google Chrome and Firefox browser


## Deployment

#### GitHub

- Create a new reposiory in GitHub.

- Create a new workspace.

- pip3 install django

- django-admin startproject PROJECT_NAME

- toutch .gitignore

- create superuser

- pip3 install django-allauth

- make driectories for templates, static and media files with mkdir

- python3 manage.py startapp APP_NAME

- pip3 install pillow to install supporting libraries

- pip3 install gunicorn

- pip3 install dj_database_url 

- pip3 install psycopg2

- pip3 freeze > requirements.txt

- python3 manage.py makemigrations 

- python3 manage.py migrate

- python3 manage.py runserver to test server locally

#### Heroku

- Create a new Heroku app by clicking new o thr top right of the screen

- Give the app a unique name

- Select the nearest location

- Add Database to the Heroku app

- Go to seettings and reveal config vars and add SECRET_KEY and paste the value from settings.py in gitpod workspace


#### AWS S3 Bucket

- Create a new S3 bucket by clicking on storage and then S3

- Give the bucket a unique name

- Select nearest location

- Select 'ACLS enabled'

- Unselect 'Block all public access' and tick the axknowledgment that this will make it public

- Open created bucket

- In the S3 bucket properties enable static web hosting

- In the S3 bucket permissions edit the CORS configuration to:
 [
    {
        "AllowedHeaders": [
        "Authorization"
        ],
        "AllowedMethods": [
        "GET"
        ],
        "AllowedOrigins": [
        "*"
        ],
        "ExposeHeaders": []
    }
]

- Edit the bucket policy

    - click on policy generator 
    - select 's# bucket polict' as policy type 
    - enter "*" in the principlr text box
    - from s3:action menu select 's3GetObject
    - enter arn from bucket policy 
    - add statement
    - generate policy
    - copy the policy and paste it in the buckey policy
    - in the same text box add "/*" to the end of the resource key and save
    - edit access control lost and enable 'list' for everyone and save


- Create AWS group and static file user

    - click services and select IAM
    - create user group
    - create permissions policy for the new user group
    - attach policy to the user group
    - create a user and download the Access key ID and the Secret access key


- Install packages in gitpod required to use AWS S3 bucket in django

    pip3 install boto3
    pip3 install django-storages

- add storages to installed apps in settings.py 

- at the top of your settings.py file set:
    - SECRET_KEY = os.environ.get("SECRET_KEY")
    - DEBUG = "DEVELOPMENT" in os.environ

- add a conditional setting for databases to  link up the Heroku Postgres server when in production and SQLite3 when developing locally

- tell Django to where to store media and static files 

- import setting and static functions

- add heroku app url into allowed hosts at the top of settings.py

- link S3 Bucket to Django Project

- create Procfile at the top level of the file structure containing 'web: gunicorn PROJECT_NAME.wsgi'

- make an initial commit and push the code to the GitHub Repository

- add AWS Keys to Heroku Config Vars

- add the USE_AWS variable to Heroku Config Vars and set it to True

- create a file call "Custom_storages.py" 

- set up Heroku for use via the console

    - heroku login -i
    - enter username 
    - password is the API key from account settings in heroku
    - get app name from heroku with'heroku apps'
    - set heroku remote with 'heroku git:remote -a
    - add commit and push to github
    - push to heroku with 'git push heroku main'

## Frameworks/ Libraries/ Technologies Used

- Django
Django was used as the python framework in the project.

- Django-allauth
Authentication library used to create the user accounts

- HTML
HTML was the base language used to lay out the skeleton of all templates.

- CSS
Custom CSS is used to style the page and make the appearance look 'prettier' for the client.

- Python
The packages installed for the project can be found in the requirements.txt

- Javascript
I have used Javascript to manipulate the DOM and communicate with the backend increment and decrement quantity and for toasts.

- SQLlite3
Was used during development as a database to test models.

- Bootstrap
I am using bootstrap v4.4.1 and it was heavily implemented.

- Crispy Forms
Used to manage Django Forms

- Font awesome
Icons used in the navbar and footer.

- Chrome Dev Tools
Used for overall development and tweaking, including testing responsiveness and performance

- ElephantSQL
Used to host postgres URL

- Mailchimp
Used for newsletter subscription

- Stripe
Used to handle payments.

- AWS S3
Used to store static and media files.

- Heroku
Used as platform for final deployed version of the site.

- W3C
Used for HTML & CSS Validation


## Credits 

- W3Schools

- Django Docs

- Bootstrap 4.6 Docs

- Stack Overflow

- Code Institute - Boutique Ado Walkthrough Project

- Stripe Documentation

## Acknowledgments

- I would like to acknowledge and thank brian and Freddie for code review and helpful ideas.