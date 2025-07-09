# Ayura
Modern biomedical research, especially in traditional systems like Ayurveda, often remains inaccessible to the general public due to its complex technical language and lack of personalization. In this project, we introduce Ayura, a novel persona-aligned conversational agent designed to simplify Ayurvedic biomedical literature and present it in a user-friendly, interactive format.

Our system combines Retrieval-Augmented Generation (RAG) with instruction fine-tuned GPT-4 models, each tailored to one of three distinct user personas: a layperson, a 20-year-old female, and a 65-year-old female. We create a domain-specific dataset using PubMed abstracts and generate synthetic instruction-following examples using Alpaca-style prompting with GPT-4.

The resulting fine-tuned models for each persona show improved clarity, helpfulness, and tone alignment—enhancing both accessibility and user trust. To enable real-time interactions, we deploy a FastAPI-based frontend that streams responses according to the user’s persona and query.

Our evaluation, conducted across four key dimensions—accuracy, helpfulness, persona alignment, and conversational fluency—demonstrates that Ayura successfully bridges the gap between complex Ayurvedic research and the diverse needs of everyday users.
