signatures = {'PK': 'Microsft Office Document',
              'JFIF': 'JPEG',
              'GIF': 'GIF',
              'BPS': 'PSD',
              'PNG': 'PNG',
              'II': 'TIFF',
              'BM': 'BMP',
              'PDF': 'PDF',
              }


def file_fingerprinting(path):
    try:
        with open(path, 'rb') as f:
            first_bytes = f.read(100)
            for key in signatures.keys():
                if key in str(first_bytes):
                    return (signatures[key])
                else:
                    continue
            return None
    except FileNotFoundError:
        pass
