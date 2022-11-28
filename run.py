
if __name__ == "__main__":
    import sys
    sys.path.append('')
    print(f"正在使用如下参数启动webui: {' '.join(sys.argv[1:])}")
    import webui
    webui.webui()
