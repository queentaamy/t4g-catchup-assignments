</What Happens When You Type a URL and Press Enter/>

When I type a URL into my browser and press Enter, several things happen behind the scenes:

1. DNS Lookup
The browser first checks with the Domain Name System (DNS) to translate the website name (like amazon.com) into an IP address. The internet uses IP addresses, not names.

2. Firewall Check
The request passes through firewalls that check if the traffic is allowed. Firewalls protect servers from unauthorized or harmful access.

3. Load Balancer
If the website has many users, a load balancer distributes the request across multiple servers so no single server becomes overloaded.

5. Web Server
The web server receives the request. It handles static content like HTML, CSS, and images. If dynamic data is needed, it forwards the request.

6. Application Server
The application server processes business logic. For example, if I’m logging in, it verifies my credentials.

7. Database
If data is needed (like user information), the application server queries the database. The database returns the data to the application server.

8. Response Sent Back
The application server sends the processed result back to the web server, which sends it to my browser to display.


</Web Server vs Application Server (Real-World Example)/>

--A web server is like a receptionist. It handles basic requests and serves static files.

--An application server is like a manager. It handles logic and makes decisions.

<For example, imagine an online dress store:>

**The web server shows the homepage and product images.

**The application server processes payment when someone buys a dress.



</Why the Client Never Talks Directly to the Database/>

The client never talks directly to the database because:

**It would be a huge security risk.

**Anyone could access or modify sensitive data.

**The application server controls validation and business logic.

**It ensures only allowed and verified actions reach the database.

  The application server acts as a secure middle layer.
