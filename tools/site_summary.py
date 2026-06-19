import json
import sys
from datetime import date

SITE_DATA = {
    "url": "https://web-lovegame.com",
    "title": "爱游戏综合门户",
    "keywords": ["爱游戏", "在线娱乐", "游戏资讯", "玩家社区"],
    "tags": ["游戏", "资讯", "社区", "娱乐"],
    "description": "一个汇集热门游戏资讯、玩家评测和社区互动的综合平台，为游戏爱好者提供最新动态与深度内容。",
    "launch_date": "2022-06-15",
    "language": "zh-CN",
    "category": "游戏门户"
}

def build_summary(data: dict) -> str:
    lines = []
    lines.append(f"站点名称：{data['title']}")
    lines.append(f"站点地址：{data['url']}")
    lines.append(f"站点描述：{data['description']}")
    lines.append(f"核心关键词：{'、'.join(data['keywords'])}")
    lines.append(f"标签：{'、'.join(data['tags'])}")
    lines.append(f"上线日期：{data['launch_date']}")
    lines.append(f"语言：{data['language']}")
    lines.append(f"所属类别：{data['category']}")
    lines.append(f"报告生成日期：{date.today().isoformat()}")
    return '\n'.join(lines)

def format_as_json(data: dict) -> str:
    output = {
        "site_url": data["url"],
        "site_name": data["title"],
        "keywords": data["keywords"],
        "tags": data["tags"],
        "description": data["description"],
        "summary_generated": date.today().isoformat()
    }
    return json.dumps(output, ensure_ascii=False, indent=2)

def format_as_markdown(data: dict) -> str:
    lines = []
    lines.append(f"# {data['title']}")
    lines.append("")
    lines.append(f"- **URL**：{data['url']}")
    lines.append(f"- **描述**：{data['description']}")
    lines.append(f"- **关键词**：{', '.join(data['keywords'])}")
    lines.append(f"- **标签**：{', '.join(data['tags'])}")
    lines.append(f"- **上线时间**：{data['launch_date']}")
    lines.append(f"- **语言**：{data['language']}")
    lines.append(f"- **类别**：{data['category']}")
    lines.append("")
    lines.append(f"*此摘要由工具于 {date.today().isoformat()} 自动生成*")
    return '\n'.join(lines)

def main():
    if len(sys.argv) > 1:
        fmt = sys.argv[1].lower()
    else:
        fmt = "text"

    data = SITE_DATA.copy()

    if fmt == "json":
        output = format_as_json(data)
    elif fmt == "markdown":
        output = format_as_markdown(data)
    elif fmt == "text":
        output = build_summary(data)
    else:
        print(f"未知格式: {fmt}，可用选项: text, json, markdown", file=sys.stderr)
        sys.exit(1)

    print(output)

if __name__ == "__main__":
    main()