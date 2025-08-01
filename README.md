# psysql

# 数据表汇总

## 管理扩展表 (`admin_extensions`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | int(10) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL | 名称 |
| `version` | varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' | 版本 |
| `is_enabled` | tinyint(4) NOT NULL DEFAULT '0' | 是否启用 |
| `options` | text COLLATE utf8mb4_unicode_ci | 配置 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 管理扩展历史表 (`admin_extension_histories`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL | 名称 |
| `type` | tinyint(4) NOT NULL DEFAULT '1' | type |
| `version` | varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0' | 版本 |
| `detail` | text COLLATE utf8mb4_unicode_ci | detail |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 管理菜单表 (`admin_menu`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `parent_id` | bigint(20) NOT NULL DEFAULT '0' | parentID |
| `order` | int(11) NOT NULL DEFAULT '0' | 排序 |
| `title` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 标题 |
| `icon` | varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL | icon |
| `uri` | varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL | uri |
| `extension` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' | extension |
| `show` | tinyint(4) NOT NULL DEFAULT '1' | show |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 管理权限表 (`admin_permissions`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 名称 |
| `slug` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 标识 |
| `http_method` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | httpmethod |
| `http_path` | text COLLATE utf8mb4_unicode_ci | httppath |
| `order` | int(11) NOT NULL DEFAULT '0' | 排序 |
| `parent_id` | bigint(20) NOT NULL DEFAULT '0' | parentID |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 权限菜单关联表 (`admin_permission_menu`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `permission_id` | bigint(20) NOT NULL | 权限ID |
| `menu_id` | bigint(20) NOT NULL | 菜单ID |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 管理角色表 (`admin_roles`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 名称 |
| `slug` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 标识 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 角色菜单关联表 (`admin_role_menu`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `role_id` | bigint(20) NOT NULL | 角色ID |
| `menu_id` | bigint(20) NOT NULL | 菜单ID |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 角色权限关联表 (`admin_role_permissions`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `role_id` | bigint(20) NOT NULL | 角色ID |
| `permission_id` | bigint(20) NOT NULL | 权限ID |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 角色用户关联表 (`admin_role_users`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `role_id` | bigint(20) NOT NULL | 角色ID |
| `user_id` | bigint(20) NOT NULL | 用户ID |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 管理设置表 (`admin_settings`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `slug` | varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL | 标识 |
| `value` | longtext COLLATE utf8mb4_unicode_ci NOT NULL | value |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 管理员用户表 (`admin_users`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `username` | varchar(120) COLLATE utf8mb4_unicode_ci NOT NULL | username |
| `password` | varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL | 密码 |
| `name` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 名称 |
| `avatar` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 头像 |
| `remember_token` | varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 记住登录 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## AI 咨询记录表 (`ai_consultation_records`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `user_id` | bigint(20) UNSIGNED DEFAULT NULL | 用户ID |
| `appointment_id` | bigint(20) UNSIGNED DEFAULT NULL | 预约ID |
| `user_query` | text COLLATE utf8mb4_unicode_ci NOT NULL | 用户问题 |
| `ai_response` | text COLLATE utf8mb4_unicode_ci NOT NULL | AI回复 |
| `recommended_resources` | text COLLATE utf8mb4_unicode_ci | 推荐资源（JSON格式） |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## AI 咨询设置表 (`ai_consultation_settings`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `provider` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'deepseek' | AI提供商 |
| `api_key` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | API密钥 |
| `api_url` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | API地址 |
| `model` | varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 模型名称 |
| `max_tokens` | int(11) NOT NULL DEFAULT '2000' | 最大token数 |
| `system_prompt` | text COLLATE utf8mb4_unicode_ci | 系统提示词 |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否启用 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 文章表 (`articles`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `title` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 文章标题 |
| `content` | longtext COLLATE utf8mb4_unicode_ci NOT NULL | 文章内容 |
| `summary` | varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 文章摘要 |
| `image` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 封面图片 |
| `category_id` | bigint(20) UNSIGNED NOT NULL | 分类ID |
| `author_id` | bigint(20) UNSIGNED DEFAULT NULL | 作者ID |
| `is_recommended` | tinyint(1) NOT NULL DEFAULT '0' | 是否推荐 |
| `views` | int(11) NOT NULL DEFAULT '0' | 浏览次数 |
| `publish_time` | timestamp NULL DEFAULT NULL | 发布时间 |
| `source` | varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 文章来源 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 文章分类表 (`article_categories`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 分类名称 |
| `description` | varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 分类描述 |
| `sort_order` | int(11) NOT NULL DEFAULT '0' | 排序顺序 |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否启用 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 文章审核表 (`article_reviews`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `article_id` | bigint(20) UNSIGNED NOT NULL | 文章ID |
| `reviewer_id` | bigint(20) UNSIGNED NOT NULL | 审核人ID |
| `comments` | text COLLATE utf8mb4_unicode_ci | 审核意见 |
| `reviewed_at` | timestamp NULL DEFAULT NULL | 审核时间 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 文章标签关联表 (`article_tag`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `article_id` | bigint(20) UNSIGNED NOT NULL | 文章ID |
| `tag_id` | bigint(20) UNSIGNED NOT NULL | 标签ID |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 文章标签表 (`article_tags`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 标签名称 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 测评 AI 设置表 (`assessment_ai_settings`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `api_key` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | DeepSeek API Key |
| `endpoint` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | DeepSeek 接口地址 |
| `model` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | DeepSeek 模型 ID |
| `system_prompt` | text COLLATE utf8mb4_unicode_ci NOT NULL | DeepSeek 系统提示词 |
| `user_prompt_template` | text COLLATE utf8mb4_unicode_ci NOT NULL | 用户提示词模板 |
| `max_tokens` | int(11) NOT NULL DEFAULT '512' | 最大 Token 数 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 启用状态 |

## 测评分析表 (`assessment_analyses`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `response_id` | bigint(20) UNSIGNED NOT NULL | 所属答卷 ID |
| `overall_score` | int(11) NOT NULL DEFAULT '0' | 总分 |
| `level_name` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 等级名称 |
| `description` | text COLLATE utf8mb4_unicode_ci | 结果描述 |
| `suggestions` | text COLLATE utf8mb4_unicode_ci | 建议 |
| `detailed_analysis` | text COLLATE utf8mb4_unicode_ci | 详细分析 |
| `ai_analysis` | longtext COLLATE utf8mb4_unicode_ci | AI分析结果 |
| `detail_json` | json NOT NULL | 分域得分及建议 JSON |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 测评答案表 (`assessment_answers`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `response_id` | bigint(20) UNSIGNED NOT NULL | 答卷ID |
| `question_id` | bigint(20) UNSIGNED NOT NULL | 题目ID |
| `option_id` | bigint(20) UNSIGNED DEFAULT NULL | 选项ID |
| `custom_value` | text COLLATE utf8mb4_unicode_ci | 自定义答案内容 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 测评选项表 (`assessment_options`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `question_id` | bigint(20) UNSIGNED NOT NULL | 所属题目 ID |
| `content` | text COLLATE utf8mb4_unicode_ci NOT NULL | 选项内容 |
| `score_value` | int(11) NOT NULL DEFAULT '0' | 选项对应评分 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 测评问卷表 (`assessment_questionnaires`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `title` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 问卷标题 |
| `description` | text COLLATE utf8mb4_unicode_ci | 问卷描述 |
| `domain` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 测评领域，如事业/家庭/健康 |
| `question_count` | int(11) NOT NULL DEFAULT '0' | 题目数量 |
| `est_duration` | int(11) NOT NULL DEFAULT '0' | 预计时长（分钟） |
| `cover_image` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 封面图片 URL |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否激活 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 测评问题表 (`assessment_questions`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `questionnaire_id` | bigint(20) UNSIGNED NOT NULL | 所属问卷 ID |
| `content` | text COLLATE utf8mb4_unicode_ci NOT NULL | 题干内容 |
| `sort_order` | int(11) NOT NULL DEFAULT '0' | 排序 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 测评答卷表 (`assessment_responses`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `user_id` | bigint(20) UNSIGNED NOT NULL | 用户 ID |
| `questionnaire_id` | bigint(20) UNSIGNED NOT NULL | 问卷 ID |
| `submitted_at` | timestamp NULL DEFAULT NULL | 提交时间 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `total_score` | int(11) NOT NULL DEFAULT '0' | 总分 |

## 测评结果配置表 (`assessment_result_configs`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `questionnaire_id` | bigint(20) UNSIGNED NOT NULL | 问卷 ID |
| `dimension_name` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 维度名称，如：焦虑程度、抑郁程度等 |
| `min_score` | int(11) NOT NULL | 最低分数 |
| `max_score` | int(11) NOT NULL | 最高分数 |
| `level_name` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 等级名称，如：轻度、中度、重度 |
| `description` | text COLLATE utf8mb4_unicode_ci | 结果描述 |
| `suggestion` | text COLLATE utf8mb4_unicode_ci | 建议内容 |
| `color` | varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '#28a745' | 显示颜色 |
| `sort_order` | int(11) NOT NULL DEFAULT '0' | 排序 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 咨询留言表 (`consultations`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `user_id` | bigint(20) UNSIGNED DEFAULT NULL | 用户ID |
| `name` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 姓名 |
| `phone` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 电话 |
| `email` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 邮箱 |
| `subject` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 主题 |
| `content` | text COLLATE utf8mb4_unicode_ci NOT NULL | 留言内容 |
| `admin_reply` | text COLLATE utf8mb4_unicode_ci | 管理员回复 |
| `replied_at` | timestamp NULL DEFAULT NULL | 回复时间 |
| `replied_by` | bigint(20) UNSIGNED DEFAULT NULL | 回复人ID |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 咨询预约表 (`consultation_appointments`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `user_id` | bigint(20) UNSIGNED NOT NULL | 用户ID |
| `counselor_id` | bigint(20) UNSIGNED NOT NULL | counselorID |
| `schedule_id` | bigint(20) UNSIGNED DEFAULT NULL | 排班ID |
| `consultation_type` | tinyint(4) NOT NULL DEFAULT '1' | 咨询方式：1文字，2语音，3视频 |
| `appointment_time` | datetime NOT NULL | 预约时间 |
| `status` | tinyint(4) NOT NULL DEFAULT '1' | 状态：0已取消，1待确认，2已确认，3进行中，4已完成 |
| `issue_description` | text COLLATE utf8mb4_unicode_ci | 问题描述 |
| `counselor_notes` | text COLLATE utf8mb4_unicode_ci | 咨询师备注 |
| `meeting_url` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 会议链接 |
| `meeting_password` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 会议密码 |
| `duration` | int(11) NOT NULL DEFAULT '60' | 咨询时长（分钟） |
| `payment_status` | tinyint(4) NOT NULL DEFAULT '0' | 支付状态：0未支付，1已支付，2已退款 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `deleted_at` | timestamp NULL DEFAULT NULL | 删除时间 |
| `confirmed_at` | timestamp NULL DEFAULT NULL | 预约确认时间 |
| `cancelled_at` | timestamp NULL DEFAULT NULL | 预约取消时间 |
| `completed_at` | timestamp NULL DEFAULT NULL | 预约完成时间 |
| `comment` | varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL | comment |
| `review` | varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 评价 |
| `rating` | int(3) DEFAULT '100' | 评分 |

## 咨询回复表 (`consultation_replies`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `consultation_id` | bigint(20) UNSIGNED NOT NULL | 留言ID |
| `user_id` | bigint(20) UNSIGNED DEFAULT NULL | 用户ID |
| `admin_id` | bigint(20) UNSIGNED DEFAULT NULL | 管理员ID |
| `content` | text COLLATE utf8mb4_unicode_ci NOT NULL | 回复内容 |
| `is_admin_reply` | tinyint(1) NOT NULL DEFAULT '0' | 是否为管理员回复 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `identity` | varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 回复身份 |

## 内容索引表 (`content_indices`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `indexable_type` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | indexabletype |
| `indexable_id` | bigint(20) UNSIGNED NOT NULL | indexableID |
| `type` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 内容类型：article, video, course_lesson |
| `title` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 内容标题 |
| `summary` | text COLLATE utf8mb4_unicode_ci | 内容摘要 |
| `image` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 封面图片 |
| `url` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 内容链接 |
| `metadata` | json DEFAULT NULL | 扩展元数据 |
| `vector` | blob | 向量数据 |
| `vector_generated` | tinyint(1) NOT NULL DEFAULT '0' | 向量是否已生成 |
| `vector_generated_at` | timestamp NULL DEFAULT NULL | 向量生成时间 |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否激活 |
| `view_count` | int(11) NOT NULL DEFAULT '0' | 查看次数 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 咨询师表 (`counselors`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 咨询师姓名 |
| `avatar` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 头像 |
| `gender` | tinyint(4) NOT NULL DEFAULT '0' | 性别：0未知，1男，2女 |
| `title` | varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 职称 |
| `phone` | varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 联系电话 |
| `email` | varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 邮箱 |
| `password` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 登录密码 |
| `introduction` | text COLLATE utf8mb4_unicode_ci | 个人简介 |
| `expertise` | text COLLATE utf8mb4_unicode_ci | 专业领域 |
| `experience` | text COLLATE utf8mb4_unicode_ci | 从业经历 |
| `education` | text COLLATE utf8mb4_unicode_ci | 教育背景 |
| `support_text` | tinyint(1) NOT NULL DEFAULT '1' | 支持文字咨询 |
| `support_voice` | tinyint(1) NOT NULL DEFAULT '1' | 支持语音咨询 |
| `support_video` | tinyint(1) NOT NULL DEFAULT '1' | 支持视频咨询 |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否激活 |
| `sort_order` | int(11) NOT NULL DEFAULT '0' | 排序 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `deleted_at` | timestamp NULL DEFAULT NULL | 删除时间 |

## 咨询师信息表 (`counselor_lxes`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 咨询师姓名 |
| `avatar` | varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 头像 |
| `gender` | tinyint(4) NOT NULL DEFAULT '0' | 性别：0未知，1男，2女 |
| `title` | varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 职称 |
| `phone` | varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 联系电话 |
| `email` | varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 邮箱 |
| `introduction` | text COLLATE utf8mb4_unicode_ci | 个人简介 |
| `expertise` | text COLLATE utf8mb4_unicode_ci | 专业领域 |
| `experience` | text COLLATE utf8mb4_unicode_ci | 从业经历 |
| `education` | text COLLATE utf8mb4_unicode_ci | 教育背景 |
| `support_text` | tinyint(1) NOT NULL DEFAULT '1' | 支持文字咨询 |
| `support_voice` | tinyint(1) NOT NULL DEFAULT '1' | 支持语音咨询 |
| `support_video` | tinyint(1) NOT NULL DEFAULT '1' | 支持视频咨询 |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否激活 |
| `sort_order` | int(11) NOT NULL DEFAULT '0' | 排序 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `deleted_at` | timestamp NULL DEFAULT NULL | 删除时间 |

## 咨询师排班表 (`counselor_schedules`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `counselor_id` | bigint(20) UNSIGNED NOT NULL | counselorID |
| `date` | date NOT NULL | 日期 |
| `start_time` | time NOT NULL | 开始时间 |
| `end_time` | time NOT NULL | 结束时间 |
| `is_available` | tinyint(1) NOT NULL DEFAULT '1' | 是否可预约 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 课程课时表 (`course_lessons`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `title` | varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL | 课程标题 |
| `slug` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | Slug |
| `image` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 封面图片 |
| `description` | text COLLATE utf8mb4_unicode_ci | 课程描述 |
| `content` | text COLLATE utf8mb4_unicode_ci | 文章内容 |
| `video_url` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 视频URL |
| `video_duration` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 视频时长 |
| `resources` | text COLLATE utf8mb4_unicode_ci | 课程资源，JSON格式 |
| `category_id` | bigint(20) UNSIGNED DEFAULT NULL | 分类ID |
| `author_id` | bigint(20) UNSIGNED DEFAULT NULL | authorID |
| `views` | int(11) NOT NULL DEFAULT '0' | 浏览量 |
| `likes` | int(11) NOT NULL DEFAULT '0' | 点赞数 |
| `lessons_count` | int(11) NOT NULL DEFAULT '1' | 课时数量 |
| `publish_time` | timestamp NULL DEFAULT NULL | 发布时间 |
| `type` | tinyint(4) NOT NULL DEFAULT '1' | 类型：1文章，2视频，3混合 |
| `level` | tinyint(4) NOT NULL DEFAULT '1' | 难度级别：1入门，2进阶，3高级 |
| `status` | tinyint(4) NOT NULL DEFAULT '0' | 状态：0草稿，1已发布，2已下架 |
| `is_recommended` | tinyint(1) NOT NULL DEFAULT '0' | 是否推荐 |
| `is_free` | tinyint(1) NOT NULL DEFAULT '1' | 是否免费 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `deleted_at` | timestamp NULL DEFAULT NULL | 删除时间 |

## 课程课时分类表 (`course_lesson_categories`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 分类名称 |
| `description` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 分类描述 |
| `icon` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 分类图标 |
| `sort` | int(11) NOT NULL DEFAULT '0' | 排序 |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否启用 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 课程课时进度表 (`course_lesson_progress`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `user_id` | bigint(20) UNSIGNED NOT NULL | 用户ID |
| `course_lesson_id` | bigint(20) UNSIGNED NOT NULL | 课程课时ID |
| `progress` | int(11) NOT NULL DEFAULT '0' | 学习进度，百分比 |
| `current_position` | int(11) NOT NULL DEFAULT '0' | 当前位置，文章为字符位置，视频为秒数 |
| `last_access_time` | timestamp NULL DEFAULT NULL | 最后访问时间 |
| `is_completed` | tinyint(1) NOT NULL DEFAULT '0' | 是否已完成 |
| `notes` | text COLLATE utf8mb4_unicode_ci | 用户笔记 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 课程课时标签关联表 (`course_lesson_tag`)
存储课程课时与标签的关联关系。

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `course_lesson_id` | bigint(20) UNSIGNED NOT NULL | 课程课时ID |
| `course_lesson_tag_id` | bigint(20) UNSIGNED NOT NULL | 课程课时标签关联ID |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 课程课时标签表 (`course_lesson_tags`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 标签名称 |
| `description` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 标签描述 |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否启用 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 课程报名表 (`course_registrations`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `user_id` | bigint(20) UNSIGNED NOT NULL | 用户ID |
| `course_id` | bigint(20) UNSIGNED NOT NULL | 课程ID |
| `registration_code` | varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL | 报名编号 |
| `status` | tinyint(4) NOT NULL DEFAULT '1' | 状态：0已取消，1待支付，2已确认 |
| `department` | varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 部门名称（团体报名用） |
| `participants_count` | int(11) NOT NULL DEFAULT '1' | 参与人数 |
| `participants_info` | text COLLATE utf8mb4_unicode_ci | 参与人员信息（JSON格式） |
| `remarks` | text COLLATE utf8mb4_unicode_ci | 备注 |
| `payment_status` | tinyint(4) NOT NULL DEFAULT '0' | 支付状态：0未支付，1已支付，2已退款 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `deleted_at` | timestamp NULL DEFAULT NULL | 删除时间 |

## 失败任务表 (`failed_jobs`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `uuid` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | uuid |
| `connection` | text COLLATE utf8mb4_unicode_ci NOT NULL | connection |
| `queue` | text COLLATE utf8mb4_unicode_ci NOT NULL | queue |
| `payload` | longtext COLLATE utf8mb4_unicode_ci NOT NULL | payload |
| `exception` | longtext COLLATE utf8mb4_unicode_ci NOT NULL | exception |
| `failed_at` | timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP | failed时间 |

## 热线表 (`hotlines`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 热线名称 |
| `phone_number` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 热线电话号码 |
| `description` | text COLLATE utf8mb4_unicode_ci | 热线描述 |
| `service_hours` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 服务时间，如24小时、9:00-18:00等 |
| `sort_order` | int(11) NOT NULL DEFAULT '0' | 排序顺序 |
| `is_enabled` | tinyint(1) NOT NULL DEFAULT '1' | 是否启用 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `deleted_at` | timestamp NULL DEFAULT NULL | 删除时间 |

## 热线记录表 (`hotline_records`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `hotline_id` | bigint(20) UNSIGNED NOT NULL | hotlineID |
| `user_id` | bigint(20) UNSIGNED DEFAULT NULL | 用户ID |
| `ip_address` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 用户IP地址 |
| `user_agent` | longtext COLLATE utf8mb4_unicode_ci | 用户浏览器信息 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 直播活动表 (`live_shows`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `title` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 直播标题 |
| `description` | text COLLATE utf8mb4_unicode_ci | 直播描述 |
| `cover_image` | varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 封面图片 |
| `live_url` | varchar(1000) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 微信视频号直播链接 |
| `qr_code_image` | varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 预约二维码图片 |
| `counselor_id` | bigint(20) UNSIGNED DEFAULT NULL | 主播咨询师ID |
| `scheduled_at` | timestamp NULL DEFAULT NULL | 预定直播时间 |
| `ended_at` | datetime DEFAULT NULL | 结束时间 |
| `is_featured` | tinyint(1) NOT NULL DEFAULT '0' | 是否首页推荐 |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否启用 |
| `sort_order` | int(11) NOT NULL DEFAULT '0' | 排序权重 |
| `notice` | text COLLATE utf8mb4_unicode_ci | 直播公告/备注 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 消息表 (`messages`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `user_id` | bigint(20) UNSIGNED NOT NULL | 用户ID |
| `counselor_id` | bigint(20) UNSIGNED NOT NULL | 咨询师ID |
| `appointment_id` | bigint(20) UNSIGNED DEFAULT NULL | 预约ID |
| `sender_type` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 发送者类型：user/counselor |
| `content` | text COLLATE utf8mb4_unicode_ci NOT NULL | 消息内容 |
| `is_read` | tinyint(1) NOT NULL DEFAULT '0' | 是否已读 |
| `read_at` | timestamp NULL DEFAULT NULL | 阅读时间 |
| `attachment` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 附件 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 数据库迁移表 (`migrations`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | int(10) UNSIGNED NOT NULL | 主键ID |
| `migration` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | migration |
| `batch` | int(11) NOT NULL | batch |

## 新闻表 (`news`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `title` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 新闻标题 |
| `slug` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | URL别名 |
| `summary` | text COLLATE utf8mb4_unicode_ci | 新闻摘要 |
| `content` | longtext COLLATE utf8mb4_unicode_ci NOT NULL | 新闻内容 |
| `cover_image` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 封面图 |
| `source` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 新闻来源 |
| `author` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 作者 |
| `category_id` | bigint(20) UNSIGNED NOT NULL | 分类ID |
| `is_featured` | tinyint(1) NOT NULL DEFAULT '0' | 是否推荐 |
| `is_published` | tinyint(1) NOT NULL DEFAULT '1' | 是否发布 |
| `published_at` | datetime DEFAULT NULL | 发布时间 |
| `view_count` | int(11) NOT NULL DEFAULT '0' | 浏览次数 |
| `share_count` | int(11) NOT NULL DEFAULT '0' | 分享次数 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `deleted_at` | timestamp NULL DEFAULT NULL | 删除时间 |

## 新闻分类表 (`news_categories`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 分类名称 |
| `slug` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 分类别名，用于URL |
| `description` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 分类描述 |
| `sort_order` | int(11) NOT NULL DEFAULT '0' | 排序 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 新闻标签关联表 (`news_tag`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `news_id` | bigint(20) UNSIGNED NOT NULL | 新闻ID |
| `news_tag_id` | bigint(20) UNSIGNED NOT NULL | 新闻标签关联ID |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 新闻标签表 (`news_tags`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 标签名称 |
| `slug` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 标签别名，用于URL |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 新闻浏览表 (`news_views`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `news_id` | bigint(20) UNSIGNED NOT NULL | 新闻ID |
| `user_id` | bigint(20) UNSIGNED DEFAULT NULL | 用户ID |
| `ip_address` | varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL | IP地址 |
| `user_agent` | longtext COLLATE utf8mb4_unicode_ci | 用户agent |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 线下课程表 (`offline_courses`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `title` | varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL | 课程标题 |
| `image` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 课程图片 |
| `lecturer_id` | bigint(20) DEFAULT NULL | lecturerID |
| `description` | text COLLATE utf8mb4_unicode_ci | 课程描述 |
| `outline` | text COLLATE utf8mb4_unicode_ci | 课程大纲 |
| `location` | varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 上课地点 |
| `start_time` | datetime NOT NULL | 开始时间 |
| `end_time` | datetime NOT NULL | 结束时间 |
| `registration_deadline` | datetime NOT NULL | 报名截止时间 |
| `max_participants` | int(11) NOT NULL DEFAULT '30' | 最大参与人数 |
| `current_participants` | int(11) NOT NULL DEFAULT '0' | 当前参与人数 |
| `status` | tinyint(4) NOT NULL DEFAULT '1' | 状态：0待发布，1已发布，2已结束 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `deleted_at` | timestamp NULL DEFAULT NULL | 删除时间 |
| `category` | tinyint(3) UNSIGNED NOT NULL DEFAULT '1' | 课程分类 1–10 |

## 密码重置令牌表 (`password_reset_tokens`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `email` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 邮箱 |
| `token` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 令牌 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |

## 个人访问令牌表 (`personal_access_tokens`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `tokenable_type` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | tokenabletype |
| `tokenable_id` | bigint(20) UNSIGNED NOT NULL | tokenableID |
| `name` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 名称 |
| `token` | varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL | 令牌 |
| `abilities` | text COLLATE utf8mb4_unicode_ci | abilities |
| `last_used_at` | timestamp NULL DEFAULT NULL | lastused时间 |
| `expires_at` | timestamp NULL DEFAULT NULL | expires时间 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 答题活动表 (`quiz_activities`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `title` | varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL | 标题 |
| `description` | text COLLATE utf8mb4_unicode_ci | 描述 |
| `cover_image` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 封面图片 |
| `start_time` | datetime NOT NULL | 开始时间 |
| `end_time` | datetime NOT NULL | 结束时间 |
| `pass_score` | int(11) NOT NULL DEFAULT '60' | pass分数 |
| `max_attempts` | int(11) NOT NULL DEFAULT '1' | maxattempts |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否启用 |
| `show_answers_after_submit` | tinyint(1) NOT NULL DEFAULT '0' | showanswersaftersubmit |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `deleted_at` | timestamp NULL DEFAULT NULL | 删除时间 |

## 答题答案表 (`quiz_answers`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `attempt_id` | bigint(20) UNSIGNED NOT NULL | 记录ID |
| `question_id` | bigint(20) UNSIGNED NOT NULL | 题目ID |
| `user_answer` | text COLLATE utf8mb4_unicode_ci NOT NULL | 用户答案 |
| `is_correct` | tinyint(1) NOT NULL DEFAULT '0' | 是否correct |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 答题记录表 (`quiz_attempts`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `quiz_activity_id` | bigint(20) UNSIGNED NOT NULL | 答题activityID |
| `user_id` | bigint(20) UNSIGNED NOT NULL | 用户ID |
| `score` | int(11) NOT NULL DEFAULT '0' | 分数 |
| `total_points` | int(11) NOT NULL DEFAULT '0' | totalpoints |
| `correct_count` | int(11) NOT NULL DEFAULT '0' | correct数量 |
| `total_questions` | int(11) NOT NULL DEFAULT '0' | totalquestions |
| `has_won_prize` | tinyint(1) NOT NULL DEFAULT '0' | haswonprize |
| `is_completed` | tinyint(1) NOT NULL DEFAULT '0' | 是否completed |
| `completed_at` | datetime DEFAULT NULL | 完成时间 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 答题选项表 (`quiz_options`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `question_id` | bigint(20) UNSIGNED NOT NULL | 题目ID |
| `option_text` | text COLLATE utf8mb4_unicode_ci NOT NULL | 选项text |
| `is_correct` | tinyint(1) NOT NULL DEFAULT '0' | 是否correct |
| `order` | int(11) NOT NULL DEFAULT '0' | 排序 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 答题奖品表 (`quiz_prizes`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `quiz_activity_id` | bigint(20) UNSIGNED NOT NULL | 答题activityID |
| `name` | varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL | 名称 |
| `description` | text COLLATE utf8mb4_unicode_ci | 描述 |
| `image` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 图片 |
| `quantity` | int(11) NOT NULL DEFAULT '0' | quantity |
| `prize_type` | varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL | prizetype |
| `min_score` | int(11) NOT NULL DEFAULT '0' | min分数 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 答题获奖者表 (`quiz_prize_winners`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `quiz_activity_id` | bigint(20) UNSIGNED NOT NULL | 答题activityID |
| `prize_id` | bigint(20) UNSIGNED NOT NULL | prizeID |
| `user_id` | bigint(20) UNSIGNED NOT NULL | 用户ID |
| `attempt_id` | bigint(20) UNSIGNED NOT NULL | 记录ID |
| `winner_name` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | winner名称 |
| `contact_info` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | contactinfo |
| `shipping_address` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | shipping地址 |
| `status` | varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'pending' | 状态 |
| `admin_notes` | text COLLATE utf8mb4_unicode_ci | 管理员备注 |
| `claimed_at` | datetime DEFAULT NULL | claimed时间 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 答题题目表 (`quiz_questions`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `quiz_activity_id` | bigint(20) UNSIGNED NOT NULL | 答题activityID |
| `question_text` | text COLLATE utf8mb4_unicode_ci NOT NULL | 题目text |
| `question_type` | varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL | 题目type |
| `explanation` | text COLLATE utf8mb4_unicode_ci | explanation |
| `points` | int(11) NOT NULL DEFAULT '1' | points |
| `order` | int(11) NOT NULL DEFAULT '0' | 排序 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 短信验证码表 (`sms_codes`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `phone` | varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL | 电话 |
| `code` | varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL | code |
| `type` | varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'login' | type |
| `expires_at` | timestamp NOT NULL | expires时间 |
| `used` | tinyint(1) NOT NULL DEFAULT '0' | used |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 系统设置表 (`system_settings`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键 |
| `key` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 配置键（唯一） |
| `value` | text COLLATE utf8mb4_unicode_ci | 配置值（JSON 或纯文本） |
| `label` | varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 配置项说明 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 用户表 (`users`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 名称 |
| `email` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 邮箱 |
| `phone` | varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 电话 |
| `phone_verified` | tinyint(1) NOT NULL DEFAULT '0' | 电话verified |
| `avatar` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 头像 |
| `email_verified_at` | timestamp NULL DEFAULT NULL | 邮箱verified时间 |
| `password` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 密码 |
| `remember_token` | varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 记住登录 |
| `last_login_at` | timestamp NULL DEFAULT NULL | lastlogin时间 |
| `last_login_ip` | varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL | lastloginIP |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `is_contact` | tinyint(1) NOT NULL DEFAULT '0' | 是否是联络人 0否 1是 |
| `enterprise` | varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 单位名称 |

## 视频表 (`videos`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `title` | varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL | 视频标题 |
| `description` | text COLLATE utf8mb4_unicode_ci | 视频简短描述 |
| `content` | longtext COLLATE utf8mb4_unicode_ci | 视频详细内容/介绍 |
| `image` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 视频封面图片 |
| `video_url` | varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 视频URL或资源路径 |
| `video_duration` | varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 视频时长 |
| `category_id` | int(10) UNSIGNED DEFAULT NULL | 分类ID |
| `author_id` | int(10) UNSIGNED DEFAULT NULL | 作者ID |
| `views` | int(10) UNSIGNED NOT NULL DEFAULT '0' | 观看次数 |
| `is_recommended` | tinyint(1) NOT NULL DEFAULT '0' | 是否推荐 |
| `status` | tinyint(4) NOT NULL DEFAULT '0' | 状态：0=草稿，1=待审核，2=已发布，3=已拒绝 |
| `publish_time` | timestamp NULL DEFAULT NULL | 发布时间 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |
| `deleted_at` | timestamp NULL DEFAULT NULL | 删除时间 |

## 视频审核日志表 (`video_audit_logs`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `video_id` | bigint(20) UNSIGNED NOT NULL | 视频ID |
| `admin_id` | int(10) UNSIGNED NOT NULL | 审核管理员ID |
| `status` | tinyint(4) NOT NULL | 审核状态：1=待审核，2=通过，3=拒绝 |
| `reason` | varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 审核意见/拒绝原因 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 视频分类表 (`video_categories`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | int(10) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 分类名称 |
| `description` | varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL | 分类描述 |
| `sort` | int(11) NOT NULL DEFAULT '0' | 排序值，越大越靠前 |
| `is_active` | tinyint(1) NOT NULL DEFAULT '1' | 是否启用 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

## 视频标签关联表 (`video_tag`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | bigint(20) UNSIGNED NOT NULL | 主键ID |
| `video_id` | bigint(20) UNSIGNED NOT NULL | 视频ID |
| `tag_id` | int(10) UNSIGNED NOT NULL | 标签ID |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |

## 视频标签表 (`video_tags`)

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | int(10) UNSIGNED NOT NULL | 主键ID |
| `name` | varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL | 标签名称 |
| `created_at` | timestamp NULL DEFAULT NULL | 创建时间 |
| `updated_at` | timestamp NULL DEFAULT NULL | 更新时间 |

