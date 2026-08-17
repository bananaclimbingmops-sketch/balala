# Prompt Templates

Replace bracketed fields with concrete visual details. Include every Common Output block item in the generation request.

## Common Output Block

> Create one brand-faithful Balala mascot based on the attached official references. Balala is performing [ACTION] with [BODY POSITION AND LIMB PLACEMENT], looking [GAZE DIRECTION], with a [EXPRESSION] expression and interacting clearly with [ESSENTIAL PROPS]. Preserve all defining Balala identity features from the selected identity reference. Center the subject on a uniform pure white #FFFFFF background. Use a square composition unless otherwise requested. Add no scenery, floor, decorative graphics, text, logo, border, watermark, extra character, or unrelated object. Keep clean margins and make the action readable at thumbnail size.

## 2D Full Body Addendum

> Use the official 2D full-body style and follow the four-view turnaround for authoritative proportions and viewpoint: flat vector-like color, thick rounded brown outlines, banana-yellow body, peach face/inner ears/belly, orange-red nose, graphic facial features, stylized limbs and toes, the turnaround's exact view-dependent brown head-top banana stem, and the official yellow tail ending in three stacked yellow gripping lobes around a short brown cap. Show the entire head stem, body, both hands, both feet, and tail with 8–12% white breathing room. Do not use 3D rendering, realistic fur, the 3D shirt-and-shorts outfit, cropped anatomy, or cast shadows.

## 2D Avatar Addendum

> Use the dedicated official 2D head/avatar style, not a crop of the full-body version. Show the complete broad head silhouette, both circular ears, peach face patch, orange-red nose, brown graphic features, and brown banana-shaped head ornament. Express [EMOTION] through eyebrows, eyelids, mouth, and cheeks while keeping the official geometry. Use flat color and rounded brown outlines. Show no torso by default. Remove the beige card background and all faint source lettering.

## 3D Full Body Addendum

> Use the official polished 3D full-body mascot style: large rounded head and ears, warm peach face/inner ears, brown oval eyes, orange-red nose, broad segmented grin when compatible with the emotion, subtle tactile molded/fuzzy surface, yellow short-sleeve shirt, warm cream shorts, sturdy yellow limbs, three rounded toes, and the official yellow tail with three curled gripping lobes around its short rounded brown cap. Follow the latest three-view turnaround for all front/side/back geometry and reproduce its compact brown head-top banana stem exactly, including view-dependent curvature, thickness, angle, and attachment; ignore conflicting older stem shapes. Use soft neutral studio lighting with at most a faint contact shadow. Show the complete figure from head stem to both feet and the full tail whenever physically visible, with 8–12% white breathing room. Reconstruct the full lower body even if an action reference is cropped. Do not use flat outlines, photoreal fur, an ordinary tapered monkey tail, cinematic scenery, or glossy plastic.

## Negative Constraints

Append concise negative constraints relevant to the request:

> No altered species, missing or older conflicting head-stem shape, missing or generic monkey tail, changed ear shape, wrong palette, extra limbs or digits, detached props, fused hands, cropped feet, duplicate character, background scene, off-white backdrop, transparent background, text, logo, watermark, or unrelated costume.

## Action Translation Examples

- “正在攀岩” → one hand reaching to a hold, the other gripping a second hold, feet pressing two lower holds, hips close to the wall plane; on white, retain only four isolated holds and necessary harness/rope.
- “使用电脑” → open laptop supported on a small plain white-compatible desk or held securely, both hands placed plausibly on the keyboard, gaze directed at the screen; omit room scenery.
- “拿奖杯庆祝” → one hand lifting a single trophy, the other raised in celebration, wide stable stance, joyful open expression; omit confetti unless explicitly requested.
- “自拍” → one arm extending a phone at a three-quarter angle, gaze directed at the phone camera, free hand making a simple celebratory gesture; retain full body for `3d-full`.
