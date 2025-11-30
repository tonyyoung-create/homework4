# -*- coding: utf-8 -*-
import sys
import random

# 設定隨機種子以便測試
random.seed(42)

# 直接導入核心邏輯
class TopicAnalyzer:
    def __init__(self):
        self.negative_keywords = [
            "痛苦", "失敗", "困難", "問題", "危機", "破裂", "崩潰", "完蛋",
            "衰退", "下滑", "虧損", "災難", "糟糕", "惡劣", "腐敗", "堕落",
            "衝擊", "衰弱", "頹廢", "挑戰", "威脅", "風險", "死亡", "戰爭",
            "恐怖", "害怕", "擔心", "焦慮", "不安", "混亂", "無序", "貧窮",
            "餓", "病", "傷", "罪", "邪惡", "黑暗", "污穢", "難過", "悲傷",
            "沮喪", "失望", "絕望", "憂鬱", "痛心", "傷心", "難受"
        ]
        
        self.positive_keywords = [
            "偉大", "成功", "勝利", "榮耀", "繁榮", "財富", "權力", "聰慧",
            "強大", "美好", "光明", "未來", "希望", "夢想", "機會", "融資",
            "投資", "增長", "發展", "進步", "智慧", "才能", "領導", "勇敢",
            "英雄", "冠軍", "贏家", "最佳", "優秀", "傑出", "卓越", "非凡"
        ]
    
    def analyze_sentiment(self, topic):
        negative_count = sum(1 for kw in self.negative_keywords if kw in topic)
        positive_count = sum(1 for kw in self.positive_keywords if kw in topic)
        
        if negative_count > positive_count:
            return "negative"
        elif positive_count > negative_count:
            return "positive"
        else:
            return "neutral"

# 測試
analyzer = TopicAnalyzer()

print("=" * 50)
print("測試 1: 負面話題")
print("=" * 50)
topic1 = "我很難過"
sentiment1 = analyzer.analyze_sentiment(topic1)
print(f"話題: {topic1}")
print(f"感情分析: {sentiment1}")
print(f"預期: negative")
print(f"結果: {'✓ 正確' if sentiment1 == 'negative' else '✗ 錯誤'}")

print("\n" + "=" * 50)
print("測試 2: 正面話題")
print("=" * 50)
topic2 = "公司融資成功"
sentiment2 = analyzer.analyze_sentiment(topic2)
print(f"話題: {topic2}")
print(f"感情分析: {sentiment2}")
print(f"預期: positive")
print(f"結果: {'✓ 正確' if sentiment2 == 'positive' else '✗ 錯誤'}")

print("\n" + "=" * 50)
print("測試 3: 中立話題")
print("=" * 50)
topic3 = "今天天氣如何"
sentiment3 = analyzer.analyze_sentiment(topic3)
print(f"話題: {topic3}")
print(f"感情分析: {sentiment3}")
print(f"預期: neutral")
print(f"結果: {'✓ 正確' if sentiment3 == 'neutral' else '✗ 錯誤'}")
