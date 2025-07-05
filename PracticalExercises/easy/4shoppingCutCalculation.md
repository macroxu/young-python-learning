04 购物折扣计算（满减与打折）---python 实战初级

### 一、购物折扣计算（满减与打折）

#### 1 题目描述

商场促销活动：购物满 200 元减 50 元，或全场 8.5 折（两者取优惠力度更大的方式）。输入商品总价，计算实际支付金额。

#### 2 示例输入输出

**例 1**

```python
请输入商品总价：250
实际支付金额：200.0 元

```

**例 2**

```python
请输入商品总价：420
实际支付金额：357.0 元

```

#### 3 解题逻辑

1. **输入商品总价**：使用 `input()` 函数获取用户输入的商品总价，并转换为浮点数。
2. **计算满减优惠**：如果商品总价大于等于 200 元，则计算满减后的价格：`total_price - 50`。
3. **计算打折优惠**：计算打折后的价格：`total_price * 0.85`。
4. **比较优惠力度**：取满减和打折两种方式中更优惠的价格。
5. **输出实际支付金额**：使用 `print()` 函数格式化输出实际支付金额，保留两位小数。

#### 4 代码实现

```python

total_price = float(input("请输入商品总价："))
# 计算满减优惠
if total_price >= 200:
    discount_price = total_price - 50
else:
    discount_price = total_price
# 计算打折优惠
discount_price_85 = total_price * 0.85
# 比较两个优惠方式，取更优惠的价格
if discount_price_85 < discount_price:
    final_price = discount_price_85
else:
    final_price = discount_price

# 输出实际支付金额，保留两位小数
print(f"实际支付金额：{final_price:.2f} 元")

```
