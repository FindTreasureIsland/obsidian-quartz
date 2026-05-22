from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = Workbook()

header_fill = PatternFill('solid', start_color='4472C4')
header_font = Font(bold=True, color='FFFFFF', size=10)
header_align = Alignment(horizontal='center', vertical='center', wrap_text=True)
thin_border = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin')
)

ws_detail = wb.create_sheet("详细资产表")

# 统一列结构
detail_headers = [
    '序号', '园区', '栋号', '楼层', '面积(m²)', '建筑类型', '层高(m)',
    '承重/首层承重', '二层承重', '首层租金', '租金', '物业费', '物业公司', '状态', 'VR点位规划'
]

for col, header in enumerate(detail_headers, 1):
    cell = ws_detail.cell(row=1, column=col, value=header)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = header_align
    cell.border = thin_border

# 序号0: 发展中心 1楼
data = [
    (0, '发展中心', '', '1楼', '', '公共建筑（商业、办公）', '', '', '', '', '', '', '高投集团', '空置', 5),
    (1, '发展中心', '—', '4楼', 1656.30, '公共建筑（商业、办公）', '', 1000, 500, '', 26, 7, '高投集团', '空置', ''),
    (2, '发展中心', '—', '5楼', 1263.44, '公共建筑（商业、办公）', '', 1000, 500, '', 26, 7, '高投集团', '空置', 4),
    (3, '发展中心', '—', '6楼', 1113.96, '公共建筑（商业、办公）', '', 1000, 500, '', 26, 7, '高投集团', '空置', 2),
    (4, '发展中心', '—', '7楼', 1230.68, '公共建筑（商业、办公）', '', 1000, 500, '', 26, 7, '高投集团', '空置', ''),
    (5, '发展中心', '—', '8楼', 1230.68, '公共建筑（商业、办公）', '', 1000, 500, '', 26, 7, '高投集团', '空置', 15),
    (6, '发展中心', '—', '9楼', 1230.68, '公共建筑（商业、办公）', '', 1000, 500, '', 26, 7, '高投集团', '空置', 15),
    (7, '发展中心', '—', '10楼', 1230.68, '公共建筑（商业、办公）', '', 1000, 500, '', 26, 7, '高投集团', '空置', ''),
    # 孵化园区 (承重、租金)
    (8, '孵化园区', 'A楼', '8层', 2125, '丁/戊类厂房', 4.5, '240-700', '', '', '待定', '', '创益产投', '空置', 8),
    (9, '孵化园区', 'A楼', '9层', 2125, '丁/戊类厂房', 4.5, '240-700', '', '', '待定', '', '创益产投', '空置', 8),
    (10, '孵化园区', 'A楼', '10层', 2125, '丁/戊类厂房', 4.5, '240-700', '', '', '待定', '', '创益产投', '空置', 8),
    (11, '孵化园区', 'B楼', '4层', 2300, '丁/戊类厂房', 4.5, '240-700', '', '', '待定', '', '创益产投', '待装修', 40),
    (12, '孵化园区', 'B楼', '5层', 2300, '丁/戊类厂房', 4.5, '240-700', '', '', '待定', '', '创益产投', '待装修', 40),
    # 伟禾生物园 (首层租金、二层及以上租金、物业费)
    (13, '伟禾生物园', '生产车间1#', '1-4层', 2121.39, '丁类厂房', 4.5, '', '', 13, 8, 1.5, '高投资管公司', '运营中', 60),
    (14, '伟禾生物园', '生产车间2#', '3-4层', 2133.29, '丁类厂房', 4.5, '', '', 13, 8, 1.5, '高投资管公司', '运营中', 40),
    (15, '伟禾生物园', '生产车间3#', '3-4层', 2279.55, '丁类厂房', 4.5, '', '', 13, 8, 1.5, '高投资管公司', '运营中', 40),
    (16, '伟禾生物园', '生产车间4#', '1-4层', 2296.14, '丁类厂房', 4.5, '', '', 13, 8, 1.5, '高投资管公司', '运营中', 60),
    (17, '伟禾生物园', '科研楼', '1层', '', '丙类厂房', 6, '', '', 15, '', 1.5, '高投资管公司', '运营中', 10),
    (18, '伟禾生物园', '科研楼', '2-4层', 1211.12, '丙类厂房', 6, '', '', '', 9, 1.5, '高投资管公司', '运营中', 45),
    # 金润产业园 (租金、物业费)
    (19, '金润产业园', '1栋', '2层', 2128.21, '丙类厂房', 4.5, '', '', '', 10, 1.1, '金工集团', '运营中', 10),
    (20, '金润产业园', '1栋', '3层', 2280.95, '丙类厂房', 4.5, '', '', '', 10, 1.1, '金工集团', '运营中', 10),
    (21, '金润产业园', '3栋', '2层', 1231.69, '丙类厂房', 4.5, '', '', '', 10, 1.1, '金工集团', '运营中', 12),
    (22, '金润产业园', '3栋', '3层', 605, '丙类厂房', 4.5, '', '', '', 10, 1.1, '金工集团', '运营中', 12),
    (23, '金润产业园', '5栋', '1层', 2292.78, '丙类厂房', 4.5, '', '', '', 11, 1.1, '金工集团', '运营中', 8),
    (24, '金润产业园', '5栋', '2层', 7364.20, '丙类厂房', 4.5, '', '', '', 10, 1.1, '金工集团', '运营中', 10),
    (25, '金润产业园', '5栋', '3层', 2971.90, '丙类厂房', 4.5, '', '', '', 10, 1.1, '金工集团', '运营中', 10),
    (26, '金润产业园', '5栋', '4层', 2971.90, '丙类厂房', 4.5, '', '', '', 9, 1.1, '金工集团', '运营中', 8),
    (27, '金润产业园', '6栋', '3层', 2986.82, '丙类厂房', 4.5, '', '', '', 10, 1.1, '金工集团', '运营中', 10),
    (28, '金润产业园', '12栋', '—', 2986.82, '丙类厂房', '6-10', '', '', '', '待定', '', '金工集团', '待修缮', 25),
    (29, '金润产业园', '15栋', '1层', 11421.30, '丙类厂房', 4.5, '', '', '', '待定', '', '金工集团', '待定', 15),
    (30, '金润产业园', '15栋', '2层', '', '丙类厂房', 4.5, '', '', '', '待定', '', '金工集团', '待定', 20),
    (31, '金润产业园', '15栋', '3层', '', '丙类厂房', 4.5, '', '', '', '待定', '', '金工集团', '待定', 20),
    (32, '金润产业园', '15栋', '3层', '', '丙类厂房', 4.5, '', '', '', '待定', '', '金工集团', '待定', 20),
]

for i, row_data in enumerate(data):
    row = 2 + i
    for col, value in enumerate(row_data, 1):
        cell = ws_detail.cell(row=row, column=col, value=value)
        cell.border = thin_border
        cell.alignment = Alignment(horizontal='center', vertical='center')

col_widths = [6, 12, 14, 8, 12, 18, 8, 12, 10, 10, 10, 10, 12, 10, 12]
for i, width in enumerate(col_widths, 1):
    ws_detail.column_dimensions[get_column_letter(i)].width = width

ws_detail.row_dimensions[1].height = 25
ws_detail.freeze_panes = 'A2'

# ========== Sheet 1: VR点位汇总表 ==========
ws_summary = wb.create_sheet("VR点位汇总表", 0)

ws_summary.merge_cells('A1:D1')
ws_summary['A1'] = '宜宾市高新区产业园区VR点位规划汇总'
ws_summary['A1'].font = Font(bold=True, size=16)
ws_summary['A1'].alignment = Alignment(horizontal='center')

sum_headers = ['园区名称', '栋号/楼层', '面积(m²)', 'VR点位规划']
for col, header in enumerate(sum_headers, 1):
    cell = ws_summary.cell(row=3, column=col, value=header)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = header_align
    cell.border = thin_border

summary_data = [
    ('发展中心', '1楼', '', 5),
    ('发展中心', '5楼', 1263.44, 4),
    ('发展中心', '6楼', 1113.96, 2),
    ('发展中心', '8楼', 1230.68, 15),
    ('发展中心', '9楼', 1230.68, 15),
    ('孵化园区', 'A楼 8层', 2125, 8),
    ('孵化园区', 'A楼 9层', 2125, 8),
    ('孵化园区', 'A楼 10层', 2125, 8),
    ('孵化园区', 'B楼 4层', 2300, 40),
    ('孵化园区', 'B楼 5层', 2300, 40),
    ('伟禾生物园', '生产车间1# 1-4层', 2121.39, 60),
    ('伟禾生物园', '生产车间2# 3-4层', 2133.29, 40),
    ('伟禾生物园', '生产车间3# 3-4层', 2279.55, 40),
    ('伟禾生物园', '生产车间4# 1-4层', 2296.14, 60),
    ('伟禾生物园', '科研楼 1层', '', 10),
    ('伟禾生物园', '科研楼 2-4层', 1211.12, 45),
    ('金润产业园', '1栋 2层', 2128.21, 10),
    ('金润产业园', '1栋 3层', 2280.95, 10),
    ('金润产业园', '3栋 2层', 1231.69, 12),
    ('金润产业园', '3栋 3层', 605, 12),
    ('金润产业园', '5栋 1层', 2292.78, 8),
    ('金润产业园', '5栋 2层', 7364.20, 10),
    ('金润产业园', '5栋 3层', 2971.90, 10),
    ('金润产业园', '5栋 4层', 2971.90, 8),
    ('金润产业园', '6栋 3层', 2986.82, 10),
    ('金润产业园', '12栋 —', 2986.82, 25),
    ('金润产业园', '15栋 1层', 11421.30, 15),
    ('金润产业园', '15栋 2层', '', 20),
    ('金润产业园', '15栋 3层', '', 20),
    ('金润产业园', '15栋 3层', '', 20),
]

park_totals = {'发展中心': 41, '孵化园区': 104, '伟禾生物园': 255, '金润产业园': 190}
park_list = ['发展中心', '孵化园区', '伟禾生物园', '金润产业园']

# 重新组织数据，按园区分组
park_data = {}
for name, building, area, vr in summary_data:
    if name not in park_data:
        park_data[name] = []
    park_data[name].append((building, area, vr))

row = 4
for i, park_name in enumerate(park_list):
    # 写入该园区的所有数据行
    for building, area, vr in park_data[park_name]:
        ws_summary.cell(row=row, column=1, value=park_name)
        ws_summary.cell(row=row, column=2, value=building)
        ws_summary.cell(row=row, column=3, value=area if area else '')
        ws_summary.cell(row=row, column=4, value=vr)
        for col in range(1, 5):
            cell = ws_summary.cell(row=row, column=col)
            cell.border = thin_border
            cell.alignment = Alignment(horizontal='center', vertical='center')
        row += 1

    # 写入小计行
    ws_summary.cell(row=row, column=1, value=f'{park_name} 小计')
    ws_summary.cell(row=row, column=4, value=park_totals[park_name])
    for col in range(1, 5):
        cell = ws_summary.cell(row=row, column=col)
        cell.fill = PatternFill('solid', start_color='D9E1F2')
        cell.font = Font(bold=True)
        cell.border = thin_border
        cell.alignment = Alignment(horizontal='center', vertical='center')
    row += 1

    # 空行分隔（最后一项后不加分隔）
    if i < len(park_list) - 1:
        row += 1

# 总计行
ws_summary.cell(row=row, column=1, value='总计')
ws_summary.cell(row=row, column=4, value=590)
for col in range(1, 5):
    cell = ws_summary.cell(row=row, column=col)
    cell.fill = PatternFill('solid', start_color='4472C4')
    cell.font = Font(bold=True, color='FFFFFF')
    cell.border = thin_border
    cell.alignment = Alignment(horizontal='center', vertical='center')

ws_summary.column_dimensions['A'].width = 18
ws_summary.column_dimensions['B'].width = 22
ws_summary.column_dimensions['C'].width = 15
ws_summary.column_dimensions['D'].width = 15
ws_summary.row_dimensions[1].height = 30
ws_summary.row_dimensions[3].height = 25

output_path = '/Users/crio/Library/CloudStorage/OneDrive-个人/Obsidian/工作/songzhiyong/03个人文档/02解决方案/宜宾市高新区产业园区VR点位规划.xlsx'
wb.save(output_path)

print(f'已保存: {output_path}')

# 验证详细表VR数据
print(f'\n===== 详细资产表数据验证 =====')
vr_sum = 0
for row_num in range(2, 35):
    seq = ws_detail.cell(row=row_num, column=1).value
    park = ws_detail.cell(row=row_num, column=2).value
    floor = ws_detail.cell(row=row_num, column=4).value
    status = ws_detail.cell(row=row_num, column=14).value
    vr = ws_detail.cell(row=row_num, column=15).value
    vr_int = vr if vr else 0
    print(f'序号{seq:2d} | {park:10s} | {str(floor):8s} | {str(status):10s} | VR:{vr_int}')
    vr_sum += vr_int

print(f'\n===== VR点位汇总 =====')
for name, total in park_totals.items():
    print(f'  {name}: {total}')
print(f'  总计: 590')
