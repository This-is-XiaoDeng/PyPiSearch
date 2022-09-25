def get_center(text, start, end):
    start_len = text.find(start)
    if start_len >= 0:
        start_len += start.__len__()
        end_len = text.find(end, start_len)
        return text[start_len:end_len]
    else:
        return None
