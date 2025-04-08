from collections import Counter

def transform(word1: str, word2: str):
    # check if the two strings can be transformed
    if len(word1) != len(word2):
        print("The two strings are not of the same length.")
        return None
    if set(word1) != set(word2):
        print("The two strings contain different character sets and cannot be transformed.")
        return None

    c1 = Counter(word1)
    c2 = Counter(word2)
    if sorted(c1.values()) != sorted(c2.values()):
        print("The frequency sets of the two strings are different and cannot be transformed.")
        return None

    steps = []
    steps.append(("initial", word1))
    
    ###################################
    # Stage 1: Global Character Swap (Operation 2)
    ###################################
    # 构造映射：对于 word1 中的每个字符，分配一个在 word2 中出现且出现次数匹配的目标字符。
    mapping = {}
    # 若某字符在两个字符串中的频率相同，则优先映射到它自身
    for ch in c1:
        if c1[ch] == c2[ch]:
            mapping[ch] = ch

    # 对于未确定映射的字符，按相同频率进行分组，然后建立一一对应映射
    unmapped = [ch for ch in c1 if ch not in mapping]
    freq_groups = {}
    for ch in unmapped:
        f = c1[ch]
        if f not in freq_groups:
            freq_groups[f] = {'src': [], 'tgt': []}
        freq_groups[f]['src'].append(ch)
    for ch in c2:
        # 排除已经用作身份映射的字符
        if ch not in mapping or mapping.get(ch) != ch:
            f = c2[ch]
            if f in freq_groups:
                freq_groups[f]['tgt'].append(ch)
    for f in freq_groups:
        src_list = freq_groups[f]['src']
        tgt_list = freq_groups[f]['tgt']
        # 理论上两个列表长度应相同，按顺序对应
        for i in range(len(src_list)):
            mapping[src_list[i]] = tgt_list[i]

    # 生成全局字符交换的操作序列
    # 先将映射看作一个置换，然后将每个非平凡循环转化为（循环长度-1）次操作2
    op2_steps = []
    visited = set()
    for ch in mapping:
        if ch in visited:
            continue
        cycle = []
        current = ch
        while current not in visited:
            visited.add(current)
            cycle.append(current)
            current = mapping[current]
        if len(cycle) > 1:
            # 对于 cycle = [a, b, c, ...] 使用 swap(a, x) 依次将周期内字符“固定”
            for i in range(len(cycle)-1, 0, -1):
                op2_steps.append(("swap_labels", cycle[0], cycle[i]))

    # 定义操作2（全局字符交换）的模拟函数：
    def apply_op2(s: str, ch1: str, ch2: str) -> str:
        # 将字符串中所有 ch1 与 ch2 对调
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == ch1:
                s_list[i] = ch2
            elif s_list[i] == ch2:
                s_list[i] = ch1
        return "".join(s_list)

    # 依次应用所有操作2，将 word1 全局转换为符合 word2 中频率分布的状态
    transformed = word1
    for op in op2_steps:
        _, a, b = op
        new_transformed = apply_op2(transformed, a, b)
        step_desc = f"Operation2: turn all '{a}' into '{b}'"
        steps.append((step_desc, new_transformed))
        transformed = new_transformed

    ###################################
    # 阶段2：通过位置交换调整字符顺序（操作1）
    ###################################
    op1_steps = []
    arr = list(transformed)
    target = list(word2)
    n = len(arr)
    # 贪心交换：依次检查每个位置，不匹配则找到后面合适的字符交换到当前位置
    for i in range(n):
        if arr[i] != target[i]:
            j = None
            for k in range(i+1, n):
                # 选择一个目标字符匹配且当前位置尚未正确
                if arr[k] == target[i] and arr[k] != target[k]:
                    j = k
                    break
            if j is not None:
                arr[i], arr[j] = arr[j], arr[i]
                op1_steps.append((i, j))
                step_desc = f"Operation1: swap({i}, {j})"
                steps.append((step_desc, "".join(arr)))
    
    total_ops = len(op2_steps) + len(op1_steps)

    ###################################
    # Output
    ###################################
    print(" 「Transform Completed」Total operations =", total_ops)
    for desc, s in steps:
        print(desc, "=>", s)
    
    return total_ops, steps
