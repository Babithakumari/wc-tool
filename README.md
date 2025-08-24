# 📝 Build Your Own `wc` Tool (ccwc)

This project is an implementation of the classic Unix command line tool **`wc`** (word count), following the Unix philosophy of *small, simple tools connected by clean interfaces*.  

It supports counting **bytes, lines, words, and characters** from files or standard input, just like the real `wc`.

---

## 🚀 Features

- `-c` → Count **bytes** in a file  
- `-l` → Count **lines** in a file  
- `-w` → Count **words** in a file  
- `-m` → Count **characters** in a file (multi-byte safe)  
- **Default (no flags)** → Show **lines, words, and bytes**  
- Supports reading from **files** or from **standard input**  

---

## 🛠 Usage

```bash
python3 ccwc.py [OPTION]... [FILE]...
```
The following options can be used with this tool:

- `-c` → Count the number of **bytes** in the file  
- `-m` → Count the number of **characters** in the file  
- `-l` → Count the number of **lines** in the file  
- `-w` → Count the number of **words** in the file  

If no FILE is specified, input will be read from stdin.