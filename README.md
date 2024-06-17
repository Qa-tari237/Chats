"# Chats" 
The Chat Rooms App is a Django-based web application that allows users to create and join chat rooms for real-time communication.

-------------------------------------------------------
2.Features
-------------------------------------------------------
User Authentication: Users can sign up, log in, and manage their profiles.
Chat Rooms: Create new chat rooms or join existing ones.
Real-time Messaging: Send and receive messages in real-time within chat rooms.
Notifications: Receive notifications for new messages and chat room activities.
Search: Search for chat rooms and messages.
Moderation: Chat room owners can moderate discussions.

-------------------------------------------------------
4.Technologies Used
-------------------------------------------------------
Django: Web framework for Python
Channels: Django extension for handling WebSockets and asynchronous communication
Bootstrap: Front-end framework for responsive design
SQLite/PostgreSQL: Database management

-----------------------------------------------------
5.Installation
-----------------------------------------------------
Prerequisites
Python 3.x
pip package manager
Django

Steps
1.Clone the repository:

Copy  the  code
git clone https://github.com/Qa-tari237/Chats

cd Chats

Install dependencies:

Copy the code
pip install -r requirements.txt

Apply database migrations:
________________________________________________
Copy the code
python manage.py migrate
_________________________________________________
Create a superuser (optional):


Copy the code
python manage.py createsuperuser
_________________________________________________

Run the development server:


Copy the  code
python manage.py runserver
Access the application at http://localhost:8000 in your web browser.

-------------------------------------------------------
6.Usage
-------------------------------------------------------
Sign Up / Log In: Create a new account or log in with existing credentials.

Create or Join Chat Rooms: Navigate to the chat rooms section, create a new room, or join an existing one by entering its name.

Chatting: Once inside a chat room, type your messages in the input field and press Enter to send. Messages appear in real-time for all participants.

Notifications: Receive notifications for new messages and other chat room activities.

Profile Management: Edit your profile information and update settings as needed.

-----------------------------------------------------
7.Contributing
------------------------------------------------------
Contributions are welcome! Fork the repository and submit a pull request with your improvements or bug fixes.