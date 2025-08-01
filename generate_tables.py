import re, json

# Load Chinese table names
with open('mapping.json', encoding='utf-8') as f:
    MAPPING = json.load(f)

# Optional table descriptions
TABLE_DESCRIPTIONS = {
    'course_lesson_tag': '存储课程课时与标签的关联关系。'
}

sql = open('psq.sql', encoding='utf-8').read()
TABLE_PATTERN = re.compile(r"-- 表的结构 `(.*?)`.*?CREATE TABLE `\1` \((.*?)\) ENGINE", re.S)
COLUMN_PATTERN = re.compile(r"^`([^`]*)`\s+([^,]*?)(?:\s+COMMENT '(.*?)')?$")

out_lines = ["# psysql", "", "# 数据表汇总", ""]
for tbl in TABLE_PATTERN.finditer(sql):
    name = tbl.group(1)
    cn_name = MAPPING.get(name, name)
    out_lines.append(f"## {cn_name} (`{name}`)")
    desc = TABLE_DESCRIPTIONS.get(name)
    if desc:
        out_lines.append(desc)
    out_lines.append("")
    out_lines.append("| 字段名 | 类型 | 描述 |")
    out_lines.append("| --- | --- | --- |")
    body = tbl.group(2)
    for line in body.strip().splitlines():
        line = line.strip().rstrip(',')
        m = COLUMN_PATTERN.match(line)
        if not m:
            continue
        col_name, col_type, comment = m.groups()
        out_lines.append(f"| `{col_name}` | {col_type} | {comment or ''} |")
    out_lines.append("")

open('README.md', 'w', encoding='utf-8').write('\n'.join(out_lines) + '\n')
