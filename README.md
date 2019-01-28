# Item Catalog Project


Part of the udacity [Full Stack Web Developer Nanodegree.](https://udacity.com/course/full-stack-web-developer-nanodegree--nd004)


### Introduction
 Python application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.


### Required Libraries and Dependencies
- Python 3
- Vagrant
- VirtualBox


### How to run the application
- Clone  [this repository](https://github.com/udacity/fullstack-nanodegree-vm).
- Look for the catalog folder and replace it with the contents of this respository.


#### Bringing the VM up

Bring up the VM with the following command:
``` 
vagrant up 
```
The first time you run this command, it will take awhile, as Vagrant needs to download the VM image.

You can then log into the VM with the following command:
```
vagrant ssh
```

More detailed instructions for installing the Vagrant VM can be found here.

#### Make sure you're in the right place
Once inside the VM, navigate to the catalog directory with this command:
```
cd /vagrant/catalog
```
#### Running the application
Run the application with the following command:
```
python application.py
```
#### Browse the website
After the last command you are able to browse the application at this URL:
```
http://localhost:5000/
```

#### API Endpoints
You could access the api endpoints by following this paths:
- `/catalog/JSON` - List of catalog categories in JSON
- `/catalog/int:category_id/JSON` - List of items in category requested in JSON
- `/catalog/<int:category_id>/items/<int:item_id>/JSON` - List the details of specific item
