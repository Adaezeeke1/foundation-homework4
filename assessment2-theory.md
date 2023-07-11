## Foundation Assessment 2 Theory

### Section 1

### Question 1.1:
SDLC stands for *Software Development Life Cycle*.

### Question 1.2:
In Python, when you divide a number by 0, a *'ZeroDivisionError'* exception is thrown.

### Question 1.3:
The git command that moves code from the local repository to the remote repository is *git push*.

### Question 1.4:
In a database, *NULL* is a special value that is used to indicate the absence of a value or the unknown state of a data field. 
In other words, it shows that a particular data item does not have a value assigned to it. It differs from zero or an empty string. 

### Question 1.5:
2 responsibilities of the Scrum Master include:

* **Facilitating the Scrum Process**: The Scrum Master is responsible for guiding and coaching the Scrum Team and making sure that the Scrum process is effectively implemented. 
They typically facilitate Scrum events, including the daily stand-up, sprint planning, sprint review, and sprint retrospective. 
The Scrum Master helps the team understand and follow Scrum practices and promotes collaboration and self-organization within the team.


* **Eliminating Impediments**: Another responsibility of the Scrum Master is to identify and eliminate any obstacles or impediments that may hinder the team's progress and productivity. 
They actively work to create a supportive and productive work environment for the team. This involves proactively identifying potential roadblocks, such as organizational barriers, resource constraints, or conflicting priorities, and taking necessary actions to address them.
The Scrum Master is generally viewed as a *servant-leader*, advocating for the team's needs and providing support and guidance to overcome challenges. 
They also collaborate with stakeholders and other teams to resolve dependencies, manage conflicts, and facilitate problem-solving. 
Ultimately, by removing impediments, the Scrum Master enables the team to focus on delivering value and achieving their sprint goals.

### Question 1.6:
* Debugging with an Interactive Debugging Console: I use a laptop with a Windows operating system, on which Pycharm is installed. 
PyCharm provides an interactive debugger that allows me to step through my code, call functions, inspect variables, and analyze the program's behavior in real-time when debugging.
To use this method, I would start the debugger by clicking on the "Debug" button or by using the keyboard shortcut *Shift + F9*.
Once in debugging mode, I would be able to use the step-by-step execution options, such as "Step Over" *(F8)*, "Step Into" *(F7)*, and "Step Out" *(Shift + F8)*, to navigate through my code and observe the execution flow. 
I can then inspect variable values, set watches, and use the debugging console to execute code during the debugging process. 
The interactive debugger in PyCharm provides a comprehensive and interactive toolset for understanding and troubleshooting my code, allowing me to track down and resolve issues effectively.


* Breakpoints: Breakpoints allow me to pause the execution of my code at specific lines, so I can analyze the state of the program and track down issues. 
To set a breakpoint in PyCharm, I would click on the left gutter of my desired line of code or use the shortcut *Ctrl + F8*. 
When the program reaches a breakpoint, it will pause, to allow me to inspect variables, step through the code, and analyze my program's behavior. 
Breakpoints are especially useful when I have identified a particular section of code where an error occurs or when I want to understand the program's execution flow.

### Question 1.7:
The function *can_pay(price, cash_given)* compares the *cash_given* amount with the *price* to determine if the payment is sufficient. 
It returns **True** if the *cash_given* amount is greater than or equal to the *price*, and **False** otherwise.

A case where this function would throw an error is if either the *price* or *cash_given* parameters are not numeric values, that is, they are string or boolean values. 
To illustrate:
```
can_pay("200", 300)
```
In this case, the function will attempt to compare a string "200" with the numeric value 300, which is not a valid operation. 
This will then result in a **TypeError** being raised.

This error can be handled using exception handling. Here, you can enclose the function call in a try-except block and catch the TypeError specifically. 
To illustrate:
``` 
try: 
   can_pay("200", 300)
except TypeError:
   print("Invalid input. Please provide numeric values for price and cash_given.")
```
By catching the **TypeError** exception, you can handle any cases where the function is called with non-numeric values and provide an appropriate user-friendly error message, as opposed to a termination by way of a traceback occurring.

### Question 1.8:
*Git branching* is a vital feature of the Git version control system that allows for the creation of independent lines of development within a repository.
It allows developers to work on different features or bug fixes simultaneously, without interfering with each other's code. 
Branching provides a way to isolate changes, experiment with new ideas or code, and merge any changes back into the main codebase when they are ready.
To illustrate how branching works in Git:

Assuming we are using GitHub as our remote repository, after cloning our repository from GitHub to our local repository, we:


* **Create a branch**: The default branch in a Git repository is usually called *"master"* or *"main."*
Each branch can have its own commits, which allows for parallel development.
We then create an independent line of development that will allow one to work in isolation from the main branch.
To create a new branch locally, use the command ``` git branch new-branch```, assuming the name of your branch is *'new-branch'*. 


* **Switch to the new branch**: Use the command ```git checkout new-branch``` to switch to the newly created *'new-branch'*. 
This step ensures that any subsequent changes will be made in the context of the new branch.
Alternatively, you can combine branch creation and switching with: ```git checkout -b new-branch```


* **Make changes**: We can then start making changes to our code, fixing bugs, or making any necessary modifications.
Git is able to track the changes made in each branch independently, keeping them separate from other branches, if they exist.


* **Stage and commit changes**: We stage the changes we want to include in the commit using ```git add -A``` or ```git add .``` to include all changes, followed by ```git commit -m "Insert commit message"``` to commit them to the branch. 
This captures a snapshot of the codebase at that point in time.


* **Push the branch**: If we want to collaborate with others or back up our work remotely, we use ```git push -u origin new-branch``` to push the named branch to our remote repository (*GitHub*). 
The ```-u``` flag sets the upstream branch, allowing us to use git push subsequently without specifying the branch name.


* **Repeat steps of making changes, staging, committing and pushing where necessary**: Repeat the process of making changes, staging, and committing as needed on the branch. 
It is possible to work on multiple branches simultaneously, each representing a distinct line of development.


* **Collaborating on a branch**: Other developers can also clone the repository from GitHub and switch to the branch we have pushed.
They can then make their own changes, commit them, and push their branch to GitHub.


* **Pull requests (using GitHub)**: A pull request is a GitHub feature that helps with collaboration and review of our code.
After pushing our branch to GitHub, we can then open a pull request to propose *merging* our changes into another branch (e.g. *main branch*).
Our collaborators can review the changes, leave comments, suggest modifications, or approve the pull request.


* **Resolving conflicts**: If there are any conflicting changes between the branch being merged and the target branch of the merging, they must be resolved.
Conflicts typically occur when Git is unable to automatically merge changes because of overlapping modifications in the same part of a file.
GitHub helps us by providing a user-friendly interface to resolve conflicts. 
It does this by highlighting the conflicting sections and offering the options to accept any one version or manually modify the code.
When this is done, the conflicts are usually resolved.


* **Deleting a branch**: Once we are done using the branch and its changes have been merged, it can be deleted without affecting the main branch.
Locally, we can delete our example branch using the command ```git branch -d new-branch```.
Remotely, on GitHub, we can also delete a branch from the web interface or use ```git push origin --delete new-branch```.


### Question 1.9:
In designing a restaurant ordering system, I have delineated the criteria I would use to achieve an efficient functioning system.


a. **Key Requirements**:
* *User-friendly interface*: It is very important that the ordering system should have a simple and intuitive interface for customers to easily browse the menu, select items, customize their orders, and submit payments.


* *User Registration and Authentication*: It is important that the system is able to allow customers to create accounts, log in securely, and manage their personal information.


* *Menu Management*: The system should enable restaurant staff to easily update and maintain the menu, so they can add new items, modify prices, and indicate item availability.


* *Order Management*: The system should be able to allow the restaurant staff to receive and manage incoming orders, track the status of these orders (e.g., pending, preparing, delivered), and communicate updates to customers.


* *Payment Processing*: It is vital that the system should support secure and seamless payment transactions, and be able to integrate with popular payment gateways to accept a variety of payment methods.


* *Reservations*: If applicable, the system should allow customers to reserve tables, specify the number of guests, and provide any special requirements.


* *Delivery or Pickup Options*: The system should provide customers the choice to select delivery or pickup, with the ability to specify delivery addresses or pickup times.


* *Notifications*: The system should be able to send real-time order status notifications to customers via email, SMS, or push notifications.


* *Special Offers and Discounts*: The system should support the application of promotional offers or discounts to customer orders (e.g student discounts).


* *Analytics and Reporting*: The system should be able to capture and analyze data on orders, sales, popular items, customer preferences, and other relevant metrics to generate reports and insights.


* *Integration with Existing Systems*: It is important that the ordering system can integrate with other restaurant systems like inventory management, POS systems e.t.c.


* *Accessibility*: It is also important to ensure the ordering system is accessible to users with disabilities and complies with accessibility standards and guidelines.


b. **Main Considerations and Problems**:
* *Scalability*: The system should be designed to handle a high volume of concurrent users and orders during peak times, without defaulting in performance or user experience.


* *Security*: Prioritize implementing robust security measures to protect customer data, including encryption, secure connections, with adherence to industry standards.


* *Usability*: Prioritize a user-friendly interface with intuitive navigation, clear item descriptions, and smooth order placement flow to enhance the customer experience.


* *Potential Integration Challenges*: Consider compatibility issues, data synchronization, and potential limitations while integrating the ordering system with existing restaurant systems (e.g. inventory systems).


* *Order Accuracy*: Minimize errors in order processing, ensure accurate capture of items, quantities, customizations, and special requests.


* *Mobile Compatibility*: Optimize the ordering system for mobile devices, as many customers may prefer to order using mobile devices.


* *Performance*: Design the system to deliver fast response times, quick loading of menus, and seamless payment processing to prevent frustration from the users.


* *Maintenance and Support*: Plan for ongoing maintenance, updates, and support to address bugs, security vulnerabilities, and accommodate future enhancements or changes in business requirements.


* *Support for unexpected system failure or crashing*: Plan for unexpected system crashes, in regard to payments, refunds, double orders and any other situations that could arise in the event of a system failure.


c. **Potential Components or Tools**:
* *Front-end Development*: HTML, CSS, and JavaScript frameworks (e.g., React) for building a responsive and interactive user interface.


* *Back-end Development*: Server-side languages (e.g., Python) and frameworks (e.g., Django) for handling business logic, data processing, and API integrations.


* *Database Management*: Relational databases (e.g., MySQL) for storing menu items, customer data, orders, and configuration settings.


* *Payment Gateway*: Integration with popular payment gateways like Stripe or PayPal to securely process payments and handle transactional data.


* *APIs*: Use APIs provided by external services (e.g., payment gateways, SMS gateways) or build custom APIs for integrating with other restaurant systems.


* *Cloud Hosting*: Platforms like Amazon Web Services (AWS) for scalable hosting infrastructure, ensuring high availability and performance.


* *Notification Services*: Utilize email service providers, SMS gateways, or push notification services to send real-time order updates to customers and staff.


* *Analytics and Reporting*: Tools like Google Analytics for capturing and analyzing order data, generating reports, and obtaining actionable insights.


* *Accessibility Tools*: Implement accessibility features compliant with Web Content Accessibility Guidelines (WCAG), including screen reader support, keyboard navigation, and high contrast options.


* *Security Measures*: SSL/TLS certificates, encryption algorithms, secure authentication protocols, and regular security audits to protect customer data and prevent unauthorized access.


* *Version Control and Deployment*: Version control systems (e.g., Git), continuous integration and deployment tools (e.g. Travis CI) to manage codebase, automate testing, and streamline deployment processes.


* *Customer Support Tools*: Helpdesk software, live chat systems, or ticketing systems for efficient customer support and issue resolution.