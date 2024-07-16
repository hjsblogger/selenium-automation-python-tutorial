# Tutorial: Automated Testing using Selenium Python

<img width="700" height="400" alt="Bulb" src="https://github.com/user-attachments/assets/2806cf9b-56ae-418d-88dd-a27a9f7d71a6">

<div align="center"><a href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_utiFN8XiYDKXMtI1UW8YG4buAslJnsuBNw&s">Image Credit</a></div>
<br/>

In this 'Automated Testing using Selenium Python Tutorial' repo, we have covered the following usecases:

* <b>Execution of simple Python tests</b>
* <b>Automating keyboard and mouse interactions</b>
* <b>Switching tabs & windows</b>
* <b>Handling drop-downs, radio-buttons, and alerts</b>
* <b>Automating Frame and iFrame interactions</b>

## Pre-requisites for test execution

**Step 1**

Create a virtual environment by triggering the *virtualenv venv* command on the terminal

```bash
virtualenv venv
```
<img width="1418" alt="VirtualEnvironment" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/89beb6af-549f-42ac-a063-e5f715018ef8">

**Step 2**

Navigate the newly created virtual environment by triggering the *source venv/bin/activate* command on the terminal

```bash
source venv/bin/activate
```

**Step 3**

Procure the LambdaTest User Name and Access Key by navigating to [LambdaTest Account Page](https://accounts.lambdatest.com/security). You might need to create an an account on LambdaTest since it is used for running tests on the cloud Grid.

<img width="1288" alt="LambdaTestAccount" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/9b40c9cb-93a1-4239-9fe5-99f33766a23a">

**Step 4**

Add the LambdaTest User Name and Access Key in the *Makefile* that is located in the parent directory. Once done, save the Makefile.

![1_Makefile](https://github.com/user-attachments/assets/8c98b44c-efd7-4a50-8647-e5477c007068)

## Dependency/Package Installation

Run the *make install* command on the terminal to install the desired packages (or dependencies) - Pytest, Selenium, etc.

```bash
make install
```
<img width="1404" alt="Make-Install" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/4cb16443-4411-4f11-8692-aa7290cded0b">

<img width="1404" alt="Make-Install-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/8c7e8938-5584-480b-ad04-002b53827396">

With this, all the dependencies and environment variables are set. Instead of PyUnit/*unittest*, the Pytest framework is used for test execution. The following websites are used for demonstration:

* [LambdaTest Selenium Playground](https://lambdatest.com/selenium-playground)
* [LambdaTest E-commerce Playground](https://ecommerce-playground.lambdatest.io/)

Follow the below mentioned steps to run automated tests using Selenium Python:

**Step 1**

Set *EXEC_PLATFORM* environment variable to *cloud*. Trigger the command *export EXEC_PLATFORM=local* on the terminal.

**Step 2**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files

<img width="512" src="https://github.com/user-attachments/assets/62d0a440-3cdb-4721-95a2-f4d3492f2a47">

**Step 3**

Trigger the respective *make* command on the terminal to run the test(s). For example, run the command *make mouse_interactions_test* for triggering mouse interaction tests.

<img width="1428" src="https://github.com/user-attachments/assets/96cda0bf-e0ed-4e5e-8b8e-d4416d8246df">

As seen above, the test execution was successful and the status is "Completed". You can find the status of test execution in the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build).

<img width="1440" src="https://github.com/user-attachments/assets/b8c562b4-6e30-49e3-874b-90a150634cf7">

<img width="1440" src="https://github.com/user-attachments/assets/b657d060-c09b-482f-8dc7-a1bf2373f15c">

Simply type *make help* on the terminal to know the command for running the intended test(s).

<img width="627" src="https://github.com/user-attachments/assets/207c5706-74e7-4508-8a04-e97f251ccfe9">

## Have feedback or need assistance?
Feel free to fork the repo and contribute to make it better! Email to [himanshu[dot]sheth[at]gmail[dot]com](mailto:himanshu.sheth@gmail.com) for any queries or ping me on the following social media sites:

<b>LinkedIn</b>: [@hjsblogger](https://linkedin.com/in/hjsblogger)<br/>
<b>Twitter</b>: [@hjsblogger](https://www.twitter.com/hjsblogger)