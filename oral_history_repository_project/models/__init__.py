class Corpus:
    def __init__(self, filename:str , relative_path:str):
        self._filename = filename
        self._relative_path = relative_path
    

    def get_corpus(self, filename:str, relative_path:str):
        # internally call the utility fucntion 
        # return the bytes in the format this corpus object should return
        pass