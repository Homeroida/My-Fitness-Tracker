# My Fitness Tracker

#### This is a Python-based fitness tracker application that allows users to log their workouts and track their progress. The application uses the Nutritionix API to identify exercises and calculate calories burned, and stores the user's workout data in a Google Sheet.

## How to Use

#### To use this application, follow these steps:

1. Clone the repository to your local machine.
2. Install the required packages by running pip install -r requirements.txt.
3. Obtain the necessary API keys and tokens:

- Sign up for a free account on [Nutritionix](https://www.nutritionix.com/) and obtain your API ID and API key.
- Obtain a Google Sheets API token by following the instructions on the [Google Sheets API documentation](https://developers.google.com/sheets/api/guides/authorizing).

4. Create a .env file in the root directory of the project and add the following environment variables:
   `APP_ID=your_nutritionix_api_id API_KEY=your_nutritionix_api_key SHEET_TOKEN=your_google_sheets_api_token`
5. Run the application by executing the main.py file in your Python environment (python main.py).
6. Follow the prompts to enter your workout details and save them to the Google Sheet.

# Contact

#### If you have any questions or issues with this application, please contact me at chanishvili@gmail.com.
