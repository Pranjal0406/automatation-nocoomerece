# Selenium Hybrid Framework
# (Python ,Selenium , PyTest , Page object Model ,Object Reports)

# What is Framework ?
# Organised way of maintaining the automation files. I  framework allthe files comunicate each other to perform a specfic Task
# Main objective  is to reuse the code or reusability
# like utility file and maintainability

# Tyes of Framework:
# 2 types are there
#
# 1)Built in frameworks:
# Pytest ,Robotframework ,unitest etc
#
# 2)Customized user defined frameworks:
# Datadriven Framework (Excel) ,Keyword driven framework ,Hybrid driven Framework

# Now we are creating our own selenium project using Hybrid Framework :

# Now  begin with the Phases
# Phases-1  :
# 1) Analyse the application , technology and skills , choose test case

# Suppose I have 100 test cases how I can verify that how much cases will automate :
# # First thing is that we need automation becoz of to overcome the challanges of retesting and regression testing
# # from that 100cases first pick the retest cases and regression testcases
# Test can can be automatible
#
# Q = now 100 percent automation is possible ?
# No its not possible whatever cases we can automate we can do only that (Analysis is necessary )
#
# 2) Phase -2
#
# Design and implementation of framework
#
# 3) Phase -3
#
# Execution
#
# 4) Maintainance (Version Control System)

# Here I am automating the E-Commerce application (Not the flipcart and amazon ) I am taking some other website

# Two sides are there of an E-commerce applicattiion
# a) frontend - means Login--> Select the product --> add to cart --> Do the payment ----> You will get the product
# b) Backend =  To many things we need to capture and we are going to automate that backend side

# Frontend Everyone will know but actual challanges we are facing in backend

# Ecommerce Application:
#
# Frontend -  For Practice Purpose # https://demo.nopcommerce.com/
# Backend =  For analysing the scenerios # https://www.nopcommerce.com/en/demo # this we are automating
#
# Start the project :
# First add all the required packages :

# In lecture 4th :
# Now version control tools are come into picture (for the maintainance part and place you code over there )
#
# We are discussing the 3 things :
# 1) Git
# 2) Git Hub
# 3) Jenkins
#
# Very very imp in Automation

# Developer write the code and place the code in a common places known as Repository same for automation as well
# Now devops will come into picture
# Like -     Developer  --------------->> Devops <<-------------------Automation
#
# Devops will pick some task from developer and some from automation they do two tasks developement as well as testing
#
# 1) Take some tasks from repository (Developer) and create a build
# Build --> We cannot test those programs directly for that we need a build means need an instaler Final integrated Product
# we dont see the code inside what they have build
# so the build creation is dne by devops
# 2) they also execute sone basic test test cases to verify that the build is stable or not
# Devops also take the basic test cases from the Automation as well
# Both done by the developer
#
# Now once the trst case is passed the devops team send an email to everybody the build is successful
# then the testing team download the build in QA Env and do the manual as well as Automation Testing

# this whole is a automated process complete build is a automation process
# some tools are there
# 1) Aapache MAVEN
# 2) jenkins
# 3) Gradle
# The version Control system will come into picture : (means we have to maintain ore code in the repository )
#
# for that we are using git and github
# Git is a local repository
# Each one in the team having the sme software
#
# Git- Whatever the code we have executed successfully first push the code into git repository (commit action )
#
# now from git push the code into remote depository means github repository
# Remote repository most of the time is same for automation and developers
# Devops team will get the code from this global repository means GITHUB
# Now evops will pick the code from GITHUB and execute the trst cases using jenkins tool (Jenkins is continious integration tool )

# Now process by diagram :
#
#
#                                         [Jenkins]
#                                         |
#                                         Down arrrow
#                                         GitHub
#                                         ^
#                                         |
#                                         GIT
#                                         ^
#                                         |
#                                         CODE
#
# Means first the code is pushed to git so the code and the git software should be present on you local repository means local system your laptop
#
# from there push the code to github means remote or global repository then
# jenkins will get the code form githun and do the execution
# End to End processs
# Now  d this practically








