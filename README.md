# Balala Skill

为香蕉攀岩吉祥物 Balala 生成品牌一致的白底图与真透明 PNG 素材。

安装后，只需描述 Balala 正在做什么。Skill 会自动选择：

- 2D 全身版：动作、运动、贴纸和教学插画
- 2D 头像版：表情、头像、反应和小图标
- 3D 全身版：品牌主视觉、公仔感和宣传渲染

所有版本都内置官方角色参考图。2D 四视图与 3D 三视图拥有最高几何优先级；3D 的尾巴末端和头顶香蕉柄以最新三视图为准。

默认一次交付两张姿势、构图和道具完全一致的 PNG：

- `balala-white.png`：纯白底预览版，方便审核、分享和直接用于白色版面
- `balala-transparent.png`：带真实 Alpha 通道的免抠图素材版，方便海报、网页、周边和视频合成

如果用户明确说“只要透明底”或“只要白底”，Skill 只输出指定版本。

## 效果预览

| 2D 全身 | 2D 头像 | 3D 全身 |
|---|---|---|
| ![2D Balala 抱石](examples/2d-full-bouldering.png) | ![2D Balala 惊讶头像](examples/2d-avatar-surprised.png) | ![3D Balala 举奖杯](examples/3d-full-trophy.png) |

## 从 Manus 安装

在 Manus 的 Skills 页面选择“从 GitHub 导入”，粘贴公开仓库地址：

```text
https://github.com/bananaclimbingmops-sketch/balala
```

本仓库的 `SKILL.md` 位于根目录，符合 Manus 的 GitHub 导入要求。

## 从 Codex 安装

在 Codex 中发送：

```text
Use $skill-installer to install bananaclimbingmops-sketch/balala from repository path "." with the skill name "balala".
```

安装完成后，Skill 名称为 `balala`。

## Agent Skills 通用安装

本仓库遵循开放的 Agent Skills 目录约定。支持 Agent Skills 的客户端可以将整个仓库克隆到个人 Skill 目录：

```bash
mkdir -p ~/.agents/skills
git clone --depth 1 https://github.com/bananaclimbingmops-sketch/balala.git ~/.agents/skills/balala
```

常见位置：

- 跨客户端、GitHub Copilot：`~/.agents/skills/balala`
- Claude Code：`~/.claude/skills/balala`
- Codex：`~/.codex/skills/balala`

也可以下载仓库根目录的 [`balala.skill.zip`](balala.skill.zip)：

- Manus：直接上传 ZIP
- 其他客户端：把 ZIP 内容解压到名为 `balala` 的 Skill 文件夹

ZIP 顶层结构为：

```text
SKILL.md
agents/
assets/
references/
scripts/
```

客户端没有立即显示新 Skill 时，请重新启动或刷新 Skill 列表。

## 使用

ChatGPT 桌面端启用 Skill 后，它会出现在 `/` 命令列表中：

```text
/balala
```

在 Codex CLI、IDE 扩展或需要跨客户端兼容时，使用官方的显式 Skill 调用写法：

```text
$balala 生成一个正在攀岩的 Balala
```

也可以自然描述，由 Agent 根据 Skill 描述自动调用：

```text
生成一个正在使用电脑的 Balala。
```

默认返回白底版和透明底版。也可以指定：

```text
$balala 生成一个正在使用电脑的 3D Balala，只要透明底 PNG。
```

## 依赖

使用端需要具备支持本地参考图片的图片生成或图片编辑能力。Skill 本身不包含图片模型或 API 凭据。

## 内容

- `SKILL.md`：执行流程、模式路由与双输出规则
- `assets/`：23 张角色、动作、表情与转面参考图
- `references/`：角色规范、模式路由与提示词模板
- `scripts/make_transparent.py`：仅移除边缘连通的近白背景，保护牙齿、短裤等内部浅色细节
- `scripts/validate_output.py`：白底/透明底、Alpha、尺寸和安全边距检查
- `agents/openai.yaml`：支持该元数据的 OpenAI 客户端界面信息

## 官方调用说明

- [Agent Skills 开放规范](https://agentskills.io/specification)
- [Manus GitHub Skill 导入说明](https://help.manus.im/en/articles/14753565-how-to-share-and-use-skills-in-manus)
- [GitHub Copilot Agent Skills 说明](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

不同客户端的调用界面可能不同：支持斜杠命令的客户端通常使用 `/balala`，Codex 也支持 `$balala` 显式调用。
