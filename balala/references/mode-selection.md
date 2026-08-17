# Mode Selection

Choose one mode before selecting references. Explicit user wording always wins when it names a supported mode.

| Signals in the request | Select | Typical uses |
|---|---|---|
| `2D全身`, `2D full body`, sticker, action illustration, sport, teaching pose, holding a prop, festival pose | `2d-full` | Dynamic action assets, stickers, educational illustrations, merchandise graphics |
| `头像`, `头图`, `表情`, `表情包`, avatar, icon, reaction, badge, emoji | `2d-avatar` | Profile images, reactions, small icons, expression graphics |
| `3D`, `三维`, `公仔`, `render`, hero visual, campaign key visual, product visual, spatial or premium promotional image | `3d-full` | Campaign hero images, polished promotional renders, physical/product presentations |

## Tie-breakers

1. Honor an explicit supported mode.
2. Prefer `2d-avatar` when expression is the deliverable and body action is irrelevant.
3. Prefer `3d-full` when the user asks for 3D, a figurine/render look, or a polished campaign main visual.
4. Prefer `2d-full` for a verb-led action with readable body mechanics.
5. Default to `2d-full` when still ambiguous. Do not ask the user solely to choose a mode.

## Examples

- “一个正在抱石的 Balala” → `2d-full`
- “Balala 开心到流泪的头像” → `2d-avatar`
- “做一个拿奖杯的 3D Balala 主视觉” → `3d-full`
- “Balala 正在敲电脑” → `2d-full` unless the user also says 3D/render/campaign visual
- “一个生气的 Balala” → `2d-avatar` because the request is emotion-only
- “一个生气地跺脚的 Balala” → `2d-full` because the body action carries the meaning

## Unsupported or Conflicting Requests

- Map “3D 头像” to `3d-full` only if the user accepts a full-body result; otherwise explain that the official modes do not include a dedicated 3D-avatar profile.
- Map “2D 半身” to `2d-full` and preserve the complete body unless the user explicitly prioritizes the crop over the standard asset contract.
- Keep white background as the default even if an action implies a location. Include only essential contact props such as a climbing hold, rope, laptop, phone, cake, or trophy.

