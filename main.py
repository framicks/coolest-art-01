# coolest-art-01 entry: the art is coolest-art.jpg beside this file, and this
# program copies its bytes to /output/entry.png. Deterministic: the same
# bytes every run, no network, no randomness, standard library only.
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "coolest-art.jpg")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
