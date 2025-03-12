# TimeLLM-Prob-Forecasting  

🚀 **基于 TimeLLM 的多模态时间序列概率预测**  

本项目基于 **TimeLLM 框架**，在 Hugging Face 上使用 **LLaMA2-7B** 预训练模型，  
结合 **重尾分位数分布函数** 扩展 LLM 进行 **概率预测**，  
在 **KDD 2022 Wind Cup** 数据集上超越 **Crossformer、Informer、Fedformer** 等主流时间序列模型。  

---

## 🔥 主要特性  
✅ **TimeLLM for Probabilistic Forecasting**  
- 采用 **Prompt-as-Prefix（PaP）** 机制，将时间序列数据转换为 LLM 兼容格式  
- 引入 **重尾分位数分布函数**，扩展 TimeLLM 框架以支持概率预测  
- 兼容 **LLaMA2-7B、通义千问、GPT-2**，对比不同 LLM 在时间序列任务中的泛化能力  

✅ **Benchmark Comparisons**  
- 在 **KDD 2022 Wind Cup** 数据集上进行风速预测  
- 对比 **Crossformer、Informer、Fedformer** 等主流时间序列模型，显著提升预测精度  

✅ **可视化 & 解释性**  
- 预测结果可视化：**预测均值、不确定性区间、概率分布**  

## 📚 参考文献  

如果你对 TimeLLM 框架感兴趣，推荐阅读以下论文：  

- Jin, Ming, et al. "**Time-LLM: Time series forecasting by reprogramming large language models**."  
  *International Conference on Learning Representations (ICLR), 2024.*  
  [[Paper](https://arxiv.org/abs/your-link)]  

本项目基于 TimeLLM 框架，并在 KDD 2022 Wind Cup 数据集上进行了实验验证。  
