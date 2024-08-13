# Board Games FAQ

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ofRC5td5rYFlonUKfXhbWmAFJu4RLIR8?usp=sharing)

This project demonstrates how to build a smart chatbot for board games using a Large Language Model (LLM) and implement Retrieval Augmented Generation (RAG) with the LangChain framework. The chatbot reads rulebooks and leverages Google's latest language model namely Google Gemini 1.5 Flash to provide accurate answers to questions about the games.

## Key Achievements:

- Intelligent Game Assistant: Transforms static rulebooks into an interactive knowledge base, making it easier for players to quickly clarify rules and resolve gameplay disputes.
- LangChain Integration: Showcases the effective use of LangChain for document loading, text splitting, embedding, and seamless interaction with LLMs.
- Google Gemini 1.5 Flash: Harnesses the advanced capabilities of this state-of-the-art language model for superior natural language understanding and response generation.

## How It's Helpful:

- Enhances the Gaming Experience: Empowers players to focus on enjoying the game rather than getting bogged down in rulebook searches.
- Learning Tool: Aids in understanding complex game mechanics by providing clear explanations on demand.
- Community Building: Fosters a more inclusive gaming environment by lowering the barrier to entry for new players.
- Educational Resource: Serves as a practical example of how to build LLM-powered applications using LangChain and Google Colab.
- This application currently supports the following games:
    - Catan base game & 5-6 player expansion
    - Codenames
    - Pandemic
    - Monopoly
    - Ticket to Ride base game & expansions

    ## How to Run It:

- Open the notebook in Google Colab [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ofRC5td5rYFlonUKfXhbWmAFJu4RLIR8?usp=sharing).
- Install the necessary libraries by running the provided code cell.
- Upload the provided board game rulebook PDFs to the designated folder (you can include your own PDFs too)
- Execute the remaining code cells sequentially.
- Test the app by entering your questions in the provided input field.

## Future Scope:

- Multi-Format Support: Extend the app to handle rulebooks in various formats (e.g., .txt, .docx).
- Enhanced UI: Develop a more interactive and user-friendly interface within Colab itself.
- Advanced NLP: Incorporate techniques like named entity recognition and relation extraction for even more nuanced query understanding.
- Deployment: Deploy the app to the web using Streamlit or other cloud platforms to make it publicly accessible.
- Game-Specific Features: Tailor the app to specific games or genres, offering features like turn summaries or strategy suggestions.
