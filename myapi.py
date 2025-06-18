import nlpcloud


class API:

    def call_api_sementic_similarity(self, text1, text2):
        client = nlpcloud.Client("paraphrase-multilingual-mpnet-base-v2", "d4ac68d1607984d2fe23c20157d68cacb1ccba23", gpu=False)
        response = client.semantic_similarity([
                    text1,
                    text2
                    ])
        if type(response) == dict:     
            return response
        else:
            return False