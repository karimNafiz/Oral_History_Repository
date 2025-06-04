from util import stream
class Corpus:
    def __init__(self,id:int, filename:str , relative_path:str):
        self.id = id 
        self._filename = filename
        self._relative_path = relative_path
    

    def get_corpus(self, filename:str, relative_path:str):
        # internally call the utility fucntion 
        # return the bytes in the format this corpus object should return
        # return the generator expression 
        return stream.stream_bytes(filename , relative_path)