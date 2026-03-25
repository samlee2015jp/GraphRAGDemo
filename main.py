import scripts.compliance_ingestor as compliance_ingestor

if __name__ == "__main__":
    # 初始化环境并扫描文件
    compliance_ingestor.setup_compliance_environment()
    compliance_ingestor.scan_compliance_files()