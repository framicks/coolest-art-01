# coolest-art-01 — Neon Ringed Planet

Entry for the [make.fun](https://make.fun/bounty/coolest-art-01) coolest-art-01
bounty ($250 pool, top 20 share the prizes).

## What it is

A lone astronaut standing on a cliff edge before an enormous glowing ringed
planet — bold neon-purple palette, a strong clear silhouette, dramatic rim
light. The art is `coolest-art.jpg` (1024x683, JPEG, 183 KB).

## How it runs

`main.py` (Python 3.13, standard library only) copies `coolest-art.jpg`
byte for byte to `/output/entry.png`. The same bytes every run: no network,
no randomness, no drawing — the image is the entry.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is `out/entry.png`, byte-identical to `coolest-art.jpg`.

## License

MIT — see [LICENSE](LICENSE).
