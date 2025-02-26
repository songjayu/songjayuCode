# ⏳ **코딩 테스트에서 `sys.stdin.readline()`을 사용해야 할까?**

## ✅ **`input()` vs. `sys.stdin.readline()` 비교**

코딩 테스트에서는 **입력 속도가 중요한 경우**가 많아.  
특히 **반복문에서 많은 입력을 받을 때** `sys.stdin.readline()`을 쓰면 훨씬 빠른 속도를 낼 수 있어!  

---

## ⏳ **입력 속도 비교**

| 입력 방식              | 코드                                   | 속도                           |
| ---------------------- | -------------------------------------- | ------------------------------ |
| `input()`              | `x = input()`                          | ❌ 느림 (한 줄씩 처리)          |
| `sys.stdin.readline()` | `import sys; x = sys.stdin.readline()` | ✅ 빠름 (버퍼에서 한 번에 읽음) |

📌 **이유:**  

- `input()`은 **한 줄 입력받을 때마다 내부적으로 `sys.stdin.readline()`을 호출**하지만,  
  추가적으로 **문자열 처리를 더 수행**해서 상대적으로 느려짐.  
- `sys.stdin.readline()`은 **한 번에 입력을 받아 버퍼에서 처리**하기 때문에 속도가 훨씬 빠름.

---

## 🚀 **언제 `sys.stdin.readline()`을 써야 할까?**

### ✅ **1. 많은 줄의 입력을 받아야 할 때**

```python
import sys
n = int(sys.stdin.readline())  # 빠른 입력
```

```
- `input()`보다 빠르게 여러 줄을 읽을 수 있음.

---

## ✅ **2. 여러 개의 정수를 한 줄에서 입력받을 때**
```python
import sys
a, b, c = map(int, sys.stdin.readline().split())  # 공백으로 구분된 정수 입력받기
```

- `input()`보다 빠르고 효율적으로 동작.

------

## ✅ **3. 리스트에 여러 개의 입력을 받을 때**

```
python복사편집import sys
data = list(map(int, sys.stdin.readline().split()))
```

- 한 줄에서 여러 개의 정수를 받을 때도 **버퍼를 활용해 빠르게 처리 가능**.

------

## ⚠️ **주의할 점**

### ❌ **1. `sys.stdin.readline()`은 `\n`(개행 문자)을 포함한다**

- `sys.stdin.readline()`으로 문자열을 입력받으면 끝에 `\n`이 포함됨.
- 따라서 문자열을 입력받을 경우 `.strip()`을 붙여서 개행 문자를 제거하는 게 좋음.

```
python복사편집import sys
s = sys.stdin.readline().strip()  # 개행 문자 제거
```

### ❌ **2. 입력이 한두 개면 그냥 `input()`을 써도 괜찮음**

- 입력이 많지 않다면 `sys.stdin.readline()`을 쓸 필요 없이 그냥 `input()`을 써도 됨.
- `sys.stdin.readline()`은 **너무 적은 입력에서는 오히려 불편**할 수 있음.

------

## 🎯 **최종 결론**

- 입력이 많을 경우 **`sys.stdin.readline()`을 사용하면 속도를 줄일 수 있음**.
- 특히 **반복문에서 많은 입력을 받을 때** `input()` 대신 `sys.stdin.readline()`을 쓰는 것이 유리함.
- 하지만 문자열 입력을 받을 때는 **`\n`을 포함하므로 `.strip()`을 활용하는 것이 중요**!

✅ **결론:**

- **입력이 많은 문제에서는 `sys.stdin.readline()`을 사용하자!** 🚀
- **단, 문자열 입력 시 개행 문자 제거(`.strip()`)를 잊지 말자!**
