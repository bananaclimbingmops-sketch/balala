---
name: balala
description: Generate or edit brand-consistent Balala (巴拉拉), the Banana Climbing / 香蕉攀岩 yellow monkey mascot, as a single-character bitmap on a pure white background using bundled official references. Use whenever a user asks for Balala doing an action, showing an emotion, holding or using an object, or appearing as an avatar, sticker, illustration, campaign visual, 2D full-body character, 2D head/avatar, or 3D full-body character. Automatically route unspecified requests among 2D full body, 2D avatar, and 3D full body.
---

# Balala

Generate the requested image, not merely a prompt. Keep Balala recognizable by using the bundled reference images and isolate the result on pure white.

## Workflow

1. Parse the requested action, emotion, props, orientation, output ratio, and intended use.
2. Choose exactly one visual mode by following [references/mode-selection.md](references/mode-selection.md). Honor an explicit mode. Otherwise infer it; default to `2d-full` without asking.
3. Read [references/character-spec.md](references/character-spec.md) and the selected mode section in [references/prompt-templates.md](references/prompt-templates.md).
4. Select references with [references/asset-manifest.md](references/asset-manifest.md). Resolve every relative path from this skill directory.
5. Inspect the selected images before generation. Use the identity set required by the manifest and at most one same-mode action or expression reference, with no more than three inputs total. Never mix 2D and 3D identity references.
6. Rewrite the request as a concrete visual action: body position, limb placement, gaze, expression, and physical interaction with each prop. Preserve user intent while removing any environmental background.
7. Call the available image-generation or image-editing tool with the selected local reference paths and the completed mode prompt. If the tool supports reference-image editing, prefer it over text-only generation.
8. Inspect the generated image. Correct identity drift, wrong mode, malformed anatomy, unreadable action, cropping, non-white background, extra characters, text, or watermarks. Regenerate or edit until it passes.
9. If a local PNG or JPEG is available and Pillow is installed, run `python <skill-directory>/scripts/validate_output.py OUTPUT_PATH`, replacing `<skill-directory>` with this installed skill's absolute path. Treat this as a background/composition check, not a substitute for visual identity review.
10. Return the final image and briefly state the selected mode. Do not expose the internal prompt unless asked.

## Reference Rules

- Treat files under `identity/` as authoritative for character identity and style. For 2D full body, the four-view turnaround is authoritative for geometry. For 3D, the three-view turnaround is authoritative for geometry, including the tail tip and head-top banana stem; front renders are authoritative only for face, material, and outfit finish.
- Treat files under `action/` as pose, emotion, or viewpoint support only.
- Treat `action-only-half-body/` as interaction reference only. Never copy its crop into a `3d-full` result.
- Do not average conflicting traits across modes or identity files. The selected mode's turnaround wins every geometry conflict.
- Keep reference images inside the installed skill; do not require the user to reattach them.
- If local reference images cannot be passed to the available generator, explain that this dependency is missing instead of claiming a faithful result.

## Output Contract

- Produce exactly one Balala unless the user explicitly requests multiple characters.
- Use a uniform `#FFFFFF` background. Do not use transparency, off-white, gradients, scenery, frames, logos, captions, or watermarks.
- Retain only props needed to communicate the action. Remove floors, walls, landscapes, decorative shapes, and unrelated climbing-gym scenery.
- For `2d-full` and `3d-full`, show the complete head ornament, body, hands, feet, and tail with 8–12% breathing room. Allow the tail to be hidden only by physically plausible body occlusion in a straight front view. Never crop a full-body result.
- For `2d-avatar`, show the complete head silhouette, both ears, and head ornament with comfortable margins; omit the torso unless required by a small gesture.
- Keep the output readable at thumbnail size. Prefer one clear action and no more than two simple props.
- Default to a square composition and at least 1024×1024 when the user gives no dimensions.
- Add no written text inside the image unless the user explicitly requests it. If requested text conflicts with the white-background character-asset purpose, provide the clean character asset first.

## Ambiguity and Conflicts

- Do not ask which mode to use when the routing rules yield a reasonable answer.
- If a user asks for a complex environment while also asking for the standard white-background asset, keep the action and essential contact props but omit the environment.
- If an environment is indispensable to the requested deliverable, ask whether to waive the white-background contract before generating.
- If the user requests a new style that would erase Balala's identity, preserve the selected official mode and apply only compatible surface-level treatment.

## Safety and Brand Integrity

- Do not depict Balala endorsing illegal, hateful, sexual, or dangerous conduct.
- For climbing actions, show plausible contact with holds and sensible safety equipment when height or roped climbing is implied.
- Do not redistribute the bundled source references separately from this skill. Confirm that the distributor has permission to ship and create derivatives from the brand assets before public release.
