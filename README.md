# PyPTO-Pro 学习笔记与练习

90天编译器与算子学习安排，每天约1—2小时，包含源码阅读、CPU/IR小实验、算子编写和阶段验收。

## 开始

```bash
git clone https://github.com/Yushouxixiwo/pypto_pro_learning_90days_2026.git
cd pypto_pro_learning_90days_2026
python3 day01_exercise.py
```

Day1为纯Python CPU教学模型，无需torch、PyPTO或NPU。它不证明设备正确性或性能。

- [完整计划](90天学习计划.md)
- [第1天讲义与题目](Day01样稿.md)
- [第1天可运行练习](day01_exercise.py)
- `plan.json`：每日主题、练习与验收。
- `progress.json`：初始进度；推送课程不表示已经学完。

后续解答建议放入 `answers/`，笔记放入 `notes/`；运行日志不进入版本库。

## 本地源码路径

讲义中的 `${PYPTO_SRC}`、`${PYPTO_SKILL_ROOT}`、`${PYPTO_GYM_ROOT}` 分别表示你自己的框架源码、新版算子资料和原知识库根目录，按实际环境设置。
源码、安装包和硬件版本分开核实。设备实验使用独立工作目录，不修改共享环境。
