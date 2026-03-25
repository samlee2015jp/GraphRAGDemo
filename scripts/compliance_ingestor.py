import os
from pathlib import Path

# 定义源文件夹名称（你可以根据之前的选择修改）
SOURCE_FOLDER = "AI_FinAds_Compliance_Source"

def setup_compliance_environment():
    """
    初始化环境：创建源码文件夹和必要的子目录
    """
    # 获取当前工作目录
    base_path = Path.cwd()
    source_path = base_path / SOURCE_FOLDER
    
    # 建议的子分类
    sub_folders = ['CN_Standard', 'JP_Standard', 'EN_Standard']
    
    if not source_path.exists():
        source_path.mkdir(parents=True)
        print(f"✅ 已创建主文件夹: {SOURCE_FOLDER}")
    
    for sub in sub_folders:
        sub_path = source_path / sub
        if not sub_path.exists():
            sub_path.mkdir()
            print(f"  - 已创建子文件夹: {sub}")

def scan_compliance_files():
    """
    扫描文件夹中的所有文件并列出
    """
    source_path = Path.cwd() / SOURCE_FOLDER
    files = list(source_path.rglob('*')) # 递归扫描所有文件
    
    print(f"\n🔍 正在扫描 {SOURCE_FOLDER} 中的文件...")
    
    document_count = 0
    for file in files:
        if file.is_file():
            document_count += 1
            print(f"📄 发现文档: {file.relative_to(source_path)}")
            
    if document_count == 0:
        print("⚠️ 文件夹目前是空的，请放入相关的法律法规 PDF 或 TXT 文件。")
    else:
        print(f"🚀 共找到 {document_count} 份源文件，准备进行 GraphRAG 处理。")

def main():
    """这里是脚本独立运行时的入口"""
    print("🚀 正在以独立模式运行合规文档导入工具...")
    setup_compliance_environment()
    scan_compliance_files()

if __name__ == "__main__":
    # 只有直接运行本文件时，才会执行 main()
    main()