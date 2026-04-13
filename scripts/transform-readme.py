#!/usr/bin/env python3
"""Transform awesome-nafarroa README entries with metadata (stars, license, language, institution tags, demos)."""

import json
import re
import sys

# Load metadata
with open("scripts/metadata.json") as f:
    metadata = json.load(f)

# Section -> default institution/location tags
SECTION_TAGS = {
    "Cartografía y Catastro": ["GobNav"],
    "Cultura y Patrimonio": [],
    "Datos Abiertos y Estadísticas": ["GobNav"],
    "Medio Ambiente y Urbanismo": [],
    "Transparencia y Gobierno Abierto": ["GobNav"],
}

# Keyword -> tag overrides/additions (applied per-entry based on name + description)
KEYWORD_TAGS = {
    "GobNav": "GobNav",
    "Gobierno de Navarra": "GobNav",
    "Gobierno Foral": "GobNav",
    "gobierno foral": "GobNav",
    "Nafarroako Gobernua": "GobNav",
    "navarra.es": "GobNav",
    "SITNA": "SITNA",
    "Sistema de Información Territorial": "SITNA",
    "Catastro de Navarra": "Catastro",
    "catastro navarra": "Catastro",
    "CatastRoNav": "Catastro",
    "cadastre": "Catastro",
    "UPNA": "UPNA",
    "Universidad Pública de Navarra": "UPNA",
    "NUP": "UPNA",
    "UNAV": "UNAV",
    "Universidad de Navarra": "UNAV",
    "TECNUN": "UNAV",
    "NASTAT": "NASTAT",
    "Instituto de Estadística": "NASTAT",
    "Tracasa": "Tracasa",
    "SODENA": "SODENA",
    "Pamplona": "Pamplona",
    "Iruña": "Pamplona",
    "Tudela": "Tudela",
    "Estella": "Estella",
    "Lizarra": "Estella",
    "Tafalla": "Tafalla",
    "Barañáin": "Barañáin",
    "Osasuna": "Osasuna",
    "Osasunbidea": "Osasunbidea",
    "Servicio Navarro de Salud": "Osasunbidea",
    "SNS-O": "Osasunbidea",
    "Bardenas": "Bardenas",
    "Bardenas Reales": "Bardenas",
    "San Fermín": "Sanfermines",
    "Sanfermines": "Sanfermines",
    "sanfermines": "Sanfermines",
    "euskera": "Euskera",
    "Euskera": "Euskera",
    "Gorosti": "Gorosti",
    "SCN Gorosti": "Gorosti",
    "megalíticas": "Gorosti",
    "Civio": "Civio",
    "presupuesto": "Civio",
    "COVID-19": "COVID-19",
    "COVID": "COVID-19",
    "covid": "COVID-19",
    "QGIS": "QGIS",
}

# Tag -> URL for clickable badges
TAG_URLS = {
    "GobNav": "https://www.navarra.es/",
    "SITNA": "https://sitna.navarra.es/",
    "Catastro": "https://catastro.navarra.es/",
    "UPNA": "https://www.unavarra.es/",
    "UNAV": "https://www.unav.edu/",
    "NASTAT": "https://www.navarra.es/es/gobierno-de-navarra/instituto-de-estadistica",
    "Tracasa": "https://www.tracasa.es/",
    "SODENA": "https://www.sodena.com/",
    "Pamplona": "https://www.pamplona.es/",
    "Tudela": "https://www.tudela.es/",
    "Estella": "https://www.estella-lizarra.com/",
    "Tafalla": "https://www.tafalla.es/",
    "Barañáin": "https://www.baranain.es/",
    "Osasuna": "https://www.osasuna.es/",
    "Osasunbidea": "https://www.navarra.es/es/gobierno-de-navarra/salud",
    "Bardenas": "https://www.bardenasreales.es/",
    "Sanfermines": "https://sanfermin.pamplona.es/",
    "Euskera": "https://www.navarra.es/es/gobierno-de-navarra/euskera",
    "Gorosti": "https://www.gorosti.org/",
    "Civio": "https://civio.es/",
    "COVID-19": "https://www.who.int/emergencies/diseases/novel-coronavirus-2019",
    "QGIS": "https://qgis.org/",
}

# Normalize language names
LANG_MAP = {
    "Jupyter Notebook": "Python",
    "GLSL": None,
    "Makefile": None,
    "Dockerfile": None,
    "Shell": None,
    "Batchfile": None,
    "Nix": None,
    "CMake": None,
    "Smarty": "PHP",
    "Mustache": "JavaScript",
    "Vue": "JavaScript",
    "Svelte": "JavaScript",
    "CSS": None,
    "SCSS": None,
    "Sass": None,
    "Less": None,
    "Roff": None,
    "PLpgSQL": "SQL",
    "TSQL": "SQL",
    "HCL": "Terraform",
    "Gherkin": None,
    "Groovy": "Java",
    "Scala": "Scala",
    "Elixir": "Elixir",
    "Erlang": "Erlang",
    "Haskell": "Haskell",
    "Lua": "Lua",
    "Perl": "Perl",
    "Dart": "Dart",
    "Swift": "Swift",
    "Objective-C": "Objective-C",
    "Assembly": None,
    "Fortran": "Fortran",
    "Mathematica": None,
    "TeX": None,
    "Jinja": "Python",
    "Starlark": None,
    "Handlebars": "JavaScript",
}

# License normalization
LICENSE_MAP = {
    "NOASSERTION": None,
    "0BSD": "0BSD",
}

# Demo URLs for known projects
DEMO_URLS = {}


def encode_tag(tag):
    """Encode tag name for shields.io badge URL."""
    return tag.replace("-", "--").replace("_", "__").replace(" ", "%20").replace("+", "%2B")


def get_navarra_tags(section_name, entry_name, description):
    """Determine institution/location tags for an entry."""
    tags = set()

    # Add section defaults
    if section_name in SECTION_TAGS:
        tags.update(SECTION_TAGS[section_name])

    # Scan description + name for keyword matches
    text = f"{entry_name} {description}"
    for keyword, tag in KEYWORD_TAGS.items():
        if keyword in text:
            tags.add(tag)

    # Remove overly broad "GobNav" tag if more specific tags are present
    specific_navarra = {"SITNA", "Catastro", "UPNA", "UNAV", "NASTAT", "Tracasa", "SODENA", "Pamplona", "Tudela", "Estella", "Tafalla", "Osasuna", "Osasunbidea", "Bardenas"}
    if "GobNav" in tags and tags & specific_navarra:
        tags.discard("GobNav")

    return sorted(tags)


def get_language(owner_repo):
    """Get normalized language for a repo."""
    meta = metadata.get(owner_repo, {})
    lang = meta.get("language", "")
    if not lang:
        return None
    if lang in LANG_MAP:
        return LANG_MAP[lang]
    return lang


def get_license(owner_repo):
    """Get license SPDX ID for a repo."""
    meta = metadata.get(owner_repo, {})
    lic = meta.get("license", "")
    if not lic:
        return None
    if lic in LICENSE_MAP:
        return LICENSE_MAP[lic]
    return lic


def get_default_branch(owner_repo):
    """Get default branch for a repo."""
    meta = metadata.get(owner_repo, {})
    return meta.get("default_branch", "main")


def get_demo_url(owner_repo):
    """Get demo URL if available."""
    return DEMO_URLS.get(owner_repo)


def transform_entry(line, current_section):
    """Transform a single entry line with metadata."""
    # Badge patterns: handle both clickable [![alt](img)](link) and plain ![alt](img)
    badge_pat = r'(?:\[!\[[^\]]*\]\([^)]+\)\]\([^)]+\)|!\[[^\]]*\]\([^)]+\))'
    demo_pat = r'\(\[Demo\]\([^)]+\)\)'

    m = re.match(
        rf'^- \[([^\]]+)\]\((https://github\.com/([^)]+))\)\s+'
        rf'(?:{badge_pat}\s*)*'
        rf'(?:{demo_pat}\s*)?'
        rf'- (.+)$',
        line
    )
    if not m:
        m = re.match(r'^- \[([^\]]+)\]\((https://github\.com/([^)]+))\) - (.+)$', line)
    if not m:
        return line

    name = m.group(1)
    url = m.group(2)
    owner_repo = m.group(3)
    raw_desc = m.group(4)

    # Strip any existing backtick tags and demo links from description
    description = re.sub(r'\s*\(\[Demo\]\([^)]+\)\)', '', raw_desc)
    description = re.sub(r'\s*`[^`]+`', '', description).strip()

    # Clickable auto-updating shields.io badges
    branch = get_default_branch(owner_repo)
    star_badge = f"[![Stars](https://img.shields.io/github/stars/{owner_repo}?style=flat-square&label=%E2%AD%90)](https://github.com/{owner_repo}/stargazers)"
    commit_badge = f"[![Last Commit](https://img.shields.io/github/last-commit/{owner_repo}?style=flat-square)](https://github.com/{owner_repo}/commits/{branch})"
    lang_badge = f"[![Language](https://img.shields.io/github/languages/top/{owner_repo}?style=flat-square)](https://github.com/{owner_repo})"
    license_badge = f"[![License](https://img.shields.io/github/license/{owner_repo}?style=flat-square)](https://github.com/{owner_repo}/blob/{branch}/LICENSE)"

    # Institution/location tags as clickable Navarra red badges
    navarra_tags = get_navarra_tags(current_section, name, raw_desc)
    tag_badge_parts = []
    for t in navarra_tags:
        encoded = encode_tag(t)
        if t in TAG_URLS:
            tag_badge_parts.append(
                f"[![{t}](https://img.shields.io/badge/{encoded}-D5232A?style=flat-square)]({TAG_URLS[t]})"
            )
        else:
            tag_badge_parts.append(
                f"![{t}](https://img.shields.io/badge/{encoded}-D5232A?style=flat-square)"
            )
    tag_badges = " ".join(tag_badge_parts)

    # Demo link
    demo = get_demo_url(owner_repo)
    demo_str = f" ([Demo]({demo}))" if demo else ""

    # Build: Name + clickable auto-badges + institution tags + demo + description
    parts = [f"- [{name}]({url}) {star_badge} {commit_badge} {lang_badge} {license_badge}"]
    if tag_badges:
        parts[0] += f" {tag_badges}"
    if demo_str:
        parts[0] += demo_str
    parts[0] += f" - {description}"

    return parts[0]


def main():
    with open("README.md") as f:
        lines = f.readlines()

    output = []
    current_section = ""

    for line in lines:
        stripped = line.rstrip("\n")

        # Track current section
        section_match = re.match(r'^## (.+)$', stripped)
        if section_match:
            current_section = section_match.group(1)

        # Transform entry lines
        if stripped.startswith("- [") and "github.com/" in stripped and "](#" not in stripped:
            transformed = transform_entry(stripped, current_section)
            output.append(transformed + "\n")
        else:
            output.append(line)

    with open("README.md", "w") as f:
        f.writelines(output)

    print(f"Transformed README.md")


if __name__ == "__main__":
    main()
