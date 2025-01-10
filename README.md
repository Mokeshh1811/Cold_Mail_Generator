# Cold Email Generator

A streamlined and efficient Cold Email Generator built using **Llama 3.2 3B** model and **LangChain** modules, hosted locally with **Streamlit**. This tool is designed to assist Business Development Executives (BDEs) in crafting professional and personalized cold emails effortlessly.

## Features
- **AI-Powered Email Generation**: Utilizes Llama 3.2 3B model for generating contextually relevant and engaging email content.
- **LangChain Integration**: Seamlessly manages prompt creation and response handling.
- **User-Friendly Interface**: Developed with Streamlit for an intuitive and responsive user experience.

## Requirements
Ensure you have the following installed before setting up the project:

- Python 3.8 or above
- pip (Python package installer)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/cold-email-generator.git
   cd cold-email-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and set up the Llama 3.2 3B model. Follow the instructions for acquiring the model weights and placing them in the appropriate directory as specified in the project configuration.

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the local Streamlit interface in your web browser at:
   ```
   http://localhost:8501
   ```

3. Input the necessary details (e.g., recipient name, company details, purpose) to generate a cold email tailored to your needs.

## Project Structure
```
.
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── models/             # Directory for Llama model weights
├── modules/            # Contains LangChain configurations
└── utils/              # Helper functions and utilities
```

## Dependencies
- **Llama 3.2 3B**
- **LangChain**
- **Streamlit**

Refer to the `requirements.txt` file for a complete list of dependencies.

## Contribution
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to improve this project.

## License
This project is licensed under the [Apache License 2.0](LICENSE).

## Acknowledgments
Special thanks to the open-source community and the developers of Llama, LangChain, and Streamlit for their amazing tools and frameworks.
