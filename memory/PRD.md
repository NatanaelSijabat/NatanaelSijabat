# Product Requirements Document — ZippoTech GitHub Profile

## Original Problem Statement
Create a uniquely designed GitHub Profile README for Natanael Sijabat that feels like a premium, interactive software dashboard. The profile must communicate senior full-stack, AI, cloud, and product architecture expertise while avoiding conventional GitHub-profile patterns such as typing SVGs, contribution snakes, badge walls, stats cards, trophies, visitor counters, streak widgets, rainbow headers, and generic biography/stack sections. Deliver a complete `README.md`, local animated SVG assets, and Mermaid source diagrams that work on GitHub without external dependencies.

## User-Provided Identity
- Name: Natanael Sijabat
- Brand: ZippoTech
- GitHub: https://github.com/NatanaelSijabat
- LinkedIn: https://www.linkedin.com/in/natanael-sijabat
- Email: nael.working@gmail.com
- Product work: private; show meaningful product domains without invented repository links
- Delivery location: directly in `/app`

## User Personas
1. **Engineering leader or founder** evaluating Natanael for high-leverage product, AI, or platform work.
2. **Senior engineer** assessing architecture judgment, technical range, and open-source values.
3. **Potential collaborator** looking for current interests and a direct contact path.
4. **Repository visitor** encountering Natanael through an issue, contribution, or shared project.

## Architecture Decisions
- GitHub-native Markdown and safe embedded HTML only; no runtime application or backend.
- All visual assets are local, self-contained SVG files with no fonts, scripts, images, or remote dependencies.
- SVG animation uses declarative CSS/SMIL-compatible primitives and remains legible when motion is unavailable.
- Information architecture behaves like an operating surface: Identity → Mission → Products → Engineering System → Roadmap → Open Protocol → Timeline → Signal.
- Native Markdown interactions use anchors, `<details>`, tables, blockquotes, admonitions, code blocks, and Mermaid.
- Private product work is represented through truthful domain tracks rather than fake project names or placeholder URLs.
- Separate `.mmd` files preserve reusable diagram sources while the README contains GitHub-renderable Mermaid blocks.

## Core Requirements (Static)
- Dark-first, minimal, futuristic, sophisticated visual language with restrained blue and purple accents.
- Animated hero and visual dashboard assets.
- Internal navigation and direct GitHub, LinkedIn, and email links.
- Current mission, experiments, roadmap, product ecosystem, principles, architecture, tech radar, learning graph, open-source philosophy, repository showcase, timeline, and contact surface.
- No common GitHub-profile generators, widgets, external asset services, or placeholder content.
- Maintainable file structure under `/assets` and `/diagrams`.
- Production-ready GitHub rendering and accessible SVG title/description metadata.

## What's Been Implemented

### 2026-07-17 — Initial Production Build
- Replaced the starter README with a 333-line GitHub-native dashboard experience.
- Added 11 original local SVG assets: hero, identity console, mission control, three product tracks, engineering principles, tech radar, roadmap, timeline, and footer.
- Added two reusable Mermaid sources for the product system and active learning graph.
- Added anchor navigation, collapsible build log and principles, product dashboard, decision workflow, architecture maps, roadmap, open-source release filters, repository index, timeline, and real contact links.
- Added a static regression suite covering structure, local references, SVG integrity, Mermaid coherence, navigation, contact links, forbidden patterns, and placeholder safety.
- Validation result: 8/8 checks passed with no blocking defects.

## Prioritized Backlog

### P0 — Required Before Use
- None.

### P1 — High-Value Future Updates
- Replace private product-domain cards with real public projects when Natanael is ready to publish them.
- Add verified career milestones and dates if Natanael wants a historically specific timeline.
- Review the rendered profile after publishing to the username-matching GitHub repository and tune any GitHub theme-specific contrast differences.

### P2 — Optional Enhancements
- Add Indonesian-language contact or identity copy for regional audiences.
- Add local SVG case-study panels for future flagship repositories.
- Add a lightweight changelog convention for major profile revisions.

## Next Tasks
1. Use these files in the `NatanaelSijabat/NatanaelSijabat` profile repository.
2. Add real public project URLs to the Product Ecosystem and Repository Showcase when available.
3. Keep `/app/tests/test_readme_static_artifacts.py` as the regression guard for future edits.