import os
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

def get_staged_diff():
    """Fetches the staged git diff."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--cached'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except FileNotFoundError:
        print("Error: 'git' command not found. Is Git installed and in your PATH?")
        return None
    except subprocess.CalledProcessError:
        return None

def generate_commit_message(diff):
    """Generates a commit message using the Gemini API."""
    # API key is configured globally in main(), so no need to load here
    try:
        model = genai.GenerativeModel('gemini-2.5-flash') # Use GenerativeModel directly
        
        prompt = f"""
        Analyze the following git diff and generate a concise, conventional commit message.
        The message should follow the Conventional Commits specification.
        Do not include the diff in your response, only the commit message.

        Format: <type>[optional scope]: <description>

        [optional body]

        ---
        GIT DIFF:
        {diff}
        """

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print(f"Error generating commit message: {e}")
        return None

def git_commit(message):
    """Executes the git commit command."""
    try:
        subprocess.run(['git', 'commit', '-m', message], check=True)
        print("\nCommit successful!")
    except subprocess.CalledProcessError as e:
        print(f"\nError committing: {e}")
    except FileNotFoundError:
        print("Error: 'git' command not found.")

def main():
    """Main function for the CommitCraft tool."""
    diff = get_staged_diff()
    if not diff:
        print("No staged changes found to commit.")
        return

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or api_key == "YOUR_API_KEY":
        print("Error: GEMINI_API_KEY not found or not set in .env file.")
        print("Please copy .env.example to .env and set your API key.")
        return
    
    genai.configure(api_key=api_key) # Configure globally at the start of main
    
    print("🤖 Generating commit message...")

    commit_message = generate_commit_message(diff)

    if not commit_message:
        print("❌ Could not generate a commit message.")
        return

    print("\n✨ Suggested Commit Message:")
    print("-" * 30)
    print(commit_message)
    print("-" * 30)

    while True:
        choice = input("Use this message? (y/n/e) [y]: ").lower()
        if choice in ['y', 'yes', '']:
            git_commit(commit_message)
            break
        elif choice in ['n', 'no']:
            print("Commit aborted.")
            break
        elif choice in ['e', 'edit']:
            # TODO: Implement editing functionality
            print("Editing is not implemented yet. Aborting.")
            break
        else:
            print("Invalid choice. Please enter 'y', 'n', or 'e'.")


if __name__ == "__main__":
    main()