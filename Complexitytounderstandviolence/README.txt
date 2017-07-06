***************************************************************************
README 
***************************************************************************

This file contains information on how to use this template.

TABLE OF CONTENTS

HTML VERSION

1.	Install your template
2.	Create a new page
3.	Edit the menu

PHP VERSION
1.	Install the php version
2.	Structure
3.	Customize

***************************************************************************
 **** HTML VERSION ****
***************************************************************************

1 - INSTALL YOUR TEMPLATE
Unzip all files in a directory on your computer and call it "template" for example. To access your template, 
open the file "index.html" in the "template" folder by double clicking on it. Your website is now ready to be used.

***************************************************************************
2 - CREATE A NEW PAGE
To create a new page, simply duplicate the file "about.html" and rename it to for example "yourpage.html". Now, open 
"yourpage.html" in any text editor. You'll see a lot of code. Don't bother this right now, scroll down until you locate 
the following line of code:

                    <div class="content-box">
                           <h3>About</h3>
                           Place your content here.
                    </div>

This a block of text displayed on your website. Every text between <h3> and </h3> is the header of the block of text and 
will be displayed in a larger font. Now, replace the sentence "Place your content here." with your own text and/or html code. 
To create a new block of text, copy the whole code from <div … to </div> and paste it below the first block. It will look 
like this now:

                    <div class="content-box">
                           <h3>Header 1</h3>
                           Place your content here.
                    </div>
                    <div class="content-box">
                           <h3>Header 2</h3>
                           Some other content here.
                    </div>
Save your page. In the next chapter we will explain how to add this page to your menu.


***************************************************************************
3 - EDIT THE MENU
Lets say that you just have created a page called "downloads.html". But now you want this page to be displayed correctly 
in the menu. Open index.html and scroll down until you see the following code:

<ul>
                     <!-- This are the links from the left menu. -->
                         <li><a href="index.html" title="Home">Home</a></li>
                         <li><a href="about.html" title="About">About</a></li>
                         <li><a href="#" title="Webdesign">Webdesign</a></li>
                         <li><a href="#" title="Music">Music</a></li>
                         <li><a href="#" title="Contact">Download</a></li>
                         <li><a href="#" title="Contact">Contact</a></li>                     
</ul>

Replace it with the following code:

<ul>
                     <!-- This are the links from the left menu. -->
                         <li><a href="index.html" title="Home">Home</a></li>
                         <li><a href="downloads.html" title="Downloads">Downloads</a></li>
</ul>

Save your page. Now, when you open index.html in your web browser you will see only two links in the menu. When you 
click on "Downloads" the page will open "downloads.html". You have changed the menu successful! However, the menu on 
"downloads.html" has not changed yet, so you might have to change this too.


***************************************************************************
**** PHP VERSION **** 
***************************************************************************

1 - INSTALL THE PHP VERSION
To install the PHP version you need a web server that supports PHP. Unzip the template in a folder named "template" for 
example. Remove all files in this folder except the "phpversion" folder. Move all files located in the "phpversion" one 
folder up, so that all files which were located in the "template/phpversion" folder are moved to the "template" folder.

Your website structure will look like this now:

template/data/
template/engine/
template/images/
template/pages/
template/index.php
templaye/GNU.txt

Now, upload these folders into the root or www folder of your website host. To access your website, type the following text in 
your web browser: http://www.yourwebsite.com/index.php.

***************************************************************************
2 - STRUCTURE
The engine has 4 folders. 

** template/data **
This folder is the folder containing all data used in the engine which can be changed without harming the layout.

" error404.data.php This file contains the text displayed when a page can't be found.
" errordefault.data.php This file contains the default error text.
" menu.data.php In here is the data for your menu. 
" title.data.php The text in this file is the text displayed in your header and in the top browserbar.

** template/engine **
All files in this folder should not be changed. If there any updates for this engine, only these files will be replaced. 

" style.css If you are an advanced user, you can customize and expand your template by editing this file. 

** template/images **
The images in here are copyright Tuned Studios, so unless you have permission, you are not supposed to edit them. Feel free to use this map for your own images however. 

** template/pages **
All pages are loaded from this folder, so make sure you put every page in this folder. 

***************************************************************************
3 - CUSTOMIZE
Menu
To customize your menu, open the file 'menu.data.php' which is located in the folder 'data'. 

The first line you see will be this one: 
'<li><a href="index.php" title="Home">Home</a></li>'. 

" href="index.php" This is the link to your page. The file 'index.php' is located in the root of your website. If you 
would like to link to a page located in the 'pages'-folder, simply change 'href="index.php"' to 'href="pages/home.php"' 
if your file is named 'home.php'.

" title="Home" This text is displayed in a label when you move your mouse over the link. 

" Home This text is displayed in your menu. 

An example on how to fill a page with content can be found in the folder 'pages' in the file named 'home.php'. 
To create a block of text, put your content between '<div class="content-box">' and '</div>' as shown in 'home.php'. 

TITLE
To edit the title displayed in your header, open 'title.data.php' which is located in the folder 'data' and change the text 
to whatever you like.

***************************************************************************
***************************************************************************

In search for other templates? Visit www.tunedstudios.com for more designs!
Questions? Contact us by sending an email to helpdesk@tunedstudios.com 

© Tuned Studios 2005-2006


