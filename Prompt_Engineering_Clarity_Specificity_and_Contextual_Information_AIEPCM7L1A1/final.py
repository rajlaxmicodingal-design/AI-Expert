# ==========================================
# CHOOSE ONE PROVIDER: Change 'groq' to 'hf'
# ==========================================
provider = "groq"  # Options: 'groq' or 'hf'

if provider == "groq":
    # Replace with your actual local groq module/method
    # from groq import generate_response
    def generate_response(prompt: str) -> str:
        return f"[Groq Response] Understood: '{prompt}'"

elif provider == "hf":
    # Replace with your actual local huggingface module/method
    # from hf import generate_response
    def generate_response(prompt: str) -> str:
        return f"[Hugging Face Response] Understood: '{prompt}'"


def prompt_engineering_activity():
    print("Welcome to the AI Prompt Engineering Tutorial!")
    print(f"Active Provider backend: {provider.upper()}\n")

    vague = input("Enter a vague prompt: ")
    print("\nAI's response to vague prompt:")
    print(generate_response(vague))

    specific = input("\nNow, make it more specific: ")
    print("\nAI's response to specific prompt:")
    print(generate_response(specific))

    context = input("\nNow, add context to your specific prompt: ")
    print("\nAI's response to contextual prompt:")
    print(generate_response(context))

    print("\n--- Reflection ---")
    print(
        "1. How did the AI's response change when the prompt was made more specific?"
    )
    print("2. How did the AI's response improve with the added context?")
    print("3. Which prompt produced the most relevant and tailored response? Why?")


if __name__ == "__main__":
    prompt_engineering_activity()