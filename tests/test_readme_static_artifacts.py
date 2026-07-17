"""Static validation tests for GitHub profile README deliverables."""

from __future__ import annotations

import re
from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path("/app")
README_PATH = ROOT / "README.md"

EXPECTED_LOCAL_FILES = [
    "assets/hero.svg",
    "assets/identity-console.svg",
    "assets/mission-control.svg",
    "assets/product-education.svg",
    "assets/product-marketplace.svg",
    "assets/product-enterprise.svg",
    "assets/engineering-principles.svg",
    "assets/tech-radar.svg",
    "assets/roadmap.svg",
    "assets/timeline.svg",
    "assets/footer.svg",
    "diagrams/product-system.mmd",
    "diagrams/learning-graph.mmd",
]

FORBIDDEN_PATTERNS = [
    r"(?i)visitor\s*counter",
    r"(?i)trophy",
    r"(?i)github\s*stats",
    r"(?i)streak\s*stats",
    r"(?i)snake",
    r"https?://[^\s\)]*shields\.io",
    r"https?://raw\.githubusercontent\.com",
]


def _readme_text() -> str:
    return README_PATH.read_text(encoding="utf-8")


def _extract_local_references(markdown: str) -> list[str]:
    # HTML img/src and anchor href
    html_refs = re.findall(r'(?:src|href)="(\./[^"\n]+)"', markdown)
    # Markdown image/link refs
    md_refs = re.findall(r"\[[^\]]*\]\((\./[^\)\n]+)\)", markdown)
    refs = sorted(set([*html_refs, *md_refs]))
    return [r[2:] if r.startswith("./") else r for r in refs]


def test_readme_exists_and_not_empty():
    """README should exist and contain substantial authored content."""
    assert README_PATH.exists(), "README.md missing"
    text = _readme_text()
    assert len(text.splitlines()) >= 250
    assert "placeholder" not in text.lower()
    assert "todo" not in text.lower()


def test_expected_local_files_exist():
    """All requested local assets and Mermaid source files should exist."""
    missing = [f for f in EXPECTED_LOCAL_FILES if not (ROOT / f).exists()]
    assert not missing, f"Missing local deliverables: {missing}"


def test_readme_local_references_resolve():
    """README local references should map to actual files."""
    refs = _extract_local_references(_readme_text())
    missing = [ref for ref in refs if not (ROOT / ref).exists()]
    assert not missing, f"Broken local references: {missing}"
    assert len(refs) >= 13


def test_svg_files_parse_as_xml_and_are_self_contained():
    """SVGs should be XML-valid and avoid external dependencies/scripts."""
    svg_paths = list((ROOT / "assets").glob("*.svg"))
    assert len(svg_paths) >= 11

    for svg_file in svg_paths:
        content = svg_file.read_text(encoding="utf-8")
        ET.fromstring(content)
        assert "<script" not in content.lower(), f"Script tag found in {svg_file.name}"

        # Allow SVG namespace declaration but block all other external URLs.
        cleaned = content.replace("http://www.w3.org/2000/svg", "")
        assert "http://" not in cleaned and "https://" not in cleaned, (
            f"External URL found in {svg_file.name}"
        )


def test_mermaid_blocks_and_sources_present_and_coherent():
    """README Mermaid blocks and .mmd sources should be present and coherent."""
    text = _readme_text()
    mermaid_blocks = re.findall(r"```mermaid\n(.*?)\n```", text, flags=re.DOTALL)
    assert len(mermaid_blocks) >= 3

    for block in mermaid_blocks:
        stripped = block.strip()
        assert stripped.startswith("flowchart"), "Mermaid block missing flowchart declaration"
        assert stripped.count("[") == stripped.count("]"), "Unbalanced [] in Mermaid block"

    for mmd in [ROOT / "diagrams" / "product-system.mmd", ROOT / "diagrams" / "learning-graph.mmd"]:
        source = mmd.read_text(encoding="utf-8")
        assert "flowchart" in source
        assert source.count("[") == source.count("]")


def test_navigation_anchors_and_contact_links_are_correct():
    """Top nav anchors and provided contact links should be present and correct."""
    text = _readme_text()
    required_anchors = [
        "#identity",
        "#mission-control",
        "#product-ecosystem",
        "#engineering-system",
        "#flight-plan",
        "#open-protocol",
        "#signal",
    ]
    for anchor in required_anchors:
        assert f'href="{anchor}"' in text

    assert "https://github.com/NatanaelSijabat" in text
    assert "https://www.linkedin.com/in/natanael-sijabat" in text
    assert "mailto:nael.working@gmail.com" in text


def test_forbidden_generic_profile_patterns_absent():
    """README should avoid disallowed generic profile tropes and assets."""
    text = _readme_text()
    for pattern in FORBIDDEN_PATTERNS:
        assert re.search(pattern, text) is None, f"Forbidden pattern found: {pattern}"


def test_markdown_safety_no_omitted_or_generation_markers():
    """README should be clean of omission markers and unsafe HTML constructs."""
    text = _readme_text()
    banned = [
        "[omitted]",
        "<script",
        "lorem ipsum",
        "insert here",
    ]
    lowered = text.lower()
    for token in banned:
        assert token not in lowered
