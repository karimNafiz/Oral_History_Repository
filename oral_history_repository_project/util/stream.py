import io

def get_full_path(filename: str, relative_path: str) -> str:
    return f"{relative_path}/{filename}"

def stream_bytes_from_path(full_path: str, buffer_size: int = 4096):
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
        raise  # propagate exception to caller (good practice)

def stream_bytes(filename: str, relative_path: str, buffer_size: int = 4096):
    full_path = get_full_path(filename, relative_path)
    return stream_bytes_from_path(full_path, buffer_size)
