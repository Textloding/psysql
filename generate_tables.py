import re, json

# Load Chinese table names
with open('mapping.json', encoding='utf-8') as f:
    MAPPING = json.load(f)

# Optional table descriptions
TABLE_DESCRIPTIONS = {
    'course_lesson_tag': '存储课程课时与标签的关联关系。'
}

# Default column descriptions by name
DEFAULT_COL_DESC = {
    'id': '主键ID',
    'created_at': '创建时间',
    'updated_at': '更新时间',
    'deleted_at': '删除时间',
    'email': '邮箱',
    'phone': '电话',
    'password': '密码',
    'remember_token': '记住登录',
    'slug': '标识',
    'name': '名称',
    'title': '标题',
    'description': '描述',
    'content': '内容',
    'summary': '摘要',
    'image': '图片',
    'cover_image': '封面图片',
    'avatar': '头像',
    'status': '状态',
    'sort_order': '排序',
    'sort': '排序',
    'order': '排序',
    'is_active': '是否启用',
    'is_enabled': '是否启用',
    'is_featured': '是否推荐',
    'is_recommended': '是否推荐',
    'is_free': '是否免费',
    'price': '价格',
    'view_count': '浏览次数',
    'views': '浏览次数',
    'likes': '点赞数',
    'published_at': '发布时间',
    'publish_time': '发布时间',
    'start_time': '开始时间',
    'end_time': '结束时间',
    'scheduled_at': '计划时间',
    'ended_at': '结束时间',
}

sql = open('psq.sql', encoding='utf-8').read()
TABLE_PATTERN = re.compile(r"-- 表的结构 `(.*?)`.*?CREATE TABLE `\1` \((.*?)\) ENGINE", re.S)
COLUMN_PATTERN = re.compile(r"^`([^`]*)`\s+([^,]*?)(?:\s+COMMENT '(.*?)')?$")

# word level translation for generating simple descriptions
WORD_MAP = {
    'user': '用户',
    'course': '课程',
    'lesson': '课时',
    'tag': '标签',
    'category': '分类',
    'admin': '管理员',
    'role': '角色',
    'permission': '权限',
    'menu': '菜单',
    'news': '新闻',
    'video': '视频',
    'quiz': '答题',
    'question': '题目',
    'option': '选项',
    'answer': '答案',
    'attempt': '记录',
    'review': '审核',
    'phone': '电话',
    'email': '邮箱',
    'title': '标题',
    'summary': '摘要',
    'content': '内容',
    'description': '描述',
    'image': '图片',
    'cover': '封面',
    'status': '状态',
    'sort': '排序',
    'order': '排序',
    'price': '价格',
    'ip': 'IP',
    'address': '地址',
    'token': '令牌',
    'score': '分数',
    'name': '名称',
    'message': '消息',
    'system': '系统',
    'version': '版本',
    'options': '配置',
    'provider': '提供商',
    'model': '模型',
    'max_tokens': '最大token数',
    'temperature': '温度',
    'schedule': '排班',
    'appointment': '预约',
    'password': '密码',
    'department': '部门',
    'phone_number': '电话号码',
    'comments': '意见',
    'rating': '评分',
}

def translate_parts(parts):
    return ''.join(WORD_MAP.get(p, p) for p in parts)

def guess_description(col):
    if col in DEFAULT_COL_DESC:
        return DEFAULT_COL_DESC[col]
    if col.endswith('_id') and col != 'id':
        base = col[:-3]
        if base in MAPPING:
            return MAPPING[base].rstrip('表') + 'ID'
        return translate_parts(base.split('_')) + 'ID'
    if col.endswith('_at'):
        base = col[:-3]
        special = {
            'created': '创建时间',
            'updated': '更新时间',
            'deleted': '删除时间',
            'replied': '回复时间',
            'published': '发布时间',
            'completed': '完成时间',
        }
        if base in special:
            return special[base]
        return translate_parts(base.split('_')) + '时间'
    if col.endswith('_time'):
        base = col[:-5]
        spec = {
            'start': '开始时间',
            'end': '结束时间',
        }
        if base in spec:
            return spec[base]
        return translate_parts(base.split('_')) + '时间'
    if col.startswith('is_'):
        return '是否' + translate_parts(col[3:].split('_'))
    if col.endswith('_count'):
        return translate_parts(col[:-6].split('_')) + '数量'
    if col.endswith('_status'):
        return translate_parts(col[:-7].split('_')) + '状态'
    if col.endswith('_url'):
        return translate_parts(col[:-4].split('_')) + '链接'
    if col.endswith('_image'):
        return translate_parts(col[:-6].split('_')) + '图片'
    if col.endswith('_name'):
        return translate_parts(col[:-5].split('_')) + '名称'
    if col.endswith('_code'):
        return translate_parts(col[:-5].split('_')) + '编号'
    if col.endswith('_token'):
        return translate_parts(col[:-6].split('_')) + '令牌'
    if col.endswith('_notes'):
        return translate_parts(col[:-6].split('_')) + '备注'
    return translate_parts(col.split('_'))

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
        if not comment:
            comment = guess_description(col_name)
        out_lines.append(f"| `{col_name}` | {col_type} | {comment} |")
    out_lines.append("")

open('README.md', 'w', encoding='utf-8').write('\n'.join(out_lines) + '\n')
