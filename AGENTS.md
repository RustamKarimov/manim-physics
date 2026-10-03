# Working rules for this project

The user supplies every lesson idea, explanation, visual action, and sequence.
Translate their instructions into code. Do not invent teaching content, titles,
transitions, narration, or screen resets.

## Editing
- Read the current files before editing. Saved code is authoritative.
- Preserve the user's changes, whether committed or uncommitted. Modify an area
  they adjusted only when their current instruction explicitly covers it.
- Additions do not authorize retuning existing objects. If a dependency requires
  changing a user-adjusted area outside the request, explain it and ask first.
- Apply narrow patches. Do not rewrite files, reformat unrelated code, rename
  existing objects, or refactor incidentally.
- Review the final diff for unrelated changes. Optional USER-TUNED markers help
  navigation but are not required for protection.

## Code and communication
- Write detailed comments explaining adjustment points, units, dependencies,
  coordinate conversion, timing, and updater lifetimes.
- Beside animation code, suggest a few relevant alternative Manim animations
  and explain their effects and required imports. Do not apply alternatives
  without a request. The user supplies small actions without needing unit IDs.
- Keep physical time and coordinates separate from playback and screen units.
- Use ordinary functions/classes and explicit imports. Avoid premature abstractions.
- Each unit is an invisible part of one continuous Scene. No automatic cleanup,
  headings, pauses, or fades at unit boundaries.
- Shared state carries named objects between units. Use tracker-based analytic
  motion where possible; accumulated dt-based motion may not skip correctly.
- Report what changed, adjustment points, checks, and remaining visual review.
- Keep progress notes short and based on the user's instructions.

## Execution
- Never render videos, still frames, or Manim dry-run scenes. The user renders.
- Non-rendering source, configuration, path, and mathematical checks are allowed.
- Do not install dependencies or alter the user's machine unless requested.
- Do not create a remote repository, push, or publish without authorization.
- Keep .venv, .idea, caches, and build output out of version control.

Initial reference: Cambridge 9702, examination years 2025–2027. This identifies
the reference only; it does not authorize choosing lesson content.
