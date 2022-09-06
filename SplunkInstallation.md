## Installing Splunk into Virtualbox

Here is a quick and easy guide how to get the main Splunk enterprise program onto your network in VirtualBox. I'll be skipping the installation step for VirtualBox but luckily there are tons of resources online that will show you how to do this. So lets start with programs...


**Finding the right base (OS)**
You can Splunk onto practically any mainstream OS; but in this scenario we want to choose an OS that has as resource efficient, cheap, and reliable. The best OS that comes to mind is **CentOS**.

CentOS is free and open source for anyone to use, its light weight and does everything we need it to do to host Splunk. You can get it [here](https://www.centos.org/download/) and choose the appropriate architecture that applies to you. You don't need anything fancy so obtaining the minimum ISO is more than enough to do what we want. We will store this in a place where we can reference it later

## Installing a SSH Client


Once the ISO is saved in a safe space the next step is to download a SSH client. I've decided to go with **PuTTY**. Again the reason I'm going with PuTTY is because it is lightweight and its *free*. We don't really need a SSH terminal, but since we are installing an SIEM, we might as well take the steps to exercise good security practices. There are many options for terminals so you can pick whichever one is best for you or your company.

Installing PuTTY is pretty straight forward it can be found here: https://www.putty.org/ just make sure to install the correct one according to your computer's specifications.

## Grabbing the Splunk installation

Head on over to Splunk, create an account and navigate your way to the Splunk Enterprise trail section. From there you have the option to choose from Windows, Linux or MacOS installation. Since we are using CentOS we are going to use the .rpm Linux 64bit option. You'll be directed to a downloads page where you can download via the Command Line that should look like this :

`wget -O splunk-9.0.1-82c987350fde-linux-2.6-x86_64.rpm "https://download.splunk.com/products/splunk/releases/9.0.1/linux/splunk-9.0.1-82c987350fde-linux-2.6-x86_64.rpm"` 

We will copy this to a notepad so that we can use it later.


## Setting up your VM

For this most part this section is fairly simple, all you need to do is set up your VM with Red Hat Enterprise Linux as your base. You need to mount the ISO that we got for CenTOS and configure the network type to be `Bridged Adapter` <-- This is fairly important. Once that is done you can start up the VM and proceed to the installation.

## Installing CentOS

Installing CenTOS is pretty simple you can just click through the settings. specify your hard drive and even set your networking options like IP and Net Mask. For storage I recommend 20 - 30 GB just in case since Splunk takes up a decent amount of space especially when it starting capturing information. Everthing else can be default, but that's up to you.
Once the OS has been installed we can do a quick reboot and log in. We need to find the IP for our new VM and to do that we can call `ip -a` in the terminal. From here we can see the IP address which we will save for the next step.


## Connecting via SSH (PuTTY)

Now that we have everything that we need, we can now boot up PuTTY. On the first screen PuTTY will have a
a field so we can input an IP address and it's connecting through port 22 which is commonly used for SSH. If you want to connect via Telnet we can also used port 23 but that is not secure. In this IP address field we are going to input the IP address of our CenTOS host and just click connect.
Now that we are SSH'd into the system we can now start preparing for the splunk installation.

## Preparation of the Firewall
We need to allow some ports to communicate between the OS and Splunk we can start doing that by adding Command lines for different ports. Now some of these ports aren't necessary so you should always consider opening up ports that are you going to use only. If you open ports that aren't necessary you're simply just increase the attack surface for malicious actors. Here are some ports and their commands that you can use:


    firewall-cmd --permanent --add-port=8000/tcp

    firewall-cmd --permanent --add-port=80/tcp

    firewall-cmd --permanent --add-port=443/tcp

    firewall-cmd --permanent --add-port=8443/tcp
   
    firewall-cmd --permanent --add-port=9997/tcp

The last one is really important because that is the port that Splunk uses to communicate.

## Downloading and installing Splunk

In order to start the download process we first need to get wget into out CenTOS. In our SSH terminal we need to use the command `yum install wget -y` . Next we need to use the wget command that we copied earlier to install splunk. If you need a reminder it looks like this: 

    wget -O splunk-9.0.1-82c987350fde-linux-2.6-x86_64.rpm "https://download.splunk.com/products/splunk/releases/9.0.1/linux/splunk-9.0.1-82c987350fde-linux-2.6-x86_64.rpm


Once this is done you'll be downloading splunk.

Now that this is done we now need to install Splunk. We can simply use `rpm -i < The Splunk file.rpm>` and after a few minutes of work we now have Splunk on our system. During the installation the file will create an `/opt/` directory.  So we need to navigate into the `bin` directory using `cd` a few times to find a particular `splunk` package. 

The last thing we now need to do is to start splunk and this is done using `./splunk start` when this starts it'll run the set up process where you can input an administrator name as well as a password and you have to agree to some licensing agreement.

Now we can attempt to access Splunk interface by grabbing our CenTOS IP and our access port which in this case is port 8000 to log into Splunk using our in-browser explorer (Firefox ftw bby). In my case its `http://192.168.1.100:8000` and now we are greeted with the Splunk login page, pop in your credentials and you're now good to go splunking :D

I'm lacking pictures  but I'll find time to add some in the near future..

-J




