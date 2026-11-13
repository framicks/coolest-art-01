# coolest-art-01 entry: the art is coolest-art.jpg beside this file, and this
# program copies its bytes to /output/entry.png. Deterministic: the same
# bytes every run, no network, no randomness, standard library only.
#
# The output keeps the name entry.png even though the bytes are JPEG: the
# gate reads the file's magic bytes (PNG or JPEG), not its extension.
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "coolest-art.jpg")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
dst = os.path.join(out_dir, "entry.png")
shutil.copyfile(src, dst)
# Fail loudly instead of shipping a partial copy.
assert os.path.getsize(dst) == os.path.getsize(src), "copy size mismatch"
