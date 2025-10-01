# samples/quick_demo.py (stub)
import sys, os, textwrap

def main():
    try:
        from see_proto import PySee  # wheelが入っていればimport成功
    except Exception:
        print(textwrap.dedent("""
        [SEE demo]
        まだ wheel / Demo ZIP がありません。
          1) Releases から Demo_v*.zip をダウンロードして展開
          2) pip install see_proto --find-links https://github.com/<you>/see_proto/releases/latest/download
          3) 展開先の samples/quick_demo.py を実行
        """).strip())
        return 0

    print("[OK] see_proto wheel detected. Run the full demo from the Demo ZIP for KPI.")
    if os.path.exists("samples/.placeholder.see"):
        s = PySee.open("samples/.placeholder.see")
        print("Opened placeholder .see (sanity check).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
