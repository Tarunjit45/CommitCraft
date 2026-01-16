# CommitCraft 🤖✨

**`CommitCraft` is a lightweight CLI tool that uses the power of AI to automatically generate your git commit messages.**

Tired of writing commit messages? Let AI do it for you! `CommitCraft` reads your staged changes, understands the context, and crafts a perfect, conventional commit message in seconds.

---

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Tarunjit45/CommitCraft.git
    cd CommitCraft
    ```
2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🔑 Configuration

1.  **Obtain a Google Gemini API Key:**
    *   Go to [Google AI Studio](https://ai.google.dev/) and create a new API key.
2.  **Set the API Key:**
    *   Copy the `.env.example` file to a new file named `.env`:
        ```bash
        cp .env.example .env
        ```
    *   Open the `.env` file and replace `"YOUR_API_KEY"` with your actual Google Gemini API Key:
        ```
        GEMINI_API_KEY="your_actual_gemini_api_key_here"
        ```

## Usage

1.  **Stage your changes:**
    ```bash
    git add .
    ```
2.  **Run CommitCraft:**
    ```bash
    python commitcraft.py
    ```
3.  **Review and confirm:**
    `CommitCraft` will suggest a commit message. You can choose to:
    *   `y` (yes): Accept and commit with the suggested message.
    *   `n` (no): Abort the commit.
    *   `e` (edit): *(Currently not implemented, aborts commit)*

---

## ⚠️ Known Issue: Deprecation Warning

You might see a `FutureWarning` related to the `google.generativeai` package. This is due to ongoing changes in Google's AI SDKs. While the tool functions correctly, this warning indicates that the package may be replaced by `google.genai` in the future. This project will be updated to the new SDK once a stable and reliable migration path is confirmed.

---

## Contributing

Contributions are welcome! Please feel free to open issues or pull requests.

## License

*(License information will be added here.)*
