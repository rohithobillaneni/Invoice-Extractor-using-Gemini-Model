# Invoice Extractor using Gemini and Streamlit

A simple web application to extract information from invoice images using **Google Gemini** model and **Streamlit**. The application allows users to upload invoice images, process them, and get relevant data from the invoices using advanced AI models.

## Features
- **Upload Invoice Image**: Upload `.jpg`, `.jpeg`, or `.png` files.
- **Gemini Integration**: Leverages Google Gemini's AI to understand and interpret invoice data.
- **Streamlit Interface**: An easy-to-use and interactive interface for users to interact with the model.

## Front-End UI

![image](https://github.com/user-attachments/assets/b65adfab-d46c-48bb-ae58-2196bd094446)

## Output UI

![image](https://github.com/user-attachments/assets/07e35b1f-9e06-41ff-bffe-eea606064e23)


## Installation

### Prerequisites
- Python 3.9 or higher
- A Google API key for the **Gemini** model

### Step 1: Clone the Repository
```bash
git clone https://github.com/rohithobillaneni/Invoice-Extractor-using-Gemini.git
cd Invoice-Extractor-using-Gemini
```

### Step 2: Set up a Virtual Environment (optional but recommended)
```bash
python -m venv venv
```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Google API Key
Create a `.env` file in the root directory of the project and add your Google API key:
```
GOOGLE_API_KEY=your-api-key-here
```

### Step 5: Run the Streamlit App
```bash
streamlit run app.py
```

This will start the app locally, and you can view it in your browser at `http://localhost:8501`.

## Usage

1. **Input**: Provide an invoice image (.jpg, .jpeg, or .png format).
2. **Process**: The application will process the image using **Gemini** model to extract relevant information.
3. **Result**: View the extracted information and ask questions related to the invoice.

## Technologies Used
- **Google Gemini**: AI model for text generation and understanding.
- **Streamlit**: Framework for building interactive web applications.
- **Python**: Main programming language.
- **Pillow**: Image processing library.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Future Improvements
- Support for multiple invoice types and formats.
- Advanced error handling for image recognition issues.
- Enhanced user interface and experience.
