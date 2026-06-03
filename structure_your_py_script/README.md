## Structure your python script

### Make your script run using Shebang

```python3
 #!/usr/bin/env python3

```


### Format your python code using `Ruff`

```python3
# ruff check
ruff check <file_name>

```

```python3
@AshuApurva14 ➜ /workspaces/python-for-devops/structure_your_py_script (main) $ ruff check quotes_generator.py 
F401 [*] `random` imported but unused
 --> quotes_generator.py:3:8
  |
1 | #!/usr/bin/env python3
2 |
3 | import random
  |        ^^^^^^
4 |
5 | from rich import print
  |
help: Remove unused import: `random`

F401 [*] `rich.print` imported but unused
 --> quotes_generator.py:5:18
  |
3 | import random
4 |
5 | from rich import print
  |                  ^^^^^
6 | from rich.text import text
  |
help: Remove unused import: `rich.print`

F401 [*] `rich.text.text` imported but unused
 --> quotes_generator.py:6:23
  |
5 | from rich import print
6 | from rich.text import text
  |                       ^^^^
  |
help: Remove unused import: `rich.text.text`

```

---

```python3
# ruff check <file_name> --select I
ruff check <file_name> --select I


@AshuApurva14 ➜ /workspaces/python-for-devops/structure_your_py_script (main) $ ruff check quotes_generator.py --select I
All checks passed!
```

---

Add some issue:

```python3
# ruff check <file_name > --select I --fix

AshuApurva14 ➜ /workspaces/python-for-devops/structure_your_py_script (main) $ ruff check quotes_generator.py --select I
I001 [*] Import block is un-sorted or un-formatted
 --> quotes_generator.py:3:1
  |
1 |   #!/usr/bin/env python3
2 |
3 | / import random
4 | |
5 | | from rich import print
6 | |
7 | | from rich.text import text
  | |__________________________^
  |
help: Organize imports

Found 1 error.
[*] 1 fixable with the `--fix` option.
@AshuApurva14 ➜ /workspaces/python-for-devops/structure_your_py_script (main) $ ruff check quotes_generator.py --select I --fix
Found 1 error (1 fixed, 0 remaining).
@AshuApurva14 ➜ /workspaces/python-for-devops/structure_your_py_script (main) $ 

```

### Using Constant

Constants are:

- Variables defined in a single place
- Designed not to be changed
- Defined in ALL CAPS  by Python convention
- Something like this FILE_PATH = 'path/to/file'


