---
name: balala
description: Generate or edit brand-consistent Balala (巴拉拉), the Banana Climbing / 香蕉攀岩 yellow monkey mascot, as a single-character bitmap using bundled official references. Use whenever a user asks for Balala doing an action, showing an emotion, holding or using an object, or appearing as an avatar, sticker, illustration, campaign visual, transparent PNG cutout, white-background image, 2D full-body character, 2D head/avatar, or 3D full-body character. Automatically route unspecified requests among 2D full body, 2D avatar, and 3D full body, and return both white-background and transparent PNG assets by default.
---

# Balala

Generate the requested image, not merely a prompt. Keep Balala recognizable by using the bundled reference images. By default, deliver a matched pair: an opaque white-background PNG for preview and a true transparent-background PNG for production use.

## Workflow

1. Parse the requested action, emotion, props, orientation, output ratio, intended use, and output-background preference.
2. Choose exactly one visual mode by following [references/mode-selection.md](references/mode-selection.md). Honor an explicit mode. Otherwise infer it; default to `2d-full` without asking.
3. Read [references/character-spec.md](references/character-spec.md) and the selected mode section in [references/prompt-templates.md](references/prompt-templates.md).
4. Select references with [references/asset-manifest.md](references/asset-manifest.md). Resolve every relative path from this skill directory.
5. Inspect the selected images before generation. Use the identity set required by the manifest and at most one same-mode action or expression reference, with no more than three inputs total. Never mix 2D and 3D identity references.
6. Choose the delivery set. Return both `balala-white.png` and `balala-transparent.png` when the user does not specify a background. Return only the transparent PNG for requests such as “透明底”, “免抠图”, “素材 PNG”, or “transparent”; return only the white PNG for requests explicitly limited to “白底” or “white background”.
7. Rewrite the request as a concrete visual action: body position, limb placement, gaze, expression, and physical interaction with each prop. Preserve user intent while removing environmental scenery.
8. Call the available image-generation or image-editing tool with the selected local reference paths and the completed mode prompt. Prefer a native transparent-background generation for the production asset when the tool reliably supports alpha. Otherwise create a clean white master, then remove only the border-connected white background with `scripts/make_transparent.py`. Never globally delete white pixels.
9. Derive the matched companion from the same approved character rendering so pose, proportions, crop, and props are identical. Composite the transparent asset over `#FFFFFF` to create the white version when native transparency is available. For 3D transparent output, remove floor and cast shadows by default; preserve a shadow only when the user explicitly requests it.
10. Inspect every delivered image. Correct identity drift, wrong mode, malformed anatomy, unreadable action, cropping, background contamination, white halos, extra characters, text, or watermarks. Regenerate or edit until it passes.
11. If local PNGs and Pillow are available, validate each delivered file:
    - white: `python <skill-directory>/scripts/validate_output.py balala-white.png --mode white`
    - transparent: `python <skill-directory>/scripts/validate_output.py balala-transparent.png --mode transparent`
    Replace `<skill-directory>` with this installed skill's absolute path. Treat these as background/composition checks, not substitutes for visual identity review.
12. Return the final image file or matched pair and briefly state the selected visual mode and background variant. Do not expose the internal prompt unless asked.

## Reference Rules

- Treat files under `identity/` as authoritative for character identity and style. For 2D full body, the four-view turnaround is authoritative for geometry. For 3D, the three-view turnaround is authoritative for geometry, including the tail tip and head-top banana stem; front renders are authoritative only for face, material, and outfit finish.
- Treat files under `action/` as pose, emotion, or viewpoint support only.
- Treat `action-only-half-body/` as interaction reference only. Never copy its crop into a `3d-full` result.
- Do not average conflicting traits across modes or identity files. The selected mode's turnaround wins every geometry conflict.
- Keep reference images inside the installed skill; do not require the user to reattach them.
- If local reference images cannot be passed to the available generator, explain that this dependency is missing instead of claiming a faithful result.

## Output Contract

- Produce exactly one Balala unless the user explicitly requests multiple characters.
- Default delivery is two visually identical PNG files: `balala-white.png` with a uniform opaque `#FFFFFF` background, and `balala-transparent.png` with real RGBA transparency.
- Honor an explicit request for only one background variant. Never simulate transparency with a checkerboard, off-white fill, flattened preview, clipping path, or colored matte.
- The transparent PNG must have transparent canvas pixels outside the subject and clean antialiased edges. Preserve Balala's ivory teeth, cream shorts, peach face, highlights, and any intentional white prop details; background removal must be border-connected, not a global white-color deletion.
- Do not include gradients, scenery, frames, logos, captions, watermarks, or an accidental floor/cast shadow in the transparent production asset.
- Retain only props needed to communicate the action. Remove floors, walls, landscapes, decorative shapes, and unrelated climbing-gym scenery.
- For `2d-full` and `3d-full`, show the complete head ornament, body, hands, feet, and tail with 8–12% breathing room. Allow the tail to be hidden only by physically plausible body occlusion in a straight front view. Never crop a full-body result.
- For `2d-avatar`, show the complete head silhouette, both ears, and head ornament with comfortable margins; omit the torso unless required by a small gesture.
- Keep the output readable at thumbnail size. Prefer one clear action and no more than two simple props.
- Default to a square composition and at least 1024×1024 when the user gives no dimensions.
- Add no written text inside the image unless the user explicitly requests it. If requested text conflicts with the reusable character-asset purpose, provide the clean character asset first.

## Ambiguity and Conflicts

- Do not ask which mode to use when the routing rules yield a reasonable answer.
- If a user asks for a complex environment while also asking for the standard reusable asset, keep the action and essential contact props but omit the environment.
- If an environment is indispensable to the requested deliverable, ask whether to waive the isolated-character contract before generating.
- If the user requests a new style that would erase Balala's identity, preserve the selected official mode and apply only compatible surface-level treatment.

## Safety and Brand Integrity

- Do not depict Balala endorsing illegal, hateful, sexual, or dangerous conduct.
- For climbing actions, show plausible contact with holds and sensible safety equipment when height or roped climbing is implied.
- Do not redistribute the bundled source references separately from this skill. Confirm that the distributor has permission to ship and create derivatives from the brand assets before public release.
