## Installing Active Direction using Windows Server 2019 on Virtual Box

This is a guide to install Active Directory and populating it with users for myself to experiment on.

What you need to download:

 - [Windows Server 2019.iso ](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019)
 - [Windows 10.iso](https://www.microsoft.com/en-gb/software-download/windows10) 
 - [Virtual Box](https://www.virtualbox.org/wiki/Downloads)

What we are building

Pic 0

## Creating the Domain Controller

First what we need to do is boot up an instance of Virtualbox and the set up our first VM to host our domain controller. 
There are many guides on how to do this, so I'm just going to breeze past this part.  
When we create our VM what we are going to focus on is making sure that the VM instance is set to Microsoft Windows and set to Other Windows 64bit.
Once that is done we are going to make sure that there are two different network adaptors.

The first one is the NIC that connects to our home internet. It will be configured with NAT. The second one we are to add our internal network and we are going to call that "Internal" 
<pic> 
Next we are going to start the VM and choose the Server 2019 iso that we downloaded earlier. Follow the entire process installing the default settings. Once you get to the operating system installation we can make our lives easier by installing **Windows Server 2019 Standard Evaluation (Desktop Experience)** so we have a GUI that we can use. If you pick the other ones we are only left with the Command Line which isn't nice to look at. 
<pic 2>

Once that is done and started up we are going to allow the system to boot and you can create your administer account and password. 

## Setting Server Network Adapters

So now that we are up and running it's time to configure our IP networking. We are going to click got to **Network Connections** on our server and we should see two adapters. Now remember we had set up one NAT adapter and the other one is internal. 
 <pic 3>
The easiest way to determine which is which is that you can click on each adapter and look at the packages sent and packets received. Once we determine which is which we need to rename those adapters in order to make it easier for us or anyone else who is following in our steps. 
<pic 4>
Next we can right click our Internal adapter and go to **IPV4** head into **properties** and configure the IP address. Getting into IP will take forever to explain if you're new so please just trust me on this. We aren't going to use a default gateway because the Domain controller will serve as our default gate way as well as the DNS server. We will also make sure that since the server is its own DNS we will use the preferred DNS to loop back on itself using `127.0.0.1`

<pic 5>  

## Setting the Domain Controller's Name

Since our computer name is all messed up because of our virtualization, it's best for us to change it. To do it we can simply go to **System > Rename my pc** and change it to "DC".

## Installing and configuring Active Directory

So now we are going to create a domain. In the Server manager we are going to add roles and features and install **Active Domain Services** and install.
We will be sent back to the Server Manager at this point and in the notifications we will get the option to promote our newly created server to a domain controller. 

Next we can add new forest and name our domain whatever is appropriate... 

pic 6

After in putting the password we can just skip everything and just install. Our computer will automatically restart and we can sign in again into our domain. 

We can now open our Active directory. At this point we can add accounts/organizational units etc and for me, I'm going to create an domain admin account to use from now on. If you need help doing this there are guides on the internet on how to do this. 

## Installing RAS/NAT
So we are installing RAS/NAT because this private virtual network will allow our client to connect to the internet via our new domain controller. 
We are going to the add roles and features on the server manager and tick off **Remote Access** and install **Routing**. Once the role has finished installing we can then go to tools on the main server management page and select **Routing and Remote Access**.

At this point we should be able to right click our **DC (local)**  and then click **Configure and Enable** we shoudl then check off **NAT** and see our network adapters. We can check off **Use this public interface to connect to the internet.** and click the one that's connected to the internet. 

## Setting the DHCP Servcer on Domain Controller

We are going to add the DHCP using add roles and feature on the Server Manager and just click DHCP when are prompted. Once installed we can go to tools on the main page and select DHCP.

pic 7

We are going to be in our DHCP control panel and then right click IPv4 and view our scope. We can name our scope with whatever we want and then we can define the ranges. 

pic 8

Once done we can move forward. If you want to have exclusions you can do that too but we don't need that at this point. 
We also have the lease duration but that depends on your use-case. If you're in a cafe you can make the lease 2 hours or if you're in the office you can have it be on the order of days. 

Now we need to create our router by configuring the DHCP options so we can add a default gateway and add it to our list. 
pic 9

SOOOO once this is all done we can next through everything and activate the scope and authorize the server.

pic 10

Now that we have a working Active Directory we can now start populating our server with some usernames and passwords.

## Running the Powershell Script for 1000 Users

Now we can use our Powerscript to populated the domain controller. Included in my github I'll have the link [here](https://github.com/shikaleathers/Shikaleathers/tree/main/ADPowerscript/AD_PS-master) We can  got to Powershell `cd` into the directory where you are hosting it and just run the script. It should populate the server pretty quickly with few errors. I've set all the accounts to have the same password : Password1 so you can sign in with any account name to see what all that is about. 

I hope yall know Powershell hahaha

## Creating VM for Client using Windows 10

So at this point we now need to make the VM client to feed into the Domain Controller. We are going to install Windows 10. First we need to set the Network adapters and make sure its pointing towards our internal network adapter so it will connect to our domain controller with ease.
During the installing make sure not to install home because it wont connect to our directory, but install Windows 10 Pro instead.

Pic 11

Skip as much as you can and get that client running with limited setup!

Once you're in, make sure that the Domain Controller is online. From here you can do ipconfig on the client and its IP address should be within the DHCP scope we have directed from our domain controller. and if we ping [www.google.com](www.google.com) and our domain controller we should be getting responses from both.

## Joining the Domain and renaming our Client

We are nearing the end, trust me...

We now need to go into our system settings and go to **rename this PC (Advanced)**  and then click **Change**

Pic 12

Now we add on arbitrary name and connect to our the domain that we created earlier and then click OK!!!!

## The END

So we have everything connected and operating perfectly. We should be able to go into Active directory and see our different users, and use our client to connect to any account at any time assuming the domain controller is live. Because we have so many accounts we can do many things like mess around in AD or even attach more clients using the same methods that were done up top. 

 Anyways... if you're having trouble connecting to the internet using the client, make sure to check your DHCP  or DNS server settings on both your domain controller and your clients. A simple typo will mess you up big time.  

Thank you for reading and learning with me.
