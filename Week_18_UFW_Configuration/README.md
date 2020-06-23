# UFW Configuration

### Scenario

- In this exercise you will set up their firewall for their Linux server. We provided you with a VM that already has preconfigured network services, namely: SSH, telnet, Apache and FTP. The VM already has UFW enabled, with defaults set to deny all incoming and outgoing traffic. Make the following configuration changes. 

   - Enable the `Apache Full` UFW profile
   - Allow outbound DNS
   - Allow inbound SSH _only from the local subnet_
   - Allow inbound telnet _only from the local subnet_
   - Allow FTP _only from the local subnet_
   - Drop inbound ICMP from outside the local subnet
 
- You have also been asked to enable logging, at level high/info. 


### Deliverables

- You are expected to submit a screenshot of your name, followed by the results of running `ufw status verbose` in your Linux terminal window. 


## Virtual Machine

Please use your **Trilogy Cyber Ubuntu VM** for this assignment. 
