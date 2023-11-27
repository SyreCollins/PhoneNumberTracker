# PhoneNumberTracker
Overview
Phone Number Tracker is a web application built with Django that allows users to track the geographical location and carrier information of a phone number. This project leverages the power of the Django framework for the backend, integrating with various libraries to provide accurate and detailed information about a given phone number.

Features
Geographical Location Tracking: Utilize the Phonenumbers library to retrieve the geographical location of a phone number, providing users with insights into the country associated with the number.

Carrier Information: Integrate with the Phonenumbers library to fetch the carrier information of a phone number, offering details about the mobile service provider.

Map Visualization: Use the OpenCage Geocoding API and Folium library to generate an interactive map displaying the location of the tracked phone number. A marker on the map provides a visual representation of the phone number's geographical coordinates.

Technologies Used
Django: The powerful Python web framework is the backbone of the application, facilitating rapid development and clean, maintainable code.

Phonenumbers Library: Leverage the Phonenumbers library to parse and analyze phone numbers, extracting valuable information such as geographical location and carrier details.

OpenCage Geocoding API: Enhance the project with geocoding capabilities, translating phone number location data into human-readable addresses.

Folium Library: Create interactive and visually appealing maps to display the geographical location of the tracked phone number directly within the web interface.

Getting Started
To run the Phone Number Tracker locally, follow these steps:

Clone the repository:

bash
git clone https://github.com/your-username/phone-number-tracker.git
cd phone-number-tracker
Install dependencies:

bash
pip install -r requirements.txt
Run the development server:

bash
python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser to access the application.

Contributions
Contributions to the Phone Number Tracker project are welcome! Whether you want to fix bugs, implement new features, or improve documentation, please feel free to submit pull requests.

License
This project is licensed under the MIT License.

Acknowledgments
Thanks to the Django community for providing a robust web framework.
The Phonenumbers and Folium libraries for their contributions to phone number parsing and map visualization.

