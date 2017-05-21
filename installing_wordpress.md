# Installing Wordpress Locally

The basic instructions for installing Wordpress are [here](https://codex.wordpress.org/Installing_WordPress). This web page is a little complicated because they provide instructions for installing in different environments. The instructions below provide a streamlined account of how you would install Wordpress locally with XAMPP. Local installations are good for developing your blog. When you are ready to install in a hosted environment, the internet service provider will likely have a more streamlined method. However, understanding how to install Wordpress locally will help you with whatever procedures they have in place.

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

