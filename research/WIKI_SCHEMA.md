# Research Wiki Schema & Operating Manual

This document defines the structure, conventions, and workflows for the **Research Wiki**. Antigravity (the LLM) is responsible for maintaining this wiki as new findings and sources are added.

## 1. Architecture

- **Raw Sources (`research/raw/`)**: Immutable source documents (papers, articles, transcripts).
- **The Wiki (`research/wiki/`)**: Interlinked markdown files representing the compiled knowledge base.
- **The Schema (`research/WIKI_SCHEMA.md`)**: This document; the governing rules for the wiki.

## 2. File Conventions

- **Filename**: kebab-case (e.g., `character-consistency-metrics.md`).
- **Headings**: Use hierarchical markdown headings (H1 for title, H2, H3 for sub-sections).
- **Cross-links**: Use standard markdown links `[Title](filename.md)` for internal navigation.
- **Frontmatter**: Every wiki page must include YAML frontmatter:
  ```yaml
  ---
  type: entity | concept | source | synthesis
  tags: []
  updated: YYYY-MM-DD
  sources: [] # List of filenames from research/raw/
  ---
  ```

## 3. Operations

### Ingest Workflow
When a new source is added to `research/raw/`:
1.  **Read**: Analyze the source contents.
2.  **Summarize**: Create a source-summary page in `research/wiki/`.
3.  **Integrate**: Update existing entity and concept pages with new information.
4.  **Log**: Add an entry to `research/wiki/log.md`.
5.  **Index**: Update `research/wiki/index.md`.

### Query Workflow
When asked a synthesis question:
1.  **Search**: Consult `index.md` to find relevant pages.
2.  **Read**: Review the interlinked wiki pages.
3.  **Synthesize**: Provide an answer with citations to the wiki pages.
4.  **Preserve**: If the answer is valuable, file it as a new `synthesis` page.

### Lint Workflow
Periodically check for:
-   **Contradictions**: Flag where sources or pages disagree.
-   **Orphans**: Find pages with no inbound links.
-   **Gaps**: Identify concepts mentioned but not defined.

## 4. Special Files

- **[index.md](wiki/index.md)**: A categorized catalog of all wiki pages. Updated on every ingest.
- **[log.md](wiki/log.md)**: A chronological, append-only record of wiki operations.
  Format: `## [YYYY-MM-DD] action | Title`
