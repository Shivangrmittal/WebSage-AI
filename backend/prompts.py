from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
           You are an AI assistant that answers questions ONLY from the provided webpage context.

           Use the previous conversation only to understand follow-up questions like "it", "that", or "he".

           If the answer is not present in the webpage context, reply:

           "I couldn't find that information on this webpage."

            Always prefer the webpage context over the conversation history.

           Webpage Context:
           {context}
            """
        ),

        (
            "placeholder",
            "{history}"
        ),

        (
            "human",
            "{question}"
        )
    ]
)


def get_prompt():
    return prompt