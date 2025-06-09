import io
import spacy 

#TODO find a good place to intialize spacy
# right now im putting it here 
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("sentencizer")

def get_full_path(filename: str, relative_path: str) -> str:
    return f"{relative_path}/{filename}"

def stream_bytes_frm_path(full_path: str, buffer_size: int = 4096):
    try:
        with open(full_path, 'rb') as raw_file:
            buffered_reader = io.BufferedReader(raw_file, buffer_size=buffer_size)

            while True:
                chunk = buffered_reader.read(buffer_size)
                if not chunk:
                    break
                yield chunk
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"Error reading file '{full_path}': {e}")
        # log different based on error
        raise  e

def stream_bytes(filename: str, relative_path: str, buffer_size: int = 4096):
    full_path = get_full_path(filename, relative_path)
    return stream_bytes_frm_path(full_path, buffer_size)


#have a function call called string stream

def stream_string_chunk(filename: str , relative_path:str, decode_standard:str):
    try:
        # stream_bytes is a generator
        # inside the stream_bytes, the file is opened with "rb"
        # so it yields the bytes class 
        # the bytes class has .decode function 
        # so we could yield from the stream bytes function
        # return the decoded stream 
        for chunk in stream_bytes(filename , relative_path):
            # option for multi-threading here
            yield chunk.decode(decode_standard)


    except Exception as e:
        raise e

#then another function called sentence stream

def stream_sentence(filename: str, relative_path: str, decode_standard: str = "utf-8"):
    try:
        prev_last_sentence_buffer = ""
        obscure_char = "¶"
        for string_chunk in stream_string_chunk(filename, relative_path, decode_standard):
            string_chunk += obscure_char
            doc_list = [sent.text for sent in nlp(string_chunk).sents]

            if not doc_list:
                continue

            # Merge previous buffer into first sentence
            doc_list[0] = prev_last_sentence_buffer + doc_list[0].lstrip()

            # Handle last sentence
            prev_last_sentence_buffer = doc_list[-1]
            if prev_last_sentence_buffer == obscure_char:
                prev_last_sentence_buffer = ""
            else:
                # there is still a partial sentence at the end
                pass  # buffer remains set

            doc_list.pop()  # remove last sentence

            for sentence in doc_list:
                yield sentence

        # After all chunks processed, yield any remaining partial buffer
        if prev_last_sentence_buffer:
            doc = nlp(prev_last_sentence_buffer)
            for sentence in doc.sents:
                yield sentence.text

    except Exception as e:
        raise e


    