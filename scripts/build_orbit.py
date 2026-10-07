#!/usr/bin/env python3
"""Builds assets/orbit.svg. If assets/profile.png|jpg|jpeg|webp exists, it is embedded
(base64) in the centre so it renders on GitHub (SVGs shown via <img> cannot load
external images). Run from the repo root:  python3 scripts/build_orbit.py"""
import base64, math, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
A = "#1F9DD4"
W, H, CX, CY = 860, 540, 430, 270
INNER = ["React", "Next.js", "TypeScript", "Node.js", "Express"]
OUTER = ["Redux Toolkit", "Tailwind", "PostgreSQL", "Prisma", "MongoDB", "Mongoose", "Git"]

def pill(label, fill):
    w = 14 + len(label) * 7.6
    return (f'<rect x="{-w/2:.1f}" y="-13" width="{w:.1f}" height="26" rx="13" fill="{fill}"/>'
            f'<text x="0" y="4.5" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">{label}</text>')

def ring(items, r, dur, clockwise, fill):
    out = []
    sgn = 1 if clockwise else -1
    a0, a1 = (0, 360) if clockwise else (360, 0)
    out.append(f'<g><animateTransform attributeName="transform" type="rotate" from="{a0}" to="{a1}" dur="{dur}s" repeatCount="indefinite"/>')
    for i, label in enumerate(items):
        ang = 360 / len(items) * i + (0 if clockwise else 20)
        c0, c1 = -ang, -ang - sgn * 360
        out.append(f'<g transform="rotate({ang:.1f})"><g transform="translate({r},0)"><g>'
                   f'<animateTransform attributeName="transform" type="rotate" from="{c0:.1f}" to="{c1:.1f}" dur="{dur}s" repeatCount="indefinite"/>'
                   f'{pill(label, fill)}</g></g></g>')
    out.append('</g>')
    return "".join(out)

img = next((p for e in ("png","jpg","jpeg","webp") for p in [root/"assets"/f"profile.{e}"] if p.exists()), None)
if img:
    mime = {"png":"image/png","jpg":"image/jpeg","jpeg":"image/jpeg","webp":"image/webp"}[img.suffix[1:]]
    b64 = base64.b64encode(img.read_bytes()).decode()
    centre = (f'<clipPath id="c"><circle r="62"/></clipPath>'
              f'<image href="data:{mime};base64,{b64}" x="-62" y="-62" width="124" height="124" preserveAspectRatio="xMidYMid slice" clip-path="url(#c)"/>')
else:
    centre = f'<circle r="62" fill="{A}" fill-opacity=".15"/><text y="12" text-anchor="middle" font-size="34" font-weight="700" fill="{A}">MD</text>'

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Md Rubel with the technologies he works with orbiting around him" font-family="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">
<g transform="translate({CX},{CY})">
<circle r="140" fill="none" stroke="{A}" stroke-opacity=".35" stroke-dasharray="3 6"/>
<circle r="250" fill="none" stroke="{A}" stroke-opacity=".25" stroke-dasharray="3 6"/>
{ring(OUTER, 250, 70, False, "#5b6b7a")}
{ring(INNER, 140, 48, True, A)}
<circle r="68" fill="none" stroke="{A}" stroke-width="3"/>
{centre}
<rect x="-46" y="78" width="92" height="26" rx="13" fill="{A}"/>
<text y="96" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">Md Rubel</text>
</g></svg>'''
(root/"assets"/"orbit.svg").write_text(svg)
print("orbit.svg written;", "profile image embedded" if img else "no assets/profile.* found, using MD placeholder")
