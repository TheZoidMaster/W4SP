import os
import re
import json


def extract_info(file_path):
    global wiki_dir

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    info = {}
    yaml_match = re.match(r"^\s*---\s*(.*?)\s*---", content, re.DOTALL)
    if yaml_match:
        frontmatter = yaml_match.group(1)
        for line in frontmatter.splitlines():
            kv = re.match(r"\s*(\w+)\s*:\s*(.+)", line)
            if kv:
                key = kv.group(1).lower()
                value = kv.group(2).strip()
                if key in ['title', 'blurb', 'image']:
                    info[key] = value

    if 'title' not in info:
        title_match = re.search(
            r"\|\s*title\s*\|\s*(.*?)\s*\|", content, re.IGNORECASE)
        if title_match:
            info["title"] = title_match.group(1)
        else:
            header_match = re.search(r"^#\s*(.+)", content, re.MULTILINE)
            info["title"] = header_match.group(
                1) if header_match else os.path.splitext(os.path.basename(file_path))[0]

    if 'blurb' not in info:
        blurb_match = re.search(
            r"\|\s*blurb\s*\|\s*(.*?)\s*\|", content, re.IGNORECASE)
        if blurb_match:
            info["blurb"] = blurb_match.group(1)

    if 'image' not in info:
        image_match = re.search(
            r"\|\s*image\s*\|\s*(.*?)\s*\|", content, re.IGNORECASE)
        if image_match:
            info["image"] = image_match.group(1)

    page = os.path.relpath(file_path, wiki_dir).replace("\\", "/")
    page = os.path.splitext(page)[0]
    info["page"] = page
    return info


def main():
    global wiki_dir

    wiki_dir = "./wiki"
    output = "./index.json"

    entries = []
    for root, _, files in os.walk(wiki_dir):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                entry = extract_info(full_path)
                entries.append(entry)

    with open(output, "w", encoding="utf-8") as out_file:
        json.dump(entries, out_file, indent=4)


if __name__ == "__main__":
    main()
