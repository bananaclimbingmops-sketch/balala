# Reference Asset Manifest

Resolve these paths relative to the installed `balala` directory.

## 2D Full Body

- Primary geometry and four-view identity: `assets/2d-full/identity/turnaround-front-three-quarter-side-back.png`
- Clean front facial/detail supplement: `assets/2d-full/identity/front-standing.png`
- Front gesture: `assets/2d-full/action/waving.png`
- Side/action body mechanics: `assets/2d-full/action/side-pose.png`
- Walking/angry expression: `assets/2d-full/action/walking-angry.png`
- Back view: `assets/2d-full/action/back-view.png`
- Dynamic climbing-hold interaction: `assets/2d-full/action/dynamic-holds.png`
- Balancing motion: `assets/2d-full/action/balancing.png`
- Seated party pose: `assets/2d-full/action/party-seated.png`
- Jumping/juggling party pose: `assets/2d-full/action/party-juggling.png`

Always include the four-view turnaround. Add the closest action reference. Add the clean front supplement only when facial/detail fidelity needs it, for a maximum of three inputs. The turnaround wins every conflict in body proportion, viewpoint, ear placement, head-top banana stem, back shape, and tail construction.

## 2D Avatar

- Identity/default grin: `assets/2d-avatar/identity/grin.png`
- Surprised: `assets/2d-avatar/expressions/surprised.png`
- Playful/tongue out: `assets/2d-avatar/expressions/playful.png`
- Angry: `assets/2d-avatar/expressions/angry.png`
- Kiss/puckered: `assets/2d-avatar/expressions/kiss.png`
- Unimpressed/flat: `assets/2d-avatar/expressions/unimpressed.png`

Always include the identity image. Add the nearest expression reference if the user requests an emotion.

## 3D Full Body

- Primary geometry and three-view identity: `assets/3d-full/identity/turnaround-front-side-back.png`, authoritative for the body, ears, back, tail tip, and head-top banana stem
- Facial identity with alpha: `assets/3d-full/identity/front-presenting-transparent.png`
- White studio material/outfit identity: `assets/3d-full/identity/front-presenting-white.png`
- Climbing action and gear: `assets/3d-full/action/climbing-scene.png`
- Sad standing expression: `assets/3d-full/action/sad-standing.png`
- Laptop interaction only: `assets/3d-full/action-only-half-body/laptop.png`
- Selfie interaction only: `assets/3d-full/action-only-half-body/selfie.png`

Always include the turnaround. Add one front identity image for face, material, and outfit fidelity. Add the closest action reference only when it materially clarifies interaction, for a maximum of three images. The turnaround wins for body, ear, back, tail, tail-tip, and head-top banana-stem geometry if references conflict. Half-body files teach only hand/prop interaction; never use them without the turnaround and a full-body front identity.

## Exclusions

- Do not pass references from more than one mode to the generator.
- Do not treat beige source backgrounds, turnaround guide lines, view labels, cropped framing, motion marks, faint letters, or black transparency previews as brand elements.
- Do not select more references merely because they are available; excess references increase style drift.
