#!/usr/bin/env python3
import argparse
import urllib.request
import urllib.error
import os

def fetch_gitignore(template):
    # Fetching directly from GitHub's official gitignore repository
    url = f"https://raw.githubusercontent.com/github/gitignore/main/{template}.gitignore"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"❌ Template '{template}' not found. (Example: Python, Node, React)")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Instantly generate .gitignore files from the command line.")
    parser.add_argument("templates", nargs="+", help="Languages/Frameworks (e.g., Python Node)")
    parser.add_argument("-o", "--output", default=".gitignore", help="Output file name (default: .gitignore)")
    
    args = parser.parse_args()
    
    print("🌐 Fetching templates...")
    combined_content = ""
    
    for tmpl in args.templates:
        # GitHub templates usually start with a capital letter (e.g., Python.gitignore)
        formatted_tmpl = tmpl.capitalize()
        print(f"  -> Fetching {formatted_tmpl}...")
        content = fetch_gitignore(formatted_tmpl)
        if content:
            combined_content += f"\n\n### {formatted_tmpl} ###\n\n"
            combined_content += content
            
    if combined_content.strip():
        mode = "a" if os.path.exists(args.output) else "w"
        with open(args.output, mode) as f:
            f.write(combined_content)
        action = "Appended to" if mode == "a" else "Created"
        print(f"\n✅ Success! {action} '{args.output}'")
    else:
        print("\n⚠️ No valid templates fetched. Nothing was saved.")

if __name__ == "__main__":
    main()
