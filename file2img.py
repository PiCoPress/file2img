def file_to_image(file: str, out: str):
    import numpy as np
    import random
    import math
    from PIL import Image
    arr = bytearray(open(file, "rb").read())
    reall = len(arr)
    sq = math.ceil(reall ** 0.5)
    ft = math.ceil(sq /2)
    arr.extend(0 for _ in range((ft ** 2) * 4 - reall))
    Image.fromarray(
    np.array(arr).reshape(
    (ft, ft, 4)), "RGBA").save(out)
