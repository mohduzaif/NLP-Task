import spacy


class API:

    def call_api_sementic_similarity(self, text1, text2):

        # Load the medium English model (with word vectors)
        nlp = spacy.load("en_core_web_md")

        # Example sentences
        sentence1 = text1
        sentence2 = text2

        # Process both sentences
        doc1 = nlp(sentence1)
        doc2 = nlp(sentence2)

        # Compute similarity
        similarity_score = doc1.similarity(doc2)

        if similarity_score:
            print(f"Similarity between {sentence1} and {sentence2} is: {similarity_score:.4f}")

        return f"Similarity is : {similarity_score:.4f}"

