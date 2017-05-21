# Installing Wordpress Locally

The basic instructions for installing Wordpress are [here](https://codex.wordpress.org/Installing_WordPress). This web page is a little complicated because they provide instructions for installing in different environments. The instructions below provide a streamlined account of how you would install Wordpress locally with XAMPP. Local installations are good for developing your blog. When you are ready to install in a hosted environment, the internet service provider will likely have a more streamlined method. However, understanding how to install Wordpress locally will help you with whatever procedures they have in place. See also [Why not just use Wordpress.com?]() at the end of this document.

## Start by getting all the software in place

1. Download and install XAMPP. On Windows, you should install XAMPP to `C:\xampp`. If you have a Mac, your `xampp` folder can go anywhere; just remove `C:\` from the instructions below.
2. Open the XAMPP control panel. In Windows, hold down the Windows key and press `Q` to search for `XAMPP control panel`. On a Mac, search for `manager-osx`. Start the Apache server service and the MySQL service (the database). When you are done playing with Wordpress, return to the control panel and stop these services.
3. Go to `C:\xampp\htdocs` and create a new folder called "myblog" (or whatever you want your blog to be called).
4. Download load Wordpress and extract the zip archive. Copy all the files and folders in the extracted wordpress folder to `C:\xampp\htdocs\myblog`.

## Next create the database

1. Open a browser and type `localhost/phpmyadmin` in the address bar. phpMyAdmin is XAMPP's database administration tool.
2. Click the `Databases` tab. Under "Create Database", enter a name for your database. For now, it is probably easiest to name it the same thing as your blog, e.g. `myblog`. Pull the "Collation" dropdown to select `utf8_general_ci`. This provides the database information about how to sort English words. For Nepali, you can try `utf8mb4_general_ci` if you start getting strange results.
3. Click the `Users` tab. Make sure there is a line with the following information:

```
User: root
Host: 127.0.0.1 (or localhost)
Password: No
privilieges: ALL PRIVILEGES
Grant: Yes
```

When you move the blog to the internet, you will have to assign a different user and password to the database, but that's not necessary for a local installation.

## Finally, install Wordpress

1. In your `myblog` folder, find a file called `wp-config-sample.php`. Open it in Sublime.
2. Look for the following lines:

```php
/** The name of the database for WordPress */
define('DB_NAME', '_database_name_here_');

/** MySQL database username */
define('DB_USER', '_username_here_');

/** MySQL database password */
define('DB_PASSWORD', '_password_here_');
```

Replace _database_name_here_ with the name of you database (e.g. _myblog_). Replace _username_here with _root_ and delete _password_here_ so that it just reads `''`. Save the file as `wp-config.php`.

3. In your browser, go to `localhost/myblog` (replace `myblog`) with whatever name you have given your blog. If everything went well, you should be prompted with instructions for installation. The only thing that might be confusing is that you will be asked for a username and password. This for your login credentials for the blog, which is different from the database username and password. I suggest using "admin" for both username and password for a local installation. You will obviously choose something more secure when you install on the internet.

4. You should now be given a login prompt. Enter your username and password, and you should arrive at the Wordpress dashboard.

## Why not just use Wordpress.com?

The terminology for the two types of Wordpress can be a little confusing. Wordpress itself is open source blog software. You can download it at Wordpress**.org**. If you do this, you are responsible for hosting the software and for backing up your data. Wordpress**.com** is a commercial hosting service that will backup your data but will not allow you to access all features of Wordpress. In essence, Wordpress.org provides greater freedom, but with greater freedom comes greater responsibility. Here are the major differences in what you get:

On Wordpress.com you’ll get a domain name like `myblog.wordpress.com`. With Wordpress.org, you will typically pay for whatever domain name you want, e.g. `scottkleinman.com`. Your blog will then generally be found at something like `scottkleinman.com/myblog`. That is, "wordpress" will not be in the address.

On Wordpress.com you are able to choose from around 100 different blog themes with a few limited customisation options. With Wordpress.org, you are able to choose from over 1500 themes (and the number is growing). You are also able to customise them fully.

Wordpress.org has thousands of plugins which allow you to extend the functionality of Wordpress. Wordpress.com does not allow you to extend the functionality. It also does not allow you to run your own Javascript, which can provide functionality for user interaction. My students have found themselves unable to do things they wanted to do using Wordpress.com.

Free Wordpress.com accounts have limits on file storage associated with your blog. Other services used for hosting Wordpress using Wordpress.org.

You can run Wordpress.org locally on your own computer without a hosted account. This is useful for designing and developing your blog before you make it visible on the internet.

For a more detailed account of the differences between the two types of Wordpress, see [https://startbloggingonline.com/wordpress-com-vs-wordpress-org-whats-the-difference/](https://startbloggingonline.com/wordpress-com-vs-wordpress-org-whats-the-difference/).
