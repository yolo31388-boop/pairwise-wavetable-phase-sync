# pairwise-wavetable-phase-sync

## 领域

游戏、图形与多媒体

## 主题

波表合成器相位对齐

## 说明

按采样率索引、每音符独立状态、包络按样本推进。

初始状态下 `av/wavetable_phase.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
