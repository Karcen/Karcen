import requests

username = "Karcen"

# GitHub Stats API (官方 github-readme-stats 的免费实例也可以用)
stats_url = f"https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=radical"
languages_url = f"https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&theme=radical"

readme_file = "README.md"

with open(readme_file, "r") as f:
    content = f.read()

# 替换占位
start_marker = "<!-- metrics-start -->"
end_marker = "<!-- metrics-end -->"

new_content = f"{start_marker}\n![GitHub Stats]({stats_url})\n![Top Languages]({languages_url})\n{end_marker}"

if start_marker in content and end_marker in content:
    content = content.split(start_marker)[0] + new_content + content.split(end_marker)[1]

with open(readme_file, "w") as f:
    f.write(content)

print("Metrics updated in README.md")
