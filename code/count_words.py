import re
import sys

def count_words(filepath):
    """读取txt文件，统计单词总个数，忽略大小写，简单过滤标点"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # 转换为小写（忽略大小写），使用正则提取单词（只保留字母数字，过滤标点）
        words = re.findall(r'\b[a-zA-Z0-9]+\b', content.lower())
        return len(words)
    except FileNotFoundError:
        print(f"错误：文件 {filepath} 不存在")
        sys.exit(1)
    except Exception as e:
        print(f"读取文件出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python count_words.py <txt文件路径>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    count = count_words(filepath)
    print(f"文件 {filepath} 单词总个数: {count}")
