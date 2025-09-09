import base64, pathlib, sys
if len(sys.argv)<2 or sys.argv[1] not in ('3.13','3.12'):
    print('Usage: python rebuild_wheels.py 3.13|3.12'); raise SystemExit(1)
v = sys.argv[1]
src = pathlib.Path(f'wheelhouse-{v}-b64')
dst = pathlib.Path(f'wheelhouse-{v}'); dst.mkdir(exist_ok=True)
for b in sorted(src.glob('*.b64')):
    out = dst / b.name[:-4]
    out.write_bytes(base64.b64decode(b.read_bytes()))
    print('Wrote', out)
print(f'\nNow run:\n  python -m pip install --no-index --find-links wheelhouse-{v} protobuf google notebook jupyter ipykernel colorama pywinpty pywin32')
