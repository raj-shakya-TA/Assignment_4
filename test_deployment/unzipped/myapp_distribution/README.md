MyApp
A simple command-line application that greets the user.
Installation
Prerequisites

Python 3.8 or higher
Conda (for environment setup)

Step 1: Set Up the Conda Environment

Ensure you have Conda installed.
Create a new Conda environment using the provided env.yml:conda env create -f env.yml


Activate the environment:conda activate myapp_env



Step 2: Install the Package
You can install myapp using either the wheel (.whl) or source distribution (.tar.gz) file provided in the distribution archive.
Option 1: Install via Wheel
pip install dist/myapp-0.3.0-py3-none-any.whl

Option 2: Install via Source Distribution
pip install dist/myapp-0.3.0.tar.gz

Step 3: Test the Installation
Run the test script to verify the installation:
python tests/test_install.py

If successful, you should see output indicating that the greet function works as expected.
Running the Application
After installation, you can run the application using the command-line interface:
myapp YourName

Example output:
Hello, YourName! Welcome to myapp.

If no name is provided:
myapp

Output:
Hello, User! Welcome to myapp.

Configuration

Logging: By default, no logging is configured. To enable logging, modify main.py to include logging configuration as needed.
Customization: The greeting message can be customized by editing the greet function in myapp/main.py.

Troubleshooting

Ensure the Conda environment is activated before running commands.
Check that the correct Python version (3.8+) is used in the environment.
Logs: Currently, no logs are generated. Add logging to main.py if needed.

License
This project is licensed under the MIT License. See the LICENSE file for details.
