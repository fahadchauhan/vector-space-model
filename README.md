# vector-space-model

The challenge was to develop an efficient information retrieval system capable of finding and ranking relevant documents within a dataset of multiple short stories stored in text files, based on their similarity to user queries.

We implemented a Vector Space Model (VSM) in Python to calculate the similarity between documents and user queries using TF-IDF (Term Frequency-Inverse Document Frequency) scores. The solution involved creating a vector representation of each document and the query, computing cosine similarities to measure their relevance, and ranking the documents accordingly. To enhance user interaction, we developed a graphical user interface (GUI) using Tkinter, allowing users to input queries and view the ranked results efficiently. The system utilized an inverted index to streamline data processing and speed up search queries.

The VSM-based retrieval system significantly improved the accuracy and efficiency of finding relevant documents from the dataset. The use of cosine similarity enabled precise document ranking, providing users with highly relevant search results. The integration of the GUI with the search engine made the interaction intuitive and streamlined, enhancing the overall user experience in querying and retrieving document information from the collection of short stories.
