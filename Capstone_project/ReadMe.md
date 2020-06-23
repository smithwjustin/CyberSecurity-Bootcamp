## Capstone Project 

### Overview

This week is dedicated to final student group projects: a Red Team vs. Blue Team activity. 

Today specifically, you will introduce the project and students will begin working on the Read Team portion. 

### Class Objectives

Students will use the following skills to complete the project: 

- Command line syntax
- Networks via `Nmap`
- The Linux directory structure
- Penetration testing
- Brute force attacks
- Using NIDs, specifically Snort
- Reading network traffic with Splunk


### Instructor Notes

**Week Overview:**

This week will proceed as follows: 

- Day 1: Project Overview, Group Assignments, Red Team Activity 
  - Students will infiltrate a remote VM.  

- Day 2: Blue Team Activity, Presentation Prep
  - Students will be given a snort file from our teams attack. 
  
- Day 3: Group Presentations
    - Students will present their findings. 
  
This is the last week of class. Students have come a long way in the program, so be sure to praise them for the hard work completed and the new skills learned. 

In lieu of three separate lesson plans, this single lesson plan will give guidance for the entire week. We haven't given specific times for individual portions of the week, but please follow the breakdown of days as noted above. 

Even though all groups will be working on the same project, each group presentation will focus on a different aspect of the project. 
  - Emphasize the importance of these presentations FILL IN 


**Lab Environment**

- Today's lab environment is **Ubuntu 18 & Kali**.

- To launch the lab, find your university-specific URL in the following spreadsheet: [CybrScore URLs](https://docs.google.com/spreadsheets/d/1PmTaBRGfPZOUKXhedtvwcDnaD9SO-shwOMaN9XArbbc/edit?usp=sharing).

- Log in and use `Ctrl/Cmd + F` to search for the lab name.

- Click the `Launch` button to start the lab.

- **Be sure to Slack out the links to each lab.**

### Slides 

Using the Project Slide Deck, explain the project structure, components, and deliverables that students will be working on during the week. 

- [Project Slide Deck](https://docs.google.com/presentation/d/1s_FrN9ENPyNWf4paWjku81StLZIPfBQ3XirmRiRetsg/edit#slide=id.g454b71f97a_0_3) 


---

### 01. Instructor Do: Project Overview  

Welcome students to class and congratulate students on reaching the last week of the program. 
- Emphasize the concepts they've learned, the skills they've developed, and how hard they've all worked to get here. 
- Let them know that this week will involve putting those skills to the test. 
  
Encourage discussion and reflection by asking the following questions: 
- What are the skills you've learned in this course?
- What do you feel more confident in? 
- Where do you want to go from here?
  
Let students know that they'll spend the entire week on a Capstone group project, which will be reflective of the skills that they've learned throughout the course. Explain the following about the Capstone project:

- The group project will be a Red Team vs. Blue Team project. 

- Specifically, students will play the role of a Red Team Pentester and hack into a vulnerable web server. They will then play the role of the Blue Team and investigate the attack via Snort logs. 

- On the final day, each group will give a presentation that focuses on a specific aspect of the project. 
  

Let students know how this week will proceed: 
- **Day 1: Red Team Day**: 
  - In groups, students will infiltrate a web server to capture a flag. The web server is hosted on Cybrscore. 

- **Day 2: Blue Team Day and Presentation Prep**: 
  - In groups, students will investigate a snort log from a different team's attack.   
  - Students will also spend the second half of the day preparing their presentations. 

- **Day 3: Presentation Day**
  - Students will present their projects. 
  - All presentations need to include an overview of what the group did, how they did, and what they found. 
  - Additionally, each group will have a specific assignment topic that they will focus on for their presentation. 


### 02. Instructor Do: Group Assignments and Presentation Expectations

Divide the class into groups of 4-5 students.

- **Note:** We've given five different presentation topics. If possible, divide the class into 5 groups in order to have all topics covered. 

Before diving into the specifics of the Red Team and Blue Team activities, give students details on the presentations they'll be preparing. Explain to students that presentations should be:
  - Between 10-15 minutes long, followed by 5 minutes of Q&A.
  
  - Each group should have a slide deck to use for their presentation.
  
  - Each member of the group is expected to speak. 
  
  - Each member of the group is expected to contribute to the slide deck. 
  
  - **Important:** Remind students to take screenshots of their work as they go through the activity so that they include these in their presentation decks. 

Remind students that communication is an important soft skill in Cybersecurity. They should spend adequate time preparing their decks to make them visually appealing. They should also use these presentations as the final opportunity in the program to practice public speaking and honing their ability to communicate highly technical topics to a general audience.

#### Demo Day

Explain to students that they can also modify their presentations for Demo Day which will occur at some point after graduation. 
  
  - Demo Day is a chance for them to meet and network with employers and other boot camp graduates. 
  
  - They should demonstrate a project that they've done during the program. We recommend they demonstrate either this project or their earlier pentesting project. 
    
    - Point out that demonstrating a report is not very dynamic, but if they can communicate their process and thinking into a visually appealing slide deck that they can walk employers through, this will better capture the skills that they've gained in the program. 
  
   - Students should modify their presentations for demo day. Encourage them to include all the group-specific topics in their presentation. 
  
   - Let them know that we'll get to these group-specific topics momentarily. 
   
#### Presentation Expectations
   
- Presentations and slide decks should include the following: 
  - **Project overview:** Discuss assignment scope, tools used, how the machine was identified, and the vulnerabilities found. 
  - **Reconnaisance:** How did you identify the target? What tools did you use to identify that the target was vulnerable? If you were a real attacker what would make this an appealing target to hack? How would the business be affected if you were to attack this  infrastructure?
  - **Group-specific topic:** Each group will expand on a specific topic aspect of the project. Your instructor will assign you these topics. 


#### Group-Specific Topics

**Vulnerabilities** Address the following questions in your presentation:
- How did you recognize this virtual machine was vulnerable? 
- Were there any other vulnerabilities that you saw? 
- What would you do to fix what you exploited? 

**Attack Methods** Address the following questions in your presentation: 
- What tools did you use to bypass the security?
- How did you know those would work? 
- Would they work in the real world? 
- What would you recommend to your clients?

**Post Exploitation** Address the following questions in your presentation:
- When you were in the machine, what user were you? 
- Did you have access to the full machine? 
- How would you be able to defend against this exploit? 
- What would you do to maintain access to the server?

**Incident Response** Address the following questions in your presentation: 
- What time did the attack start and how long did it last?
- What was the IP address of the attacker?
- Who was the attacker trying to login as? Was the attacker successful?
- How many passwords did the attacker use before they found the correct password?
- What kind of attack was the attacker using? How is this reflected in the report?

**Mediation** Address the following questions in your presentation: 
- How would you protect your servers from these attacks? 
- Are there any other vulnerabilities that the server would be prone to? What are they? 
- How would you fix those?


### 03. Student Do: Red Team 

Let students know that for the Red Team portion of the project, they will log into Cybrscore and use a Kali instance to log into a vulnerable web server. 

 - Hidden in the web server is a file called `flag.txt`. They will need to use a reverse `php` shell to gain access to the web server to recover the `flag.txt` document. 
 
Below is the solution file for the activity. Do **not** review it in class. Only use it as reference to help groups if they are stuck. 

- [Solution](activities/1_stu_red_team/solution/ReadMe.md)
	
Point out that students will need to complete the following steps in order to find the flag:
- Log in to Cybrscore. 
- Discover the IP address of the Linux server.
- Locate the hidden directory on the server.
- Brute force the password for the hidden directory.
- Break the hash password with John the Ripper
- Connect to the server via Webdav.
- Upload a reverse php connection payload.
- Capture and show the flag to your instructor.
- Show your instructor once you have captured the flag, and they will send you the pcap file for the next part of the capstone. 

Emphasize that students should be taking screenshots as they work through this activity to include in their presentations.

When students show that they have located the flag, please Slack out the Snort log below so students can get started on the Blue team exercise. 

- [Snort Log](resources/snort.log.1557160271)
 
Send students the following instructions over Slack:

- [Instructions](activities/1_stu_red_team/ReadMe.md)

The details of the student activity file are located below for your reference.


**Red Team**


In this activity, you will log into CybrScore and use a Kali instance to hack into a vulnerable web server. 

- Hidden in the web server is a file called `flag.txt`. 

- You will need to use a reverse `php` shell to gain access to the web server to recover the `flag.txt` document. 

- Once you have shown the instructor that you have recovered the flag, raise your hand and your instructor will give you a Snort file from a different teams attack. 


**Part 1: Red Team Objectives**

Complete the following in order to find the flag:
- Log in to Cybrscore. 
- Discover the IP address of the Linux server.
- Locate the hidden directory on the server.
- Brute force the password for the hidden directory.
- Break the hash password with John the Ripper
- Connect to the server via Webdav.
- Upload a reverse php connection payload.
- Capture and show the flag to your instructor.
- Show your instructor once you have captured the flag, and they will send you the pcap file for the next part of the capstone. 

**Note**: You need to complete **each** step for full credit. 

**Important**: Make sure to take screenshots as you work through the process. They will be need in your presentation. 



### 04. Student Do: Blue Team 

Explain the following to students:

- They will be able to complete the Blue Team portion of the Capstone after they have infiltrated the vulnerable machine and downloaded the Snort log. 

- Let students know that if they finish the Red Team activity before the end of Day 1, they can move on to the Blue Team activity. 

Below is the solution file for the activity. Do **not** review it in class. Only use it as reference to help groups if they are stuck. 

- [Solution](activities/2_stu_blue_team/solution/ReadMe.md)


Send students the following instructions over Slack:

- [Instructions](activities/2_stu_blue_team/ReadMe.md)

The details of the student activity file are located below for your reference.


**Blue Team**

In order to complete the Blue team portion of the Capstone, you will already need to have infiltrated the vulnerable machine and have received the snort log from your instructor. Next you will need to complete the following objectives. 

**Objectives:**

- On your Kali machine, use Wireshark to open the Snort log.

- Look through the data and **answer the following questions according to Wireshark**: 
  
  - How long did the attack last?
  
  - How many password attempts were made?
  
  - In which packet was the correct password found? 
  
  - In which packet was the shell placed onto the server?
  
  - In which packet was the shell activated? 
	




