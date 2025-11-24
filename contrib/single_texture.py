#!/usr/bin/env python3
"""
Outputs a single block texture by blockid and optionally data value.
"""

import argparse
import sys
import os

# incantation to be able to import overviewer_core
if not hasattr(sys, "frozen"):
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0], '..')))


def main(blockid, data, outfile, texturepath=None):
    from overviewer_core import textures

    # Check if the blockid is valid
    if blockid >= textures.max_blockid:
        print(f"Error: blockid {blockid} is out of range (max: {textures.max_blockid - 1})", file=sys.stderr)
        return 1

    # Check if the data value is valid
    if data >= textures.max_data:
        print(f"Error: data value {data} is out of range (max: {textures.max_data - 1})", file=sys.stderr)
        return 1

    # Check if there's a generator for this block/data combination
    if (blockid, data) not in textures.blockmap_generators:
        print(f"Error: No texture generator found for blockid {blockid} with data {data}", file=sys.stderr)
        print(f"Available generators: {len(textures.blockmap_generators)}", file=sys.stderr)
        return 1

    # Create a minimal textures object
    t = textures.Textures(texturepath=texturepath)

    # Only load the color maps if they might be needed (try/catch to handle missing files gracefully)
    try:
        t.load_foliage_color()
        t.load_grass_color()
    except textures.TextureException:
        # Some blocks don't need these, so it's okay if they're missing
        pass

    # Get the specific generator for this block/data
    texgen = textures.blockmap_generators[(blockid, data)]

    # Generate only this specific texture
    tex = texgen(t, blockid, data)

    if tex is None:
        print(f"Error: Texture generator returned None for blockid {blockid} with data {data}", file=sys.stderr)
        return 1

    # Convert to texture tuple format (image, mask)
    tex_tuple = t.generate_texture_tuple(tex)

    # Save the texture (tex_tuple[0] is the actual image)
    tex_tuple[0].save(outfile)
    print(f"Saved texture for blockid {blockid} (data: {data}) to {outfile}")
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('blockid', type=int, help='Block ID to extract')
    parser.add_argument('--data', '-d', type=int, default=0, help='Data value (default: 0)')
    parser.add_argument('--output', '-o', type=str, default='block_texture.png',
                        help='Output file path (default: block_texture.png)')
    parser.add_argument('--texturepath', '-t', type=str, default=None,
                        help='Path to custom textures (resource pack or directory)')
    args = parser.parse_args()

    exit_code = main(args.blockid, args.data, args.output, args.texturepath)
    sys.exit(exit_code)

