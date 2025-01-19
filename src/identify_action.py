import google.generativeai as genai
from dotenv import load_dotenv  # type: ignore
import os

load_dotenv()

# configure genai api
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

class IdentifyAction:
    def __init__(self):
        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

    def identify_action(self, text):
        prompt = f"""
            Analyze the following text: "{text}".
            Identify the user's action and the corresponding task. The possible actions are:
            - "add": For adding an item to a list.
            - "remove": For removing an item from a list.
            - "view": For viewing the list or its contents.

            If the action matches "add" or "remove", extract the item name being referenced.
            If the action matches "view", set the task as "view list" or "see item" depending on context.
            If none of the actions apply, return "unknown" for the action.

            Provide the response as a list in the format: ["action", "task"].
            Examples:
            - Input: "I want to add apples to the list" => Output: ["add", "apples"]
            - Input: "remove bananas from the list" => Output: ["remove", "bananas"]
            - Input: "Can I see my list?" => Output: ["view", "list"]
            - Input: "What is on my list?" => Output: ["view", "item"]
            - Input: "random input that doesn't match" => Output: ["unknown", "unknown"]

            Respond with only the action and task in the specified format.
        """

        response = self.model.generate_content(prompt)
        return response.text

